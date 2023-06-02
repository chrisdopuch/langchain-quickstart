from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

chat = ChatOpenAI(temperature=0, verbose=True)

batch_messages = [
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to Croatian."
        ),
        HumanMessage(content="I love programming."),
    ],
    [
        SystemMessage(
            content="You are a helpful assistant that translates English to Croatian."
        ),
        HumanMessage(content="I love artificial intelligence."),
    ],
]
result = chat.generate(batch_messages)
print(result)
print(result.llm_output["token_usage"])
