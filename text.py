from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv(override=True)

llm=ChatGroq(model="openai/gpt-oss-120b")

print("My first Chatbot")
history=[]
while True:

    prompt=input("user:")
    history.append(prompt)
    if prompt=="exit":
        break

    response=llm.invoke(history)
    history.append(response)
    print(response.content)

print(history)