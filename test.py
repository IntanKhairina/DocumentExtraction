import os
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

api_key = os.getenv("ANTHROPIC_API_KEY")
print(f"API Key loaded: {api_key[:10]}...")

try:
    client = Anthropic(api_key=api_key)
    print("Client initialized successfully")
    
    response = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=50,
        messages=[{"role": "user", "content": "Say hello"}]
    )
    print(f"API works: {response.content[0].text}")
except Exception as e:
    print(f"Error: {e}")