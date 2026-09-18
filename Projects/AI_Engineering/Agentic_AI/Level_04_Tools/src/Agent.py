
from tools.calculator import calculate
from tools.api_tool import get_country_info
from langgraph.graph import StateGraph, START, END
from services.llm_service import generate_response
import re


# Decide which tool should be used
def analyze_question(state):
    message = state["message"]

    # Arithmetic question
    if re.search(r"\d+\s*[\+\-\*\/]\s*\d+", message):
        action = "calculator"

    # Country / capital question
    elif "capital" in message.lower() or "country" in message.lower():
        action = "api"

    # General question
    else:
        action = "llm"

    return {
        "message": message,
        "action": action
    }


# Extract numbers for the calculator
def extract_numbers(state):
    message = state["message"]

    numbers = re.findall(r"\d+", message)

    a = int(numbers[0])
    b = int(numbers[1])

    return {
        "message": message,
        "action": state["action"],
        "a": a,
        "b": b
    }


# Use Calculator Tool
def use_calculator(state):
    result = calculate.invoke({
        "a": state["a"],
        "b": state["b"]
    })

    return {
        "message": state["message"],
        "action": state["action"],
        "a": state["a"],
        "b": state["b"],
        "result": result
    }


# Use API Tool
def use_api(state):
    # Extract country name from the question
    message = state["message"]

    country_match = re.search(
        r"(?:capital of|country)\s+([A-Za-z]+)",
        message,
        re.IGNORECASE
    )

    if country_match:
        country = country_match.group(1)
    else:
        country = "France"

    result = get_country_info.invoke({
        "country": country
    })

    return {
        "message": message,
        "action": state["action"],
        "country": country,
        "api_result": result
    }


# Use LLM
def use_llm(state):
    response = generate_response(
        state["message"]
    )

    return {
        "message": state["message"],
        "action": state["action"],
        "response": response
    }


# Decide where to route the question
def route_question(state):
    if state["action"] == "calculator":
        return "calculator"

    elif state["action"] == "api":
        return "api"

    return "llm"


# Build LangGraph
builder = StateGraph(dict)

builder.add_node("analyze_question", analyze_question)
builder.add_node("extract_numbers", extract_numbers)
builder.add_node("use_calculator", use_calculator)
builder.add_node("use_api", use_api)
builder.add_node("use_llm", use_llm)

builder.add_edge(START, "analyze_question")

builder.add_conditional_edges(
    "analyze_question",
    route_question,
    {
        "calculator": "extract_numbers",
        "api": "use_api",
        "llm": "use_llm"
    }
)

builder.add_edge("extract_numbers", "use_calculator")
builder.add_edge("use_calculator", END)

builder.add_edge("use_api", END)

builder.add_edge("use_llm", END)

graph = builder.compile()


# Test
result = graph.invoke({
    "message": "What is the capital of France?"
})

print(result)

