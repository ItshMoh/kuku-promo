"""Responses API adapter with schema-constrained output and immutable raw attempts."""
import hashlib
import json
import time
import uuid
from pathlib import Path
from typing import TypeVar

from openai import OpenAI
from pydantic import BaseModel

from .storage import read_json, write_json

T = TypeVar("T", bound=BaseModel)


class ModelCallError(RuntimeError):
    pass


class OpenAIProvider:
    def __init__(self, raw_dir: Path, api_key: str, max_output_tokens: int = 16000):
        if not api_key:
            raise ValueError("Set OPENAI_API_KEY in the environment or a local .env file before live runs")
        self.raw_dir = raw_dir
        self.client = OpenAI(api_key=api_key, timeout=180, max_retries=2)
        self.max_output_tokens = max_output_tokens

    def call(self, *, stage: str, model: str, system: str, payload: dict, schema: type[T]) -> T:
        request = {
            "model": model, "instructions": system,
            "input": json.dumps(payload, ensure_ascii=False), "store": False,
            "reasoning": {"effort": "medium"}, "max_output_tokens": self.max_output_tokens,
            "text": {"format": {"type": "json_schema", "name": schema.__name__,
                                "strict": True, "schema": schema.model_json_schema()}},
        }
        digest = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
        directory = self.raw_dir / f"{stage}-{digest[:20]}"
        cache = directory / "parsed.json"
        if cache.exists():
            return schema.model_validate(read_json(cache))
        directory.mkdir(parents=True, exist_ok=True)
        write_json(directory / "request.json", request)
        attempt = uuid.uuid4().hex[:12]
        started = time.monotonic()
        try:
            response = self.client.responses.create(**request)
        except Exception as exc:
            # Do not serialize SDK exception bodies: authentication errors can contain key fragments.
            write_json(directory / f"{attempt}.error.json", {"error_type": type(exc).__name__,
                       "elapsed_seconds": round(time.monotonic() - started, 3)})
            raise ModelCallError(f"{stage}: {type(exc).__name__}; check API access/network and resume") from None
        # Preserve the complete SDK response before parsing, including refusals/incomplete outputs.
        (directory / f"{attempt}.response.json").write_text(response.model_dump_json(indent=2), encoding="utf-8")
        write_json(directory / f"{attempt}.timing.json", {"elapsed_seconds": round(time.monotonic() - started, 3)})
        if response.status != "completed" or not response.output_text:
            raise ModelCallError(f"{stage}: incomplete or refused response; original response saved")
        try:
            parsed = schema.model_validate_json(response.output_text)
        except ValueError:
            raise ModelCallError(f"{stage}: response failed schema validation; original response saved") from None
        write_json(cache, parsed.model_dump())
        return parsed


def usage_summary(raw_dir: Path) -> dict:
    totals = {"calls": 0, "input_tokens": 0, "output_tokens": 0, "cached_input_tokens": 0, "by_model": {}}
    for path in raw_dir.glob("*/*.response.json"):
        response = read_json(path)
        usage = response.get("usage") or {}
        model = response.get("model", "unknown")
        row = totals["by_model"].setdefault(model, {"calls": 0, "input_tokens": 0, "output_tokens": 0,
                                                  "cached_input_tokens": 0})
        values = {"calls": 1, "input_tokens": usage.get("input_tokens", 0),
                  "output_tokens": usage.get("output_tokens", 0),
                  "cached_input_tokens": (usage.get("input_tokens_details") or {}).get("cached_tokens", 0)}
        for key, value in values.items():
            totals[key] += value
            row[key] += value
    return totals
