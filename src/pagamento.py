from datetime import datetime

class Pagamento:
    def __init__(self, tipo: str, valor: float):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo.")
            
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        data_formatada = self.data.strftime("%d/%m/%Y %H:%M")
        return f"Pagamento: {self.tipo} | Valor: R$ {self.valor:.2f} | Data: {data_formatada}"