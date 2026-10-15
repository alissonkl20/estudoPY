#a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25,
# 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
#  53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77,
#  79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

#print(a[2::9])

# Correção 1: O 'for' deve começar grudado na margem esquerda
# Correção 2: Usamos len(a) para obter o tamanho da lista (50)
#max = 10
#min = 4

#rag = max & min

#for i in range(rag):
    # Correção 3: Alinhado com 4 espaços/1 tab. Mostra o elemento atual da repetição
    #print(a[i])

#print(a[2::9])

##class Viagem:

  """def __init__(self, preco: float):
    self.preco = preco
    # Cria uma lista (array) de 20 posições.
    # False significa vaga LIVRE. True significa vaga OCUPADA.
    self.vagas = [False] * 200


def marcar_vaga(bus: Viagem):
  # 1. Desenha o mapa ASCII do ônibus (2 fileiras de cada lado, total 4 colunas)
  print("\n=== MAPA DO ÔNIBUS ===")
  print("  [ Motorista ]")
  print("-----------------")

  for i in range(0, 80, 4):
    linha = []
    for j in range(4):
      if i + j < 40:
        assento_num = i + j + 1
        # Se a vaga estiver ocupada (True), exibe [ X ]. Se livre, exibe o número [01]
        if bus.vagas[i + j]:
          status = "[ X ]"
        else:
          status = f"[{assento_num:02d}]"

        linha.append(status)

        # Adiciona o corredor central após as 2 primeiras colunas
        if j == 1:
          linha.append("   ")

    print(" ".join(linha))
  print("-----------------")
  print("Legenda: [ X ] Ocupado | [No] Disponível\n")

  # 2. Campo de input para o usuário escolher o assento
  try:
    escolha = int(
        input(f"Preço da passagem: R${bus.preco:.2f}. Escolha uma vaga (1-20): ")
    )
    indice = escolha - 1

    # 3. Lógica de validação e marcação
    if indice < 0 or indice >= 20:
      print("❌ Número de vaga inválido! Escolha entre 1 e 20.")
    elif bus.vagas[indice]:
      print(f"❌ A vaga {escolha} já está ocupada! Escolha outra.")
    else:
      bus.vagas[indice] = True
      print(f"✅ Vaga {escolha} reservada com sucesso!")

  except ValueError:
    print("❌ Entrada inválida! Por favor, digite um número.")


# --- TESTANDO O SISTEMA ---
# Criamos um ônibus com preço de R$ 50.00
meu_onibus = Viagem(50.00)

# Loop simulando o sistema rodando para testar várias marcações
while True:
  marcar_vaga(meu_onibus)

  continuar = (
      input("\nDeseja reservar outra vaga? (s/n): ").strip().lower()
  )
  if continuar != "s":
    print("\nObrigado por usar o sistema de reservas!")
    break
"""




