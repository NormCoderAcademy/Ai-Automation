import os
import openai
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
api_key = os.getenv("CHAT_GPT_API_KEY")
openai.api_key = api_key

def automated_task(prompt):
    try:
        # Create a chat completion request
        chat_completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract the AI-generated response
        response = chat_completion.choices[0].message["content"]
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
user_prompt = "Tell me a joke!"
generated_response = automated_task(user_prompt)
print(f"Generated response: {generated_response}")
