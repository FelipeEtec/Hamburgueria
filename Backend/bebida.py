from itemCardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def exibirBebida(self):
        """
        Exibe as informações da bebida cadastrada. (nome, preço e tamanho)
        """
        super().exibirItem()
        print(f"Tamanho: {self.tamanho}ml")
    # Fim do método exibirBebida
# Fim da classe Bebida
