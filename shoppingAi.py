from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

MAX_ITERATIONS = 10
MODEL = "qwen3.5:0.8b"


@tool
def get_product_price(product: str) -> float:
    """Look up the price of a product in the catalog."""
    print(f"    >> Executing get_product_price(product={product!r})")
    prices = {
        "laptop": 1299.99,
        "headphones": 149.95,
        "keyboard": 89.50,
    }
    return prices.get(product.lower(), 0.0)


@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Apply a discount tier to a price and return the final price.
    Available tiers: bronze, silver, gold.
    """
    print(f"    >> Executing apply_discount(price={price}, discount_tier={discount_tier!r})")

    
    discount_percentages = {
        "bronze": 0.05,
        "silver": 0.12,
        "gold": 0.23,
    }

    tier = discount_tier.lower().strip()
    discount = discount_percentages.get(tier, 0.0)
    return round(price * (1 - discount), 2)


def run_agent(question: str):
    tools = [get_product_price, apply_discount]
    tools_dict = {t.name: t for t in tools}

   llm = init_chat_model(f"ollama:{MODEL}",temperature=0)
    
    #llm = init_chat_model(f"openai:gpt-4.1-mini", temperature=0)
    
    llm_with_tools = llm.bind_tools(tools)

    print(f"Question: {question}")
    print("=" * 60)

    messages = [
        SystemMessage(
            content=(
                "You are a helpful shopping assistant.\n"
                "Rules:\n"
                "1. Never guess a product price. Always call get_product_price first.\n"
                "2. Only call apply_discount after you have a real price.\n"
                "3. Never do discount math yourself; always use apply_discount.\n"
                "4. If the user does not specify a discount tier, ask for it.\n"
                "5. When you are done, answer clearly in one sentence."
            )
        ),
        HumanMessage(content=question),
    ]

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"\n--- Iteration {iteration} ---")

        ai_message = llm_with_tools.invoke(messages)
        messages.append(ai_message)

        tool_calls = getattr(ai_message, "tool_calls", None) or []

        if not tool_calls:
            print(f"\nFinal Answer: {ai_message.content}")
            return ai_message.content

        for tool_call in tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call.get("args", {})
            tool_call_id = tool_call["id"]

            print(f"  [Tool Selected] {tool_name} with args: {tool_args}")

            tool_to_use = tools_dict.get(tool_name)
            if tool_to_use is None:
                raise ValueError(f"Tool {tool_name!r} not found")

            observation = tool_to_use.invoke(tool_args)
            print(f"  [Tool Result] {observation}")

            messages.append(
                ToolMessage(
                    content=str(observation),
                    tool_call_id=tool_call_id,
                )
            )

    raise RuntimeError("Max iterations reached without a final answer")


if __name__ == "__main__":
    print("Hello LangChain Agent (.bind_tools)!")
    result = run_agent(
        "What is the price of a laptop after applying a gold discount?"
    )
    print("\nReturned:", result)