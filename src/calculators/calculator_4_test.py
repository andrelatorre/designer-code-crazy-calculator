from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 1, 51, 1,2]})

    calculator_4 = Calculator4()
    response = calculator_4.calculate(mock_request)

    assert response == {'data': {'Calculator': 4, 'result': 11.2, 'Sucess': True}}
    assert response["data"]["result"] == 11.2
    assert response["data"]["Sucess"] == True