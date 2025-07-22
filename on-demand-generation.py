# import neded data
import os , ast
from groq import Groq
from termcolor import colored
from dotenv import load_dotenv
load_dotenv()
# vars 
intro = "-> ai-scriptor $"
# needed instructions
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
def generateScript(idea,desc,language,filename) :
    script = request_response(f"Write a {language} script with the following description : {idea}, which represents: {desc}. Output code only — no explanations, no extra text, and no comments.")
    with open(f"./generated/{filename}",mode="w") as file :
        file.write(script.replace('\n','',1)[3+len(language):-3])
        print(colored(f"{intro} done ...","blue"))
# interact interface with user
print(colored("""
┌─┐┬   ┌─┐┌─┐┬─┐┬┌─┐┌┬┐┌─┐┬─┐
├─┤│───└─┐│  ├┬┘│├─┘ │ │ │├┬┘
┴ ┴┴   └─┘└─┘┴└─┴┴   ┴ └─┘┴└─
""","red"))
generateScript(
    input( colored(f"{intro} Idea you want generate : ","green")),
    input( colored(f"{intro} Give description : ","green")),
    input( colored(f"{intro} Select language : ","green")),
    input( colored(f"{intro} choose filenmae (with extension) : ","green"))
               )