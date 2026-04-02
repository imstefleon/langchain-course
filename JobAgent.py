from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool

load_dotenv()

search = TavilySearch()

@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information."""
    return str(search.invoke({"query": query}))

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

agent = initialize_agent(
    tools=[web_search],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

result = agent.invoke(
    "Search for 3 job postings for an AI engineer using LangChain in the Bay Area and list their details."
)

print(result)