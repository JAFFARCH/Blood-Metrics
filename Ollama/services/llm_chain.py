from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from config.prompt_template import prompt_template

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | model
