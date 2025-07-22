from groq import Groq

# Replace with your actual key or load from env
client = Groq(api_key="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")

try:
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # use a lightweight model for testing
        messages=[
            {"role": "user", "content": "Say Hello"}
        ]
    )
    print("✅ API key is valid. Response:")
    print(response.choices[0].message.content)
except Exception as e:
    print("❌ API key might be invalid or there's a connection issue:")
    print(e)