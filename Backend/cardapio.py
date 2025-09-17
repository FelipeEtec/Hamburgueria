from sanduiche import Lanche
class Cardapio:
    # Criação do método adicionarItem()
    def adicionarItem(self,item: Lanche):
        """
        Adiciona um item do tipo Lanche ao cardápio.
        """
        self.itens.append(item)
    # Fim do método adicionarItem()

    def exibirCardapio(self):
        """
        Exibe o cardápio completo com todos os lanches cadastrados.
        """
        for item in self.itens:
            item.exibirLanche()
# Fim da classe