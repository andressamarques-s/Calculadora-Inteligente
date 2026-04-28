
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


print("=== Calculadora Inteligente ===")

historico = []

while True:
    try:
        number = float(input("Digite um número: "))
        operacao = input("Digite a operação (+, -, *, /) ou 'sair': ")

        if operacao.lower() == "sair":
            break

        number2 = float(input("Digite outro número: "))

        if operacao == '+':
            resultado = soma(number, number2)
        elif operacao == '-':
            resultado = subtracao(number, number2)
        elif operacao == '*':
            resultado = multiplicacao(number, number2)
        elif operacao == '/':
            resultado = divisao(number, number2)
        else:
            print("Operação inválida")
            continue

        print("Resultado:", resultado)

        conta = f"{number} {operacao} {number2} = {resultado}"
        historico.append(conta)

    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except ValueError:
        print("Digite apenas números válidos")

print("\n=== Histórico ===")
for item in historico:
    print(item)
