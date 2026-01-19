from typing import Dict
from .calculator_1 import Calculator1
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    calculator_1 = Calculator1()
    mock_request = MockRequest(body={"number": 1})
    response = calculator_1.calculate(mock_request)

    #precisamos testar o formato da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    #Assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_body_error():
    calculator_1 = Calculator1()
    mock_request = MockRequest(body={"somethings": 1})

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)
    
    assert str(excinfo.value) == 'Body mal formatado'
