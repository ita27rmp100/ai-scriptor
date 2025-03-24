import os , json , requests
api_key = ""
def get_deepseek_response(user_message, max_tokens=4096, temperature=0.7):
    # Replace with your actual API key
    API_KEY = ""
    API_URL = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"
    except KeyError:
        return "Error: Unexpected response format from API"
    except json.JSONDecodeError:
        return "Error: Could not decode API response"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
def nameScript(idea) :
    return f"{''.join(word[0] for word in idea.split())}.py"
idea = get_deepseek_response("generate a script idea with python (just the idea title)")
script = get_deepseek_response(f"Write Python script for : {idea}")
with open(nameScript(idea),mode="w") as file :
    file.write(script)
os.system(f"git commit -m 'create : {nameScript(idea)}'")
os.system("git push")