class ItemCardapio:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def exibirItem(self):
        """
        Exibe as informações do item cadastrado. (nome, preço e categoria)
        """
        print(f"Item: {self.nome}; Preço: R${self.preco:.2f}")
        print(f"Categoria: {self.categoria}")