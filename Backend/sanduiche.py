from itemCardapio import ItemCardapio
class Lanche(ItemCardapio):
    def __init__(self, nome, preco, categoria, ingredientes):
        super().__init__(nome, preco, categoria)
        self.ingredientes = ingredientes
    # Fim do construtor __init__()

    def exibirLanche(self):
        """
        Exibe as informações do lanche cadastrado. (nome, preço e ingredientes)
        """
        super().exibirItem()
        print(f"Ingredientes: {self.ingredientes}")
        # Fim do método exibirLanche

# Fim da classe Lanche





















sanduiches = [] 

for i in range(4):
  sanduiche = input("Nome do novo sanduiche:")
sanduiches.append(sanduiche)

for sanduiche in sanduiches:
    print(f"Lanche: {sanduiches}")
