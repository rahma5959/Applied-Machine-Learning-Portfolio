from langgraph.graph import StateGraph, START, END

from services.llm_service import generate_response


def analyse_message(state):
    message = state["message"]

    return {
        "message": message,
        "status": "Message analyzed"
    }


def generate_message(state):
    message = state["message"]

    response = generate_response(message)

    return {
        "message": message,
        "response": response,
        "status": state["status"]
    }


builder = StateGraph(dict)

builder.add_node("analyse_message", analyse_message)
builder.add_node("generate_message", generate_message)

builder.add_edge(START, "analyse_message")
builder.add_edge("analyse_message", "generate_message")
builder.add_edge("generate_message", END)

graph = builder.compile()


result = graph.invoke({
    "message": "What is artificial intelligence?"
})

print(result)

