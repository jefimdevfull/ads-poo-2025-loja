from typing import List
from src.endereco import Endereco

class Cliente:
    def __init__(self, id: int, nome: str, email: str, cpf: str):
        self.id = id
        self.nome = nome
        self._email = email
        self._cpf = cpf
        self.enderecos: List[Endereco] = []

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if "@" not in valor:
            raise ValueError("Email inválido")
        self._email = valor

    @property
    def cpf(self):
        return self._cpf
    
    def adicionar_endereco(self, endereco: Endereco):
        self.enderecos.append(endereco)

    def __eq__(self, outro):
        if isinstance(outro, Cliente):
            return self.cpf == outro.cpf or self.email == outro.email
        return False

    def __str__(self):
        return f"ID: {self.id} | Cliente: {self.nome} | CPF: {self.cpf}"