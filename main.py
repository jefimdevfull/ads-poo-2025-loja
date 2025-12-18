from src.cliente import Cliente
from src.endereco import Endereco
from src.produto import Produto

def teste_sistema():
    print("=== TESTE DA ENTREGA 1 - LOJA VIRTUAL ===")
    
    # 1. Testando Endereço e Cliente
    try:
        end1 = Endereco("Rua das Flores", "123", "Juazeiro", "CE", "63000-000")
        cli1 = Cliente(1, "Cicero Jeferson", "jeferson@email.com", "123.456.789-00")
        cli1.adicionar_endereco(end1)
        print(f"\n✅ Cliente Criado: {cli1}")
        print(f"📍 Endereço: {cli1.enderecos[0]}")
    except ValueError as e:
        print(f"❌ Erro no cliente: {e}")

    # 2. Testando Produto
    try:
        prod1 = Produto("SKU001", "Notebook Gamer", "Eletrônicos", 4500.00, 10)
        print(f"\n✅ Produto Criado: {prod1}")
        
        # Teste de validação de preço
        # prod1.preco = -50  # Isso deve gerar erro se descomentar
        
        prod1.atualizar_estoque(-2)
        print(f"🔄 Estoque atualizado (Venda de 2): {prod1.estoque}")
        
    except ValueError as e:
        print(f"❌ Erro no produto: {e}")

if __name__ == "__main__":
    teste_sistema()