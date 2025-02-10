from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from nemoguardrails import RailsConfig
from nemoguardrails.integrations.langchain.runnable_rails import RunnableRails

load_dotenv(override=True)

config = RailsConfig.from_path("./config")
guardrails = RunnableRails(config)


prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

chain_with_guardrails = prompt | (guardrails | model) | output_parser

output = chain_with_guardrails.invoke({"topic": "AI"})
print(output)
