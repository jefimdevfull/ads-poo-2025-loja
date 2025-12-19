class Pedido:
    def _init_(self, cliente_nome: str, frete: float):
        # Atributos protegidos (Encapsulamento)
        self._cliente = cliente_nome
        self._frete = frete
        self._itens = []
        self._pagamentos = []
        self._status = StatusPedido.PENDENTE

    @property
    def status(self):
        return self._status

    def adicionar_item(self, item: 'ItemPedido'):
        if self._status != StatusPedido.PENDENTE:
            print("❌ Erro: Não é possível alterar pedidos já processados.")
            return
        self._itens.append(item)

    def calcular_total(self) -> float:
        total_produtos = sum(item.subtotal() for item in self._itens)
        return total_produtos + self._frete

    def registrar_pagamento(self, pagamento_obj: 'Pagamento'):
        if self._status == StatusPedido.CANCELADO:
            print("❌ Erro: Pedido cancelado não aceita pagamentos.")
            return

        if pagamento_obj.processar():
            self._pagamentos.append(pagamento_obj)
            # Ajuste aqui: usar o atributo interno _status
            self._status = StatusPedido.PAGO
            print(f"✅ Pagamento registrado para {self._cliente}!")