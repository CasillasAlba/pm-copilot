import ollama

from .config import MODEL, SYSTEM_PROMPT, TEMPERATURE

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Let's talk about Prebid.js and Prebid Server. What would you like to know? ")
while True:
    user_entry = input(">>> ").strip()
    
    if user_entry.lower() in ["exit", "quit", "bye"]:
            break
    
    messages.append({"role": "user", "content": user_entry})
    
    response = ollama.chat(
        model=MODEL,
        messages=messages,
        options={"temperature": TEMPERATURE},
    )
    
    print(str(response.message.content) + "\n")
    messages.append({"role": "assistant", "content": response.message.content})

    