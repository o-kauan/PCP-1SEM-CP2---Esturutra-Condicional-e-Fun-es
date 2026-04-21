nome = input("Digite seu nome: ")
print("==================================================")
print("1-Gerente\n2-Analista\n3-Assistente\n4-Estagiario")
print("==================================================")
cargo = int(input("INSIRA O NUMERO CORRESPONDENTE\nDigite seu cargo: "))
sal = float(input("Digite o seu salario: "))
extra = int(input("Digite as horas extras trabalhadas: "))
falta = int(input("Digite a quantidade de faltas (Periodo de 1 mes): "))
bonus = input("Recebeu bonus por desempenho? (s / n): ")

def horasextras():
    valextra = sal * 0.015
    return valextra

def descfaltas():
    desc = sal * 0.02
    return desc

def calcbonus():
    if cargo == 1 and bonus == "s":
        bonss = 1000
        bsal = sal + bonss
    elif cargo == 2 and bonus == "s":
        bonss = 500
        bsal = sal + bonss
    elif cargo == 3 and bonus == "s":
        bonss = 300
        bsal = sal + bonss
    elif cargo == 4 and bonus == "s":
        bonss = 100
        bsal = sal + bonss
    elif bonus == "n":
        bonss = 0
    else:
        print("Erro! Tente novamente!")
    return bonss

valextra = horasextras()
desc = descfaltas()
bonss = calcbonus()

btotal = valextra + bonss
salariofinal = sal + btotal - desc
print("=============================================")
print(f"salario bruto: R${sal}")
print(f"Valor da hora extra + bonus: R${btotal}")
print(f"Total de descontos: -R${desc}")
print(f"Salario final: R${salariofinal}")
print("=============================================")
