from groq import Groq

client = Groq(api_key="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")
print("Chatbot ready! 'quit' likho band karne ke liye")
print("-" * 40)

while True:
    user_input = input("User: ")
    
    if user_input.lower() == "quit":
        print("Good Bye!")
        break
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    
    print("Bot:", response.choices[0].message.content)
    print("-" * 40)