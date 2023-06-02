from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes miniature figures for tabletop games?"

print(llm(text))