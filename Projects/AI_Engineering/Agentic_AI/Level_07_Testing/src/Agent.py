from langgraph.graph import StateGraph, START, END
from tools.calculate_tool import calculate


def analyze_question(state):
    message = state["message"]

    if "+" in message:
        return {"action": "calculator"}

    return {"action": "unknown"}


def use_calculator(state):
    result = calculate.invoke({
        "a": 2,
        "b": 2
    })

    return {
        "action": "calculator",
        "result": result
    }


builder = StateGraph(dict)

builder.add_node("analyze_question", analyze_question)
builder.add_node("use_calculator", use_calculator)

builder.add_edge(START, "analyze_question")

builder.add_conditional_edges(
    "analyze_question",
    lambda state: state["action"],
    {
        "calculator": "use_calculator",
        "unknown": END
    }
)

builder.add_edge("use_calculator", END)

graph = builder.compile()