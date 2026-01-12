from pathlib import Path

PROMPT_DIR = Path(__file__).resolve().parents[2] / "prompts"

def load_prompt(name: str) -> str:
    path = PROMPT_DIR / f"{name}.txt"
    return path.read_text()
