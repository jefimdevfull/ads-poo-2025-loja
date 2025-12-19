class ItemCarrinho:
    def __init__(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade inválida")
        if quantidade > produto.estoque:
            raise ValueError("Estoque insuficiente")

        self.sku = produto.sku
        self.nome = produto.nome
        self.preco = produto.preco
        self.quantidade = quantidade
        self.subtotal = self.preco * quantidade
        self._produto = produto  # referência para validação de estoque

    def atualizar_quantidade(self, nova_quantidade):
        if nova_quantidade <= 0:
            raise ValueError("Quantidade inválida")
        if nova_quantidade > self._produto.estoque:
            raise ValueError("Estoque insuficiente")

        self.quantidade = nova_quantidade
        self.subtotal = self.preco * nova_quantidade


class Carrinho:
    def __init__(self, id_cliente):
        self.id_cliente = id_cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        for item in self.itens:
            if item.sku == produto.sku:
                item.atualizar_quantidade(item.quantidade + quantidade)
                return

        self.itens.append(ItemCarrinho(produto, quantidade))

    def remover_item(self, sku):
        self.itens = [item for item in self.itens if item.sku != sku]

    def alterar_quantidade(self, sku, nova_quantidade):
        for item in self.itens:
            if item.sku == sku:
                item.atualizar_quantidade(nova_quantidade)
                return
        raise ValueError("Item não encontrado no carrinho")

    def calcular_subtotal(self):
        return sum(item.subtotal for item in self.itens)
