from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv(override=True)


llm=ChatGroq(model="openai/gpt-oss-120b",max_tokens=200)

print("My first Chatbot")

messages=[
    SystemMessage(content="you are funny ai assitant, reply in fun way")
]
    
while True:

    prompt=input("user:")
    messages.append(HumanMessage(content=prompt))
    if prompt=="exit":
        break

    response=llm.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print(response.content)

print(SystemMessage)