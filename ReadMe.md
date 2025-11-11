** THING 1 **
First create a ollama docker container
you can see how to make at dockerhub , offical ollama image
then just download whatever llm you want , i am using llama3:8b

"ollama run llama3:8b"

** THING 2 **
next thing i did was to start exploring langchain, more or less its a framework to make AI Agents.
in "./langchain/01_createAgent.py" there is code for making a simple AI Agent with one tool .
tool are just functions that provide llm functionalities. I saw this code on langchain website.

but instead of using Claude model with API Key , i am using qwen2.5:7b on ollama for now
for that i needed to install :

"pip install -U langchain-ollama" in the .venv

and then wrap my model into ChatOllama() then pass it into create_agent() function.

agent calls the llm with all the info like system prompt , tools list and their description, other things like context , prompt and content written by the user.

there are different roles like system , user , assistant. 