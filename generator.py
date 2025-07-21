import os , ast
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
def request_response(prompt, max_tokens=4096, temperature=0.7):
    client = Groq(
        api_key=os.getenv('groq_api'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    return chat_completion.choices[0].message.content
def nameScript(idea) :
    return f"{''.join(word[0] for word in idea.split())}.py"
idea = ast.literal_eval(request_response("Gimme python idea script (only one idea without giving the code, The answer will be as an array like : ['<ideaname>','<description>','<IdeaNameFileName>.py']"))
script = request_response(f"Write a Python script for: {idea[0]}, which represents: {idea[1]}. Output code only — no explanations, no extra text, and no comments.")
with open('python/'+idea[2],mode="w") as file :
    file.write(script.replace('\n','',1)[9:-3])
    print(f"{idea[0]} : done")
    os.system(f"git commit -m 'create : {nameScript(idea)}'")
    os.system("git push")