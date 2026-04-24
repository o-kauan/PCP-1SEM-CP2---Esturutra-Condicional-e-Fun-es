lado_1 = float(input("Digite o valor do lado 1: "))
lado_2 = float(input("Digite o valor do lado 2: "))
lado_3 = float(input("Digite o valor do lado 3: "))

lados = [lado_1, lado_2, lado_3]

lados.sort(reverse=True)
print(lados)

A = lados [0]
B = lados [1]
C = lados [2]

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A **2 == B **2 + C **2:
        print("TRIANGULO RETANGULO")
    elif A **2 > B **2 + C **2:
        print("TRIANGULO OBTUSANGULO")
    elif (A**2) < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")