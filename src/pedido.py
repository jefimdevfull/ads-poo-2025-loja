from enum import Enum

class StatusPedido(Enum):
    PENDENTE = "Pendente"
    PAGO = "Pago"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"

class Pedido:
    def __init__(self, cliente_nome: str, frete: float):
        self._cliente = cliente_nome
        self._frete = frete
        self._itens = []
        self._pagamentos = []
        self._status = StatusPedido.PENDENTE
    
    @property
    def status(self):
        return self._status

    @property
    def total(self):
        soma_itens = sum([item.preco * item.quantidade for item in self._itens])
        return soma_itens + self._frete

    def adicionar_item(self, item):
        if self._status != StatusPedido.PENDENTE:
            print("Erro: Não é possível adicionar itens a um pedido fechado.")
            return
        
        self._itens.append(item)
        print(f"Item '{item.nome}' adicionado ao pedido.")

    def registrar_pagamento(self, pagamento):
        self._pagamentos.append(pagamento)
        
        total_pago = sum([p.valor for p in self._pagamentos])
        
        if total_pago >= self.total:
            self._status = StatusPedido.PAGO
            print(f"Pedido quitado! Status alterado para {self._status.value}")
        else:
            falta = self.total - total_pago
            print(f"Pagamento registrado. Ainda faltam R$ {falta:.2f}")

    def __str__(self):
        return f"Pedido de {self._cliente} | Status: {self._status.value} | Total: R$ {self.total:.2f}"