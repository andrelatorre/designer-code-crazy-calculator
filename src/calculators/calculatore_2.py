from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validade_body(body)
        calculator_number = self.__process_data(input_data)
        format_response = self.__format_response(calculator_number)
        return format_response

    def __validade_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado")
        
        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        numpy_handle = NumpyHandler()
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = numpy_handle.standard_derivation(first_process_result)
        return 1 / result
    
    def __format_response(self, calculator_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculator_number,2)
            }
        }

