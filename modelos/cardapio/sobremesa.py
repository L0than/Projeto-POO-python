from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tamanho, tipo, descricao):
        super().__init__(nome, preco)
        self.tamanho = tamanho
        self.tipo = tipo
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15