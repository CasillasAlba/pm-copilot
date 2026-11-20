import ollama

MODEL = "llama3.1:8b"

question = input("Enter your question: ")
response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": question}])
print(response.message.content)

