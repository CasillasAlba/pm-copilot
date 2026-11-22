import sys
from pathlib import Path

import ollama

sys.path.insert(0, str(Path(__file__).resolve().parent / "pm-copilot"))
from config import MODEL, SEED, SYSTEM_PROMPT, TEMPERATURE

question = input("Enter your question: ")
response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ],
    options={"temperature": TEMPERATURE, "seed": SEED},
)
print(response.message.content)
print("\nTokens evaluated in the prompt: " + str(response.prompt_eval_count))
print("\nTokens evaluated in the response: " + str(response.eval_count))

