# Getting the host running Ollama
import os
ollama_host = os.environ["OLLAMA_HOST"] or "localhost"
base_url = f"http://{ollama_host}:11434"

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

# 1. Setup the FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


# 2. Setup the LLM call
prompt = ChatPromptTemplate.from_template("write a tweet {topic}")
add_routes(
    app,
    prompt | Ollama(model="phi3", base_url=base_url),
    path="/tweet-phi3",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
