from openai import OpenAI

client = OpenAI(api_key="i6VpZR1WqPOG3GDToKNwi8KB85IDL8TG0QnH", base_url="http://193.104.69.173:8800/v1")

response = client.chat.completions.create(
    model="Qwen/Qwen3-14B-AWQ",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Какое население России?"},
    ],
    stream=False
)

print(response.choices[0].message.content)
