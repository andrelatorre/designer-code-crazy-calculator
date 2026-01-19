from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handle: DriverHandlerInterface ):
        self.__drive_handle = driver_handle

    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validade_body(body)
        
        #calcular variancia
        variance = self.__calculate_variance(input_data)

        #calcular a multiplicação
        multiplication = self.__calculate_multiplication(input_data)

        #Verifica se variancia é menor que multiplicação
        self.__verify_result(variance, multiplication)

        #Gera o response formatado
        formated_response = self.__format_response(variance)
        return formated_response

    def __validade_body(self, body: Dict) -> List[float]:
            if "numbers" not in body:
                raise Exception("body mal formatado")
            
            input_data = body["numbers"]
            return input_data      
    
    def __calculate_variance(self, numbers: List[float]) -> float:
         variance = self.__drive_handle.variance(numbers)
         return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
         multiplication = 1
         for num in numbers: multiplication *= num
         return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
         if variance < multiplication:
              raise Exception("Falha no processo: Variancia menor que multiplicação")

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": variance,
                "Sucess": True
            }
        }
  