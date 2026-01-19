from src.calculators.calculatore_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    numpy_handle = NumpyHandler()
    calc = Calculator2(numpy_handle)
    return calc