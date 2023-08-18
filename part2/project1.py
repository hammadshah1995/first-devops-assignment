import os
import openai
#openai.organization = "org-vgBTgf6DIcsh5nGvNjuh1spC"
openai.api_key = "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"

#print (openai.api_key)

messages = [
    {"role": "system", "content": "Act like yoda from the series Star Wars"},
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})