from tools.calculate_tool import calculate

def test_calculate():
    result=calculate.invoke({"a":2,"b":3})
    assert result == 5
