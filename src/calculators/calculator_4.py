from flask import request as FlaskRequest 
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError



class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validade_body(body)
        total_sum = self.__calculate_sum(input_data)
        total_size = self.__calculate_list_size(input_data)        
        average = self.__calculate_average(total_sum, total_size)
        formated_response = self.__format_response(average)
        return formated_response

    def __validade_body(self, body: Dict) -> List[float]:
            if "numbers" not in body:
                raise HttpUnprocessableEntityError("body mal formatado")            
            input_data = body["numbers"]
            return input_data     
      
     
    def __calculate_sum(self, input_data: List[float]) -> float:
         adder = 0
         for num in input_data: adder += num
         return adder 
    
    def __calculate_list_size(self, input_data: List[float]) -> int:
         size = len(input_data)
         return size
    
    def __calculate_average(self, adder: float, size: int) -> float:
         average = adder / size
         return average
         
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": average,
                "Sucess": True
            }
        }