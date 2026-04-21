cp1 = float(input("Digite a nota do primeiro CheckPoint (0 a 10): "))
cp2 = float(input("Digite a nota do segundo CheckPoint (0 a 10): "))
cp3= float(input("Digite a nota do terceiro CheckPoint (0 a 10): "))
sp1 = float(input("Digite a nota da primeira Sprint (0 a 10): "))
sp2 = float(input("Digite a nota da segunda Sprint (0 a 10): "))
gs = float(input("Digite a nota do Global Solution (0 a 10): "))

menor_cp = cp1
if cp2 < menor_cp:
    menor_cp = cp2
if cp3 < menor_cp:
    menor_cp = cp3

soma_cp = (cp1 + cp2 + cp3) - menor_cp

media = ((soma_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6

print(f"A média do semestre sem o peso foi: {media:.1f}")

mediaPeso = media * 0.4

print(f"A média do semestre com o peso foi: {mediaPeso:.1f}")
