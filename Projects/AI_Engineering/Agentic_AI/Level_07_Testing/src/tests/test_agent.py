from Agent import graph

def test_agent_calculator():
    result=graph.invoke({
        "message":"what is 2+2"
    })
    assert result["action"]=="calculator"
    assert result["result"]==4