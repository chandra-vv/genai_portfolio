import openai

# Set your API key
client = openai.OpenAI(api_key="your-api-key")

# Send a chat request to GPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "You are a senior data engineer. Explain step-by-step how to build a scalable data pipeline using AWS Glue, S3, and Redshift."}
    ],
    temperature=0.5,
    max_tokens=400
)

# Print the response
print(response.choices[0].message.content)
