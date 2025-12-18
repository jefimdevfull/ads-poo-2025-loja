class ItemCarrinho:
    def __init__(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")
        if quantidade > produto.estoque:
            raise ValueError("Estoque insuficiente")

        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade

    def atualizar_quantidade(self, nova_quantidade):
        if nova_quantidade <= 0:
            raise ValueError("Quantidade inválida")
        if nova_quantidade > self.produto.estoque:
            raise ValueError("Estoque insuficiente")

        self.quantidade = nova_quantidade
        self.subtotal = self.produto.preco * nova_quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        for item in self.itens:
            if item.produto.sku == produto.sku:
                item.atualizar_quantidade(item.quantidade + quantidade)
                return

        self.itens.append(ItemCarrinho(produto, quantidade))

    def remover_item(self, sku):
        self.itens = [item for item in self.itens if item.produto.sku != sku]

    def calcular_total(self):
        return sum(item.subtotal for item in self.itens)
