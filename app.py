"""Local review interface. Viewing saved results never calls the API."""
import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

from promo_finder.cli import DEFAULT_INPUT, ROOT, load_environment
from promo_finder.models import Candidate, Episode, WEIGHTS
from promo_finder.parser import load_folder, timestamp
from promo_finder.pipeline import run_pipeline
from promo_finder.provider import OpenAIProvider
from promo_finder.reporting import comparison_rows, csv_text, export_report, load_results, load_reviews, posting_order
from promo_finder.storage import read_json, write_json
from promo_finder.validation import assemble_clip

load_environment()
st.set_page_config(page_title="Kuku · Promo Finder", page_icon="🎬", layout="wide")
st.markdown("""<style>
:root {
    --paper: #f3f0e7;
    --surface: #fcfaf4;
    --ink: #203c32;
    --muted: #656b5e;
    --line: #d8d8ca;
    --clay: #ab4d30;
}
[data-testid="stAppViewContainer"] {background: var(--paper)}
[data-testid="stHeader"] {background: #f3f0e7ed}
.block-container {padding-top:4.5rem;padding-bottom:4rem;max-width:1380px}
.studio-masthead {
    display:flex;align-items:center;justify-content:space-between;gap:1rem;
    border-bottom:1px solid var(--line);padding-bottom:1.1rem;margin-bottom:1.7rem;
}
.studio-brand {display:flex;align-items:center;gap:.7rem}
.studio-monogram {
    display:grid;place-items:center;width:34px;height:34px;background:var(--ink);
    color:var(--surface);font-family:Georgia,serif;font-size:25px;border-radius:3px;
}
.eyebrow {font-size:11px;font-weight:700;letter-spacing:2px;color:var(--ink)}
.studio-edition {font-size:10px;letter-spacing:1.5px;color:var(--muted);text-align:right}
[data-testid="stMain"] h1 {
    font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.4rem,4.5vw,4rem);
    font-weight:400;line-height:1.08;letter-spacing:-2px;color:var(--ink);
    max-width:1040px;padding-top:0;padding-bottom:.8rem;
}
[data-testid="stMain"] h2, [data-testid="stMain"] h3 {color:var(--ink);letter-spacing:-.4px}
[data-testid="stMain"] [data-testid="stCaptionContainer"] {color:var(--muted)}
.scope-note {
    display:flex;align-items:baseline;gap:.85rem;flex-wrap:wrap;padding:.8rem 1rem;
    margin:.8rem 0 1.6rem;border-left:3px solid var(--clay);background:#eae7db;
    color:#4f584b;font-size:.88rem;line-height:1.6;
}
.scope-note strong {color:var(--ink);font-weight:650;white-space:nowrap}
[data-testid="stMetric"] {
    min-height:126px;background:var(--surface);border:1px solid var(--line);
    border-top:3px solid #9b9e76;border-radius:5px;padding:18px 22px;
}
[data-testid="stMetricLabel"] {color:var(--muted);font-size:.78rem;letter-spacing:.3px}
[data-testid="stMetricValue"] {
    font-family:Georgia,"Times New Roman",serif;color:var(--ink);font-size:2.7rem;
    font-weight:400;line-height:1.25;
}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child [data-testid="stMetric"] {
    background:var(--ink);border-color:var(--ink);
}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child [data-testid="stMetricLabel"] {color:#cbd4bb}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child [data-testid="stMetricValue"] {color:#f8efd9}
[data-testid="stMain"] [data-baseweb="tab-list"] {
    gap:1.5rem;background:transparent;border-bottom:1px solid var(--line);margin-top:.8rem;
}
[data-testid="stMain"] [data-baseweb="tab"] {
    padding:.7rem .1rem;font-weight:550;color:var(--muted);height:auto;
}
[data-testid="stMain"] [data-baseweb="tab"][aria-selected="true"] {color:var(--ink);font-weight:700}
[data-testid="stMain"] [data-baseweb="tab-highlight"] {background:var(--clay);height:3px}
[data-testid="stMain"] [data-baseweb="tab-panel"] {padding-top:1.5rem}
[data-testid="stWidgetLabel"] p {font-size:.85rem;font-weight:600}
[data-testid="stCode"] {
    border:1px solid var(--line);border-left:3px solid #9b9e76;border-radius:4px;
}
[data-testid="stCode"] pre {line-height:1.75;font-size:.82rem}
[data-testid="stForm"] {background:var(--surface);border:1px solid var(--line);border-radius:5px;padding:1.4rem}
[data-testid="stExpander"] {background:var(--surface);border-radius:5px}
.stButton button, .stDownloadButton button, [data-testid="stFormSubmitButton"] button {
    font-weight:600;padding:.55rem 1rem;transition:background-color .15s,border-color .15s;
}
.stButton button:hover, .stDownloadButton button:hover {border-color:var(--clay)}
[data-testid="stSidebar"] {border-right:1px solid #314e40}
[data-testid="stSidebarContent"] {padding-top:1.5rem}
[data-testid="stSidebar"] h2 {font-family:Georgia,serif;font-weight:400;font-size:1.8rem}
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {color:#c2cdb9}
[data-testid="stSidebar"] hr {border-color:#49604d}
.sidebar-kicker {color:#d8b77c;font-size:10px;letter-spacing:2px;font-weight:700;margin-bottom:.7rem}
.sidebar-rules {margin:.8rem 0 1rem;padding:0;list-style:none}
.sidebar-rules li {
    display:flex;gap:.8rem;padding:.65rem 0;border-bottom:1px solid #3c5547;
    font-size:.85rem;color:#eff0df;
}
.sidebar-rules span {color:#d8b77c;font-family:Georgia,serif;font-size:1rem;min-width:22px}
@media (max-width:760px) {
    .block-container {padding-top:4.5rem}
    .studio-edition {display:none}
    [data-testid="stMain"] h1 {letter-spacing:-1px}
    [data-testid="stMetric"] {padding:14px;min-height:105px}
    [data-testid="stMetricValue"] {font-size:2rem}
    [data-testid="stHorizontalBlock"]:has([data-testid="stMetric"]) {flex-wrap:wrap}
    [data-testid="stHorizontalBlock"]:has([data-testid="stMetric"]) > [data-testid="stColumn"] {
        flex:1 1 calc(50% - .5rem);min-width:0;
    }
    [data-testid="stMain"] [data-baseweb="tab-list"] {gap:1rem}
    [data-testid="stMain"] [data-baseweb="tab"] {font-size:.85rem}
}
</style>""", unsafe_allow_html=True)
st.markdown('''<div class="studio-masthead">
    <div class="studio-brand"><span class="studio-monogram">k</span>
    <span class="eyebrow">KUKU / PROMO STUDIO</span></div>
    <span class="studio-edition">THE EDITORIAL WORKSPACE</span>
</div>''', unsafe_allow_html=True)
st.title("Find the moment. Leave a question.")
st.caption("Turn episode scripts into a shortlist worth watching. Find the hook, review the cut, choose what goes first.")
st.markdown('''<div class="scope-note"><strong>One episode. A stronger cut.</strong>
    <span>Build a continuous promo or join moments from the same episode.</span></div>''', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-kicker">YOUR EDITING DESK</div>', unsafe_allow_html=True)
    st.header("Workspace")
    folders = sorted({p.parent for p in (ROOT / "runs").glob("*/inventory.json")}, key=lambda p: str(p))
    options = ["Source scripts only"] + [str(p.relative_to(ROOT)) for p in folders]
    preferred_run = next((r for r in ("runs/full", "runs/demo") if r in options), "Source scripts only")
    chosen = st.selectbox("Saved run", options, index=options.index(preferred_run))
    run = ROOT / chosen if chosen != options[0] else None
    st.caption("Saved results open without an API call.")
    show_judge = st.checkbox("Show model scores and explanations", value=False)
    st.caption("Leave scores hidden to record your first impression independently.")
    st.divider()
    st.markdown("**Selection rules**")
    st.markdown('''<ul class="sidebar-rules">
        <li><span>01</span>20–60 seconds per promo</li>
        <li><span>02</span>A hook in the first 3 seconds</li>
        <li><span>03</span>Clear characters and stakes</li>
        <li><span>04</span>An ending that leaves a question</li>
    </ul>''', unsafe_allow_html=True)
    st.caption("Script-based editorial assessment. Delivery and precise timing need footage review.")

sources, parse_errors, results = [], [], []
if run is not None:
    inventory = read_json(run / "inventory.json")
    sources = [Episode.model_validate(e) for e in inventory["episodes"]]
    parse_errors = inventory["errors"]
    results = load_results(run)
elif DEFAULT_INPUT.is_dir():
    sources, parse_errors = load_folder(DEFAULT_INPUT)
reviews = load_reviews(run) if run else {}
rows = comparison_rows(results, reviews)
by_episode = {e["episode_id"]: e for e in results}

stats = st.columns(4)
stats[0].metric("Episodes available", len(sources))
stats[1].metric("Episodes analysed", len(results))
stats[2].metric("Candidates selected", len(rows))
stats[3].metric("Qualified by model", sum(r["status"] == "qualified" for r in rows) if show_judge else "Hidden")
if parse_errors:
    st.error(f"{len(parse_errors)} input file(s) need parser review")
    st.json(parse_errors)

episode_tab, ranking_tab, run_tab = st.tabs(["Episode review", "Compare & export", "Prepare & run"])


def render_clip(clip: dict) -> None:
    for segment in clip["segments"]:
        st.markdown(f"**Segment {segment['segment_number']}** · source {timestamp(segment['source_start_cs'])}–"
                    f"{timestamp(segment['source_end_cs'])} · playback {timestamp(segment['playback_start_cs'])}–"
                    f"{timestamp(segment['playback_end_cs'])}")
        lines = []
        for event in segment["events"]:
            who = f" · {event['speaker']}" if event["speaker"] else ""
            partial = " [partial event]" if event["partial"] else ""
            lines.append(f"{timestamp(event['playback_start_cs'])}–{timestamp(event['playback_end_cs'])} "
                         f"{event['kind'].upper()}{who}{partial} [{event['event_id']}]\n{event['text']}")
        st.code("\n\n".join(lines), language=None, wrap_lines=True)


with episode_tab:
    if not sources:
        st.write("Load a script folder or upload scripts in Prepare & run.")
    else:
        first_processed = next((i for i, e in enumerate(sources) if e.id in by_episode), 0)
        episode = st.selectbox("Episode", sources, index=first_processed,
                               format_func=lambda e: f"Episode {e.number:02d} · {timestamp(e.duration_cs)}")
        result = by_episode.get(episode.id)
        if show_judge and result:
            st.caption(f"Processing status: {result['status']}")
        for warning in episode.warnings:
            st.warning(f"Source timing warning: {warning}")
        candidates = result["candidates"] if result else []
        if not candidates:
            st.write("No candidates have been selected for this episode yet." if not result else
                     result.get("no_candidate_reason", "No candidate returned; inspect the saved output."))
            with st.expander("Inspect timestamped source", expanded=not bool(result)):
                st.dataframe([{"id": e.id, "type": e.kind, "start": timestamp(e.start_cs), "end": timestamp(e.end_cs),
                               "speaker": e.speaker or "", "text": e.text} for e in episode.events], hide_index=True,
                             column_config={"text": st.column_config.TextColumn(width="large")})
        else:
            selected = st.selectbox("Candidate", candidates, format_func=lambda c: f"{c['id']} · {c['type']} · "
                                    f"{c['validation']['duration_cs'] / 100:.2f}s")
            candidate = Candidate.model_validate(selected["candidate"])
            # A neutral candidate ID prevents the selector's persuasive title/rationale influencing blind review.
            st.subheader(selected["id"])
            opening, full, source_tab = st.tabs(["First 3 seconds", "Assembled promo", "Source references"])
            with opening:
                st.caption("Partial dialogue words are withheld: the screenplay does not time individual words.")
                render_clip(assemble_clip(episode, candidate, 300))
            with full:
                render_clip(assemble_clip(episode, candidate))
            with source_tab:
                ids = set(selected["validation"]["source_event_ids"])
                st.dataframe([{"event": e.id, "line": e.line, "source_start": timestamp(e.start_cs),
                               "source_end": timestamp(e.end_cs), "text": e.text}
                              for e in episode.events if e.id in ids], hide_index=True)
            for issue in selected["validation"]["errors"]:
                st.error(issue)
            for flag in selected["validation"]["flags"]:
                st.warning(flag)
            if show_judge:
                st.markdown(f"**{candidate.title}** · {selected['status']} · score {selected['score']}")
                st.write(candidate.rationale)
                if selected["judge"]:
                    judgement = selected["judge"]
                    st.write("**Newcomer situation:**", judgement["newcomer_situation"])
                    st.write("**Continuation question:**", judgement["continuation_question"])
                    st.dataframe([{"criterion": k.replace("_", " "), "weight": WEIGHTS[k],
                                   "score / 5": v["value"], "evidence": ", ".join(v["evidence_ids"]),
                                   "reason": v["reason"]} for k, v in judgement["scores"].items()], hide_index=True)
                    st.write("**Main weakness:**", judgement["main_weakness"])
                    with st.expander("Eligibility and fidelity checks"):
                        st.json({k: v for k, v in judgement.items() if isinstance(v, dict) and k != "scores"})
                        st.json(selected["fidelity"])
                    st.caption(judgement["footage_review"])
                for error in selected["errors"]:
                    st.error(error)
            if run:
                st.divider()
                st.markdown("**Your editorial review**")
                saved = reviews.get(selected["id"], {})
                with st.form(f"review-{selected['id']}"):
                    decisions = ["needs_review", "approve", "reject"]
                    decision = st.selectbox("Decision", decisions, index=decisions.index(saved.get("decision", "needs_review")))
                    situation = st.text_area("Who matters, and what could they lose?", value=saved.get("situation", ""))
                    continuation = st.text_area("What specifically do you want to see next?", value=saved.get("continuation", ""))
                    note = st.text_area("Weakness, disagreement, or correction", value=saved.get("note", ""))
                    if st.form_submit_button("Save human review"):
                        write_json(run / "reviews" / f"{selected['id']}.json", {"candidate_id": selected["id"],
                                   "decision": decision, "situation": situation, "continuation": continuation,
                                   "note": note, "model_scores_visible": show_judge,
                                   "updated_at": datetime.now(timezone.utc).isoformat()})
                        st.success("Review saved separately from model outputs.")

with ranking_tab:
    if not results:
        st.write("Comparisons will appear after a saved model run. No scores have been fabricated.")
    else:
        st.caption("Comparing episode promos does not combine episodes into a series promo.")
        st.caption("Posting priority follows score, then cliffhanger, newcomer clarity, and opening impact. "
                   "Equal scores remain tied; episode number earns no preference. Human-rejected cuts are excluded.")
        status_filter = st.multiselect("Eligibility", ["qualified", "needs_review", "rejected", "api_failed"],
                                       default=["qualified", "needs_review"])
        type_filter = st.multiselect("Clip type", ["continuous", "joined"], default=["continuous", "joined"])
        filtered = [r for r in rows if r["status"] in status_filter and r["type"] in type_filter]
        columns = ["id", "episode", "type", "duration_seconds", "segments", "human_review"]
        if show_judge:
            columns = ["global_rank", "episode_rank", "score", "status", "title"] + columns
            priorities = {r["id"]: r["posting_priority"] for r in posting_order(rows)}
            columns = ["posting_priority"] + columns
            filtered = [{**r, "posting_priority": priorities.get(r["id"])} for r in filtered]
            filtered = sorted(filtered, key=lambda r: (r["posting_priority"] or 100000, -(r["score"] or 0)))
        else:
            st.caption("Scores are hidden; candidate order follows source episodes for independent review.")
        st.dataframe([{k: r[k] for k in columns} for r in filtered], hide_index=True)
        if st.button("Refresh exports from saved results"):
            export_report(run)
            st.success("JSON, CSV, coverage and Markdown report refreshed.")
        st.download_button("Download comparisons CSV", csv_text(rows), file_name="episode-promos.csv", mime="text/csv")
        st.download_button("Download global posting order", csv_text(posting_order(rows)),
                           file_name="global-posting-order.csv", mime="text/csv")
        coverage = [{"episode": e.number, "status": by_episode.get(e.id, {}).get("status", "not_processed"),
                     "candidates": len(by_episode.get(e.id, {}).get("candidates", []))} for e in sources]
        with st.expander("Every episode: coverage and processing status"):
            st.dataframe(coverage, hide_index=True)
        if (run / "summary.json").exists():
            with st.expander("Run usage"):
                st.json(read_json(run / "summary.json").get("usage", {}))

with run_tab:
    st.subheader("Prepare an episode-only run")
    st.caption("This button sends the selected scripts to your configured OpenAI API. Reviewing results does not.")
    input_mode = st.radio("Script input", ["Folder", "Upload", "Paste"], horizontal=True)
    input_folder = str(DEFAULT_INPUT if DEFAULT_INPUT.exists() else ROOT / "examples")
    uploaded = []
    if input_mode == "Folder":
        input_folder = st.text_input("Script folder", value=input_folder)
    elif input_mode == "Upload":
        uploaded = st.file_uploader("Upload timestamped episode .txt files", type=["txt"], accept_multiple_files=True)
        if not uploaded:
            input_folder = str(ROOT / "runs" / "no-upload-selected")
    else:
        pasted = st.text_area("Paste one timestamped episode script", height=220,
                              placeholder="EPISODE NUMBER: Episode 1\n... scenes, camera/action/dialogue and Start/End timestamps ...")
        if pasted.strip():
            paste_hash = hashlib.sha256(pasted.encode()).hexdigest()[:16]
            paste_folder = ROOT / "runs" / "pasted" / paste_hash
            paste_folder.mkdir(parents=True, exist_ok=True)
            (paste_folder / "episode.txt").write_text(pasted, encoding="utf-8")
            input_folder = str(paste_folder)
        else:
            input_folder = str(ROOT / "runs" / "no-paste-selected")
    if uploaded:
        digest = hashlib.sha256(b"".join(f.name.encode() + f.getvalue() for f in uploaded)).hexdigest()[:12]
        upload_folder = ROOT / "runs" / "uploads" / digest
        upload_folder.mkdir(parents=True, exist_ok=True)
        for file in uploaded:
            (upload_folder / Path(file.name).name).write_bytes(file.getvalue())
        input_folder = str(upload_folder)
        st.caption(f"Uploaded inputs stored locally in {upload_folder.relative_to(ROOT)}")
    try:
        available, input_errors = load_folder(Path(input_folder))
        st.caption(f"{len(available)} episodes parsed · {len(input_errors)} parse failures")
        if input_errors:
            st.json(input_errors)
    except (ValueError, OSError) as exc:
        available = []
        st.warning(str(exc))
    selector_model = st.text_input("Selection model", value=os.getenv("SELECTOR_MODEL", "gpt-6-luna"))
    judge_model = st.text_input("Judge model", value=os.getenv("JUDGE_MODEL", "gpt-6.1-sol"))
    numbers = [e.number for e in available]
    preferred = [n for n in [3, 6, 12, 23, 45, 50] if n in numbers]
    chosen_numbers = st.multiselect("Episodes to process", numbers, default=preferred or numbers[:3])
    max_candidates = st.number_input("Maximum candidates per episode", min_value=1, max_value=6, value=3)
    output_folder = st.text_input("Output folder", value=str(ROOT / "runs" / "new-run"))
    has_key = bool(os.getenv("OPENAI_API_KEY"))
    if not has_key:
        st.warning("Live runs need OPENAI_API_KEY in the project's local .env file or environment. Do not paste it into chat.")
        st.button("Recheck API configuration")
    if st.button("Select and judge selected episodes", type="primary", disabled=not has_key or not chosen_numbers):
        status = st.empty()
        try:
            output = Path(output_folder)
            provider = OpenAIProvider(output / "raw", os.environ["OPENAI_API_KEY"])
            run_pipeline(folder=Path(input_folder), output=output, provider=provider,
                         rubric=(ROOT / "criteria.md").read_text(encoding="utf-8"),
                         selector_model=selector_model, judge_model=judge_model,
                         episode_numbers=set(chosen_numbers), max_candidates=int(max_candidates),
                         progress=lambda message: status.info(message))
            export_report(output)
            st.success(f"Run saved to {output}. Select it in the sidebar to review.")
        except Exception as exc:
            st.error(str(exc))
