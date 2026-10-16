from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv(override=True)


llm=ChatGroq(model="openai/gpt-oss-120b",
                temperature=0.6,
                max_tokens=300)

prompt_template=PromptTemplate.from_template(
        """Analyse the {topic} and give me a structured 3 lines theory about it , dont guess it ,
        answer should be in one paragraph and simple points """
)

prompt=prompt_template.invoke(
    {"topic" : input("user topic: ")}
    )
response=llm.invoke(prompt)
print(response.content) 