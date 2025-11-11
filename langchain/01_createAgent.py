from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_weather(city: str)-> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatOllama(model="qwen2.5:7b")

#create agent
agent = create_agent(
    model = model,
    tools = [get_weather],
    system_prompt="""
    you are an helpful assitant. When the user asks a question requiring external info, call the appropriate tool with correct arguments. Do not answer without using the tool if the tool is relevant."""
)

#Run the agent
result = agent.invoke({
    "messages":[
        {
            "role":"user",
            "content":"how is the weather in indore?"
        }
    ]
}
)

print(result["messages"][-1].content)

