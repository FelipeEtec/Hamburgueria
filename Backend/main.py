from sanduiche import Lanche
from sanduiche import Cardapio

resposta = "s"
# Criação do objeto Cardápio
c = Cardapio()
while resposta == 's':

    ingredientes = []
    nome = input("Nome do sanduiche: ")
    preco = float(input("Preço do sanduiche: "))

    for i in range(3):
        ingrediente = input(f"Informe o ingrediente {i + 1}: ")
        ingredientes.append(ingrediente)

    # Criando o objeto Lanche dentro do laço
    l = Lanche(nome, preco, ingredientes)

    # Adicionando o lanche "l" ao cardapio "c"
    c.adicionar_item(l)
    resposta = input("Deseja adicionar outro item? (s/n): ")

# Fim do laço while

print(f"\nCardápio:\n{c}")
