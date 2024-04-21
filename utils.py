from langchain_openai import ChatOpenAI
from langchain_together import Together
from dotenv import load_dotenv
import json
import requests
import os
from prompts import CHARACTER_DESCRIPTION_PROMPT

CONTEXT = CHARACTER_DESCRIPTION_PROMPT.format(
    scenario="Adrien and Vincent work at the office and want to start a new product, and they create it in one night before presenting it to the board."
)

models_dict = {
    "OpenAI": "gpt-3.5-turbo",
    "Mistral": "Mistral-7B-Instruct-v0.2",
    "meta-llama": "Llama-3-8b-chat-hf",
    "Gemma": "gemma-7b-it"
}

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
            temperature=0.7,
            max_tokens=512,
            top_k=50,
            top_p=0.7,
            repetition_penalty=1.0,
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


def invoke_llm(llm, prompt, stop=None):
    return llm.invoke(prompt, stop=stop)


def invoke_llm_api(model_id="meta-llama/llama-3-8b-chat-hf", prompt=None):
    load_dotenv()
    together_key = os.getenv("TOGETHER_API_KEY")
    url = "https://api.together.xyz/v1/chat/completions"

    payload = json.dumps({
        "model": model_id,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1000
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {together_key}'
    }
    response = requests.post(url, headers=headers, data=payload)
    response = response.json()
    try:
        response = response.get("choices")[0].get("message").get("content")
    except Exception as e:
        print(e)
        print(response)
        response = "Error"

    return response


#
# Test

# llm = load_llm_model("OpenAI", "gpt-3.5-turbo")
# print(llm.invoke("Hello, how are you?"))
#
# llm = load_llm_model("Mistral", "Mistral-7B-Instruct-v0.2")
# print(llm.invoke("What is the capital of France?", stop=["<|eot_id|>"]))

# llm = load_llm_model("meta-llama", "Llama-3-8b-chat-hf")
# response = invoke_llm(llm,CHARACTER_DESCRIPTION_PROMPT.format(
#     scenario="Adrien and Vincent work at the office and want to start a new product, and they create it in one night before presenting it to the board."
# ), stop=["<|eot_id|>"])
# print(response)

# llm = load_llm_model("Gemma", "gemma-7b-it")

# print(llm)
# print(llm.invoke("Hellooo"))

CONTEXT = CHARACTER_DESCRIPTION_PROMPT.format(
    scenario="Adrien and Vincent work at the office and want to start a new product, and they create it in one night before presenting it to the board."
)

print("\n\nLlama")
response = invoke_llm_api("meta-llama/Llama-3-8b-chat-hf", CONTEXT)
print(response)

print("\n\nGemma")

response = invoke_llm_api("google/gemma-7b-it", CONTEXT)
print(response)

print("\n\nMistral")

response = invoke_llm_api("mistralai/Mistral-7B-Instruct-v0.2", CONTEXT)
print(response)
