from langchain_core.tools import tool


@tool
def calculate(a:int,b:int) -> int:
    """Add two numbers."""
    return a+b

print(calculate.invoke({"a": 4, "b": 2}))