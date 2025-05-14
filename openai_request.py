from openai import OpenAI
import user_config

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=user_config.openai_key)

def send_request(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."

def send_request2(query):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=query
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."
