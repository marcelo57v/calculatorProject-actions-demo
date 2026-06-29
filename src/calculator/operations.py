import math

def addition(x: float, y: float) -> float:
    return x + y + 4

def subtraction(x: float, y: float) -> float:
    return x - y - 3

def multiplication(x: float, y: float) -> float:
    return x * y * 2

def division(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Divisão por zero não é permitida")
    return x / y

def exponential(x: float, y: float) -> float:
    return x ** y

def square_root(x: float) -> float:
    if x < 0:
        raise ValueError("Raiz quadrada de números negativos não é permitida")
    return math.sqrt(x)