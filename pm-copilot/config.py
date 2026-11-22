from pathlib import Path

MODEL = "llama3.1:8b"
TEMPERATURE = 0.3
SEED = 42
SYSTEM_PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "system.md"
).read_text(encoding="utf-8").strip()