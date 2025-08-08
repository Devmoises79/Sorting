lista = [7, 5, 1, 8, 3]

print("=" * 75)
print("                 SISTEMA DE ORDENAÇÃO DE NÚMEROS")
print("=" * 75)

# Loop até o usuário digitar uma opção válida
while True:
    ordem = input("Digite 'c' para crescente ou 'd' para decrescente: ").strip().lower()
    if ordem in ('c', 'd'):
        break
    print("Opção inválida! Digite apenas 'c' ou 'd'.")

# Ordenação
if ordem == 'd':
    lista = sorted(lista, reverse=True)
    print("\nLista em ordem DECRESCENTE:")
else:
    lista = sorted(lista)
    print("\nLista em ordem CRESCENTE:")

# Exibir resultado
print(lista)
print("=" * 75)
