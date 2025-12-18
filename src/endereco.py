class Endereco:
    def __init__(self, rua: str, numero: str, cidade: str, uf: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.uf = uf
        self.cep = cep

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.uf} ({self.cep})"