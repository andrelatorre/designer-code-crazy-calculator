from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers):
        return 3
    def variance(self, numbers):
        return 3

#Integração entre NumpyHandler e Calculator2
def test_calculate_integration():    
    mock_request = MockRequest(body={"numbers": [1,2,3]})

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    calculator_2.calculate(mock_request)
    format_response = calculator_2.calculate(mock_request)

    assert isinstance(format_response, dict)
    assert format_response == {'data': {'Calculator': 2, 'result': 0.14}}

def test_calculate():    
    mock_request = MockRequest(body={"numbers": [1,2,3]})

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    calculator_2.calculate(mock_request)
    format_response = calculator_2.calculate(mock_request)

    assert isinstance(format_response, dict)
    assert format_response == {'data': {'Calculator': 2, 'result': 0.33}}    