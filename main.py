import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from calculator.operations import (
    addition,
    subtraction,
    multiplication,
    division,
    exponential,
    square_root
)

from calculator.memory import Memory

def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Digite um número válido, por favor. (ex: 2 ou 3.5, ou 100)")

def run_operations(memory: Memory) -> None:
    print("\nOperações disponíveis: \n+ (soma) \n- (subtração) \n/ (divisão) \n* (multiplicação) \n^ (exponencial) \nv (raiz quadrada)")
    operation = input("Digite a operação que deseja fazer:  ").strip()

    try:
        if operation == "v":
            x = read_number("Qual o valor do radicando? ")
            result = square_root(x)
        elif operation in ("+", "-", "*", "/"):
            x = read_number("Qual o valor de x? ")
            y = read_number("Qual o valor de y? ")
            if operation == "+":
                result = addition(x, y)
            elif operation == "-":
                result = subtraction(x, y)
            elif operation == "*":
                result = multiplication(x, y)
            elif operation == "/":
                result = division(x, y)
        elif operation in ("^"):
            x = read_number(" Qual o valor da base? ")
            y = read_number(" Qual o valor do expoente? ")
            result = exponential(x, y)
        else:
            print(f"Operação Desconhecida: {operation!r}")
            return
    except ValueError as error:
        print(f"  Erro: {error}")
        return

    print(f"Resultado: {result}")
    if input("Deseja salvar o valor na memória? (s/n): ").strip().lower() == "s":
        entry_id = memory.create(result)
        print(f"  Salvo com o id: {entry_id}.")


def run_memory(memory: Memory) -> None:
    print("\nMemória:  (L)eitura  (V)er todos  (A)tualizar  (D)eletar")
    action = input("Escolha o que deseja fazer: ").strip().lower()
    try:
        if action == "v":
            entries = memory.list_all()
            if not entries:
                print("A memória está vazia.")
            for entry_id, value in entries.items():
                print(f"  [{entry_id}] {value}")
        elif action == "l":
            entry_id = int(input("Qual o id da operação que você deseja ver? "))
            print(f"Resultado: {memory.read(entry_id)}")
        elif action == "a":
            entry_id = int(input("Qual o id da operação que você deseja atualizar? "))
            value = read_number("Qual o novo valor? ")
            memory.update(entry_id, value)
            print("Atualizado")
        elif action == "d":
            entry_id = int(input("Qual o id da operação que você deseja deletar? "))
            memory.delete(entry_id)
            print("Deletado")
        else:
            print(f"Ação Desconhecida: {action!r}")
    except ValueError as error:
        print(f"Erro: {error}")


def main() -> None:
    memory = Memory()
    print("=== Calculadora Básica ===")
    while True:
        print("\nMenu:  (C)alcular  (M)emória  (S)air")
        choice = input("Escolha o que deseja fazer: ").strip().lower()
        if choice == "c":
            run_operations(memory)
        elif choice == "m":
            run_memory(memory)
        elif choice == "s":
            print("Bye!")
            break
        else:
            print(f"Escolha Desconhecida: {choice!r}")


if __name__ == "__main__":
    main()