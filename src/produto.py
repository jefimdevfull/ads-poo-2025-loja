class Produto:
    def __init__(self, sku: str, nome: str, categoria: str, preco: float, estoque: int):
        self.sku = sku
        self.nome = nome
        self.categoria = categoria
        self._preco = preco
        self._estoque = estoque
        self.ativo = True

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self._preco = valor

    @property
    def estoque(self):
        return self._estoque

    def atualizar_estoque(self, quantidade: int):
        """Adiciona ou remove itens do estoque (use valor negativo para remover)"""
        novo_estoque = self._estoque + quantidade
        if novo_estoque < 0:
            raise ValueError("Estoque insuficiente.")
        self._estoque = novo_estoque

    def __str__(self):
        return f"[{self.sku}] {self.nome} - R$ {self._preco:.2f} (Estoque: {self._estoque})"
    
    def __eq__(self, outro):
        return self.sku == outro.sku if isinstance(outro, Produto) else False