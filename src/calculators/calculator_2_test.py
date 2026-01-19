from .calculatore_2 import Calculator2
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():    
    mock_request = MockRequest(body={"numbers": [1,2,3]})


    calculator_2 = Calculator2()
    calculator_2.calculate(mock_request)
    format_response = calculator_2.calculate(mock_request)


    assert isinstance(format_response, dict)
    assert format_response == {'data': {'Calculator': 2, 'result': 0.14}}