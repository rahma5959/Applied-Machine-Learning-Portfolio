
import sys
import os
from tracemalloc import start

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.calculator import calculate
from tools.database_tool import get_document
from langgraph.graph import StateGraph,START,END

import re

def analyze_question(state):
    message = state["message"]

    if re.search(r"\d+\s*[\+\-\*\/]\s*\d+", message):
        action = "calculator"
    else:
        action = "database"

    return {
        "message": message,
        "action": action
    }

def route_question(state):
    if state["action"]=="calculator":
        return "calculator"
    else:
        return "database"
    
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

def use_calculate(state):
    result=calculate.invoke({
        "a":state["a"],
        "b":state["b"]
    })
    
    return {
        "message": state["message"],
        "action": state["action"],
        "a": state["a"],
        "b": state["b"],
        "result": result
    }

def use_database(state):
    document=get_document.invoke({})
    return{
        "message":state["message"],
        "action":state["action"],
        "document":document
    }

builder=StateGraph(dict)

builder.add_node("analyze_question", analyze_question)
builder.add_node("extract_numbers", extract_numbers)
builder.add_node("use_calculate", use_calculate)
builder.add_node("use_database", use_database)
        
builder.add_edge(START,"analyze_question")

builder.add_conditional_edges(
    "analyze_question",
    route_question,
    {
        "calculator": "extract_numbers",
        "database": "use_database"
    }
)

builder.add_edge("extract_numbers", "use_calculate")
builder.add_edge("use_database", END)

graph = builder.compile()

result = graph.invoke({
    "message": "What documents are stored in the database?"
})

print(result)

