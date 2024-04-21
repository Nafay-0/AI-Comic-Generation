from langchain_openai import ChatOpenAI
from langchain_together import Together
from dotenv import load_dotenv
import os


def load_llm_model(name="OpenAI", model_id="gpt-3.5-turbo"):
    load_dotenv()
    llm = None
    if name == "OpenAI":
        llm = ChatOpenAI(model_name=model_id, temperature=0.2)

    elif name == "Mistral":
        llm = Together(
            model=f'mistralai/{model_id}',
            temperature=0.2,
            max_tokens=20,
            top_k=1,
            together_api_key=os.getenv("TOGETHER_API_KEY"),
        )
    elif name == 'meta-llama':
        llm = Together(
            model=f'meta-llama/{model_id}',
            temperature=0.2,
            max_tokens=512,
            top_k=1,
            together_api_key=os.getenv("TOGETHER_API_KEY"),
        )
    elif name == 'Gemma':
        llm = Together(
            model=f'google/{model_id}',
            temperature=0.2,
            max_tokens=512,
            top_k=1,
            together_api_key=os.getenv("TOGETHER_API_KEY"),
        )
    else:
        raise ValueError(f"Model {name} not found.")
    if llm is None:
        raise ValueError(f"Model {name} not found.")
    return llm


# Test

llm = load_llm_model("OpenAI", "gpt-3.5-turbo")
print(llm.invoke("Hello, how are you?"))

# llm = load_llm_model("Mistral", "Mistral-7B-Instruct-v0.2")
# print(llm.invoke("What is the capital of France?"))

# llm = load_llm_model("meta-llama", "Llama-3-8b-chat-hf")
# print(llm.invoke(
#     """Answer this question briefly and to the point:
#     What is the capital of France?
#     """
# ))

# llm = load_llm_model("Gemma", "gemma-7b-it")

# print(llm)
# print(llm.invoke("Hellooo"))