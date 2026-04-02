from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch


# -------------------------
# SCHEMAS
# -------------------------
class Source(BaseModel):
    """Schema fora source used by the agent"""
    
    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for a agent response with answer and sources"""
    
    answer: str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list,description="List of sources used to generate a answer")


# -------------------------
# LLM
# -------------------------
llm = ChatOpenAI(
    model="gpt-4.1-mini",  
    temperature=0
)

# -------------------------
# TOOLS
# -------------------------
tools = [TavilySearch()]

# -------------------------
# AGENT (LangChain v1+)
# -------------------------
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse,  
)


# -------------------------
# MAIN
# -------------------------
def main():
    print("Hello from langchain-course!")

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Search for 3 job postings for an AI engineer using LangChain in the Bay Area on LinkedIn and list their details with sources."
                }
            ]
        }
    )

    print(result)


if __name__ == "__main__":
    main()