from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Buraya LangGraph agent executor kodunu da eklemelisin
from langchain_core.prebuilt import create_agent_executor
from langserve import add_routes
from my_agent import agent, tools     # kendi agent tanımın

# create_agent_executor: agent'ını çalıştıran executor
executor = create_agent_executor(agent, tools)

# FastAPI içine /chat rotası olarak ekle
add_routes(app, executor, path="/chat")
