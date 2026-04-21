# Função para verificar aprovação
def pode_aprovar(idade, renda, valor):
    if idade < 18:
        return False
    if valor > renda * 20:
        return False
    return True

# Função para definir taxa de juros
def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

# Função para calcular parcela (Tabela Price)
def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    pmt = valor * (i * (1 + i)**n) / ((1 + i)**n - 1)
    return pmt

# Função para calcular total pago
def calcular_total(parcela, parcelas):
    return parcela * parcelas

# Função para calcular juros pagos
def calcular_juros(total, valor):
    return total - valor

# Programa principal
def main():
    print("=== Sistema de Financiamento ===")

    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("Renda mensal: "))
    valor = float(input("Valor do empréstimo: "))
    parcelas = int(input("Número de parcelas (3 a 24): "))

    # Validação de parcelas
    if parcelas < 3 or parcelas > 24:
        print("Número de parcelas inválido!")
        return

    # Verificar aprovação
    if not pode_aprovar(idade, renda, valor):
        print("\nEmpréstimo NEGADO.")
        return

    # Definir taxa
    taxa = definir_taxa(parcelas)

    # Calcular valores
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    # Exibir resultados
    print("\n=== Empréstimo APROVADO ===")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa de juros: {taxa*100:.1f}% ao mês")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Total de juros: R$ {juros:.2f}")

# Executar o programa
main()