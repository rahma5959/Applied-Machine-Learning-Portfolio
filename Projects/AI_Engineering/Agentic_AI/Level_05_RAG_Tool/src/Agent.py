
from tools.calculator import calculate
from tools.api_tool import get_country_info
from tools.rag_tool import retrieve_context

from services.llm_service import generate

from langgraph.graph import StateGraph, START, END

import re


# --------------------------------------------------
# 1. Analyze the question
# --------------------------------------------------

def analyze_question(state):
    message = state["message"]

    if re.search(r"\d+\s*[\+\-\*\/]\s*\d+", message):
        action = "calculator"

    elif "capital" in message.lower() or "country" in message.lower():
        action = "api"

    elif any(
        keyword in message.lower()
        for keyword in [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "natural language processing",
            "computer vision"
        ]
    ):
        action = "rag"

    else:
        action = "llm"

    return {
        "message": message,
        "action": action
    }


# --------------------------------------------------
# 2. Route the question
# --------------------------------------------------

def route_question(state):
    if state["action"] == "calculator":
        return "calculator"

    elif state["action"] == "api":
        return "api"

    elif state["action"] == "rag":
        return "rag"

    return "llm"


# --------------------------------------------------
# 3. Calculator
# --------------------------------------------------

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


# --------------------------------------------------
# 4. API
# --------------------------------------------------

def use_api(state):
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


# --------------------------------------------------
# 5. RAG
# --------------------------------------------------

def use_rag(state):
    context = retrieve_context.invoke({
        "question": state["message"]
    })

    return {
        "message": state["message"],
        "action": state["action"],
        "context": context
    }


# --------------------------------------------------
# 6. LLM
# --------------------------------------------------

def use_llm(state):
    response = generate(
        state["message"]
    )

    return {
        "message": state["message"],
        "action": state["action"],
        "response": response
    }


# --------------------------------------------------
# 7. Build the LangGraph
# --------------------------------------------------

builder = StateGraph(dict)

builder.add_node(
    "analyze_question",
    analyze_question
)

builder.add_node(
    "extract_numbers",
    extract_numbers
)

builder.add_node(
    "use_calculator",
    use_calculator
)

builder.add_node(
    "use_api",
    use_api
)

builder.add_node(
    "use_rag",
    use_rag
)

builder.add_node(
    "use_llm",
    use_llm
)


# Start
builder.add_edge(
    START,
    "analyze_question"
)


# Routing
builder.add_conditional_edges(
    "analyze_question",
    route_question,
    {
        "calculator": "extract_numbers",
        "api": "use_api",
        "rag": "use_rag",
        "llm": "use_llm"
    }
)


# Calculator
builder.add_edge(
    "extract_numbers",
    "use_calculator"
)

builder.add_edge(
    "use_calculator",
    END
)


# API
builder.add_edge(
    "use_api",
    END
)


# RAG
builder.add_edge(
    "use_rag",
    END
)


# LLM
builder.add_edge(
    "use_llm",
    END
)


# Compile
graph = builder.compile()


# --------------------------------------------------
# 8. Test
# --------------------------------------------------

result = graph.invoke({
    "message": "What is machine learning?"
})

print(result)

