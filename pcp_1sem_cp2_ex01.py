peso = float(input("Quantas toneladas o caminhao tem?: "))
estado = int(input("Qual o código do estado de origem da carga? (1 a 5): "))
codigo = int(input("Qual o código da carga? (10 a 40): "))

peso_quilos = peso * 1000
print(f"O peso do caminhao em quilos é de: {peso_quilos}kg")

preco_quilo = 0
if 10 <= codigo <= 20:
  preco_quilo = 100
elif 21 <= codigo <= 30:
  preco_quilo = 250
elif 31 <= codigo <= 40:
  preco_quilo = 340
else:
  print("Código da carga inválido! Por favor, insira um valor entre 10 e 40")

if preco_quilo > 0:
  preco_carga = peso_quilos * preco_quilo
  print(f"O preco da carga é de: R${preco_carga}")

  imposto = 0
  if estado == 1:
    imposto = 35
  elif estado == 2:
    imposto = 25
  elif estado == 3:
    imposto = 15
  elif estado == 4:
    imposto = 5
  elif estado == 5:
    imposto = 0
  else:
    print("Erro: Código de estado inválido! Por favor, insira um valor entre 1 e 5")

  print(f"O imposto pelo estado da carga é de: {imposto}%")

  preco_imposto = preco_carga * imposto
  preco_total = preco_carga + preco_imposto

  print(f"O preço do imposto é de: R${preco_imposto}")
  print(f"O valor total transportado pelo caminhão é de: R${preco_total}")
else:
  print("Não foi possível calcular o preço da carga devido a um código de carga inválido.")