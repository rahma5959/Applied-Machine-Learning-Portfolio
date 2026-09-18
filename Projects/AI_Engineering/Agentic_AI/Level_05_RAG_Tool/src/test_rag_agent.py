from langgraph.graph import StateGraph, START, END

from tools.rag_tool import retrieve_context


def use_rag(state):

    context = retrieve_context.invoke({
        "question": state["message"]
    })

    return {
        "message": state["message"],
        "context": context
    }


builder = StateGraph(dict)

builder.add_node("use_rag", use_rag)

builder.add_edge(START, "use_rag")
builder.add_edge("use_rag", END)

graph = builder.compile()


result = graph.invoke({
    "message": "What is machine learning?"
})

print(result)

