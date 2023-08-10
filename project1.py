import os
import openai
#openai.organization = "org-vgBTgf6DIcsh5nGvNjuh1spC"
openai.api_key = "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"

#print (openai.api_key)

messages = [
    {"role": "system", "content": "You are an assistent English Poet who replies in poetry"},
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