import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

model = "gpt-3.5-turbo"

def invoke_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = model,
        messages=[
            {"role": "user", "content": prompt}
        ]    
    )

    message = response['choices'][0]['message']['content']

    return message

result = invoke_gpt("What is BTC")
print (result)