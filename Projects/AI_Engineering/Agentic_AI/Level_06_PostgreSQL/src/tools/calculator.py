from langchain_core.tools import tool 

@tool
def calculate(a:int,b:int) -> int:
    """
    Calculate the sum of two numbers.
    """
    return a + b