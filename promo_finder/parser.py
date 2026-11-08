"""Parse parallel screenplay tracks without adding their durations together."""
import hashlib
import re
from decimal import Decimal
from pathlib import Path

from .models import Episode, Event, Scene

TIME = r"\d{1,3}:\d{2}(?:\.\d{1,2})?"
BLOCK = re.compile(
    rf"^\*\*(?P<label>[^\n]+?)\*\*\s*\n"
    rf"Start:\s*\((?P<start>{TIME})\)\s*\|\s*End:\s*\((?P<end>{TIME})\)\s*\n"
    r"(?P<text>.*?)(?=\n\s*\n|\Z)", re.M | re.S | re.I,
)


def parse_time(value: str) -> int:
    minutes, seconds = value.strip().split(":")
    seconds_value = Decimal(seconds)
    if not 0 <= seconds_value < 60 or int(minutes) < 0:
        raise ValueError(f"Invalid timestamp: {value}")
    return int((int(minutes) * 60 + seconds_value) * 100)


def timestamp(cs: int) -> str:
    return f"{cs // 6000:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def _metadata(text: str, name: str) -> str:
    match = re.search(rf"^{name}:\s*(.*)$", text, re.M | re.I)
    return match.group(1).strip() if match else ""


def parse_episode(path: Path) -> Episode:
    text = path.read_text(encoding="utf-8-sig")
    match = re.search(r"^EPISODE NUMBER:\s*(?:Episode\s*)?(\d+)\s*$", text, re.M | re.I)
    if not match:
        raise ValueError("Missing or invalid EPISODE NUMBER")
    number = int(match.group(1))
    eid = f"ep-{number:03d}"
    scene_matches = list(re.finditer(r"^SCENE\s+(\d+)\s*$", text, re.M | re.I))
    if not scene_matches:
        raise ValueError("No scene sections found")
    scenes, events, warnings = [], [], []
    total_headers = len(re.findall(r"^\*\*[^\n]+\*\*\s*$", text, re.M))
    seen_scenes = set()
    for i, scene_match in enumerate(scene_matches):
        sid = f"{eid}-s{int(scene_match.group(1)):02d}"
        if sid in seen_scenes:
            raise ValueError(f"Duplicate scene identifier: {sid}")
        seen_scenes.add(sid)
        start = scene_match.end()
        end = scene_matches[i + 1].start() if i + 1 < len(scene_matches) else len(text)
        section = text[start:end]
        scene_start = _metadata(section, "Scene start")
        scene_end = _metadata(section, "Scene end")
        if not scene_start or not scene_end:
            raise ValueError(f"Missing scene timestamps: {sid}")
        scene = Scene(id=sid, heading=_metadata(section, "Scene heading"),
                      start_cs=parse_time(scene_start), end_cs=parse_time(scene_end))
        if scene.end_cs <= scene.start_cs:
            raise ValueError(f"Non-positive scene duration: {sid}")
        scenes.append(scene)
        for block in BLOCK.finditer(section):
            label = block.group("label").strip().rstrip(":")
            base = label.split("(", 1)[0].strip().upper()
            kind = {"CAMERA": "camera", "ACTION": "action", "SOUND FX": "sound"}.get(base, "dialogue")
            direction = label[label.find("("):] if "(" in label else None
            event = Event(
                id=f"{eid}-b{len(events) + 1:04d}", scene_id=sid, kind=kind,
                speaker=base if kind == "dialogue" else None, direction=direction,
                start_cs=parse_time(block.group("start")), end_cs=parse_time(block.group("end")),
                text=block.group("text").strip(), line=text.count("\n", 0, start + block.start()) + 1,
            )
            if event.end_cs <= event.start_cs or not event.text:
                raise ValueError(f"Empty or non-positive event at line {event.line}")
            if event.start_cs < scene.start_cs or event.end_cs > scene.end_cs:
                warnings.append(f"{event.id} extends outside its declared scene")
            events.append(event)
    if len(events) != total_headers:
        raise ValueError(f"Parsed {len(events)} of {total_headers} event headers; source needs inspection")
    if not events:
        raise ValueError("No timestamped events")
    return Episode(
        id=eid, number=number, source_path=str(path.resolve()),
        source_hash=hashlib.sha256(text.encode()).hexdigest(),
        logline=_metadata(text, "EPISODE LOGLINE"), continuity=_metadata(text, "CONTINUITY NOTES"),
        duration_cs=max([s.end_cs for s in scenes] + [e.end_cs for e in events]),
        scenes=scenes, events=events, warnings=warnings,
    )


def load_folder(folder: Path) -> tuple[list[Episode], list[dict]]:
    if not folder.is_dir():
        raise ValueError(f"Input folder does not exist: {folder}")
    paths = sorted(folder.glob("*.txt"))
    if not paths:
        raise ValueError("No .txt screenplay files in input folder")
    episodes, errors, seen = [], [], set()
    for path in paths:
        try:
            episode = parse_episode(path)
            if episode.id in seen:
                raise ValueError(f"Duplicate episode number: {episode.number}")
            seen.add(episode.id)
            episodes.append(episode)
        except (ValueError, OSError) as exc:
            errors.append({"file": str(path.resolve()), "error": str(exc)})
    return sorted(episodes, key=lambda e: e.number), errors
