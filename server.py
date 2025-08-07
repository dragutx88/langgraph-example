from fastapi import FastAPI
from langgraph.prebuilt import create_react_agent       # ← Burayı değiştirdik!
from langserve import add_routes
from my_agent import agent, tools                       # kendi agent tanımın

app = FastAPI()

# create_react_agent, hazır bir ReAct-style ajan döndürür.
executor = create_react_agent(
    model="anthropic:claude-3-0",   # veya OpenAI vs. provider
    tools=tools,
    prompt="You are a helpful assistant."
)

# FastAPI içine /chat rotası olarak ekle
add_routes(app, executor, path="/chat")
