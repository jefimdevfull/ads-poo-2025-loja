# Sistema de Loja Virtual Simplificada

Este repositório contém o projeto da disciplina de Programação Orientada a Objetos (POO) do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Universidade Federal do Cariri (UFCA).

O objetivo é desenvolver um sistema de linha de comando (CLI) para uma loja virtual, aplicando conceitos como herança, encapsulamento, polimorfismo e composição.

---

## 👥 Distribuição de Responsabilidades da Equipe

Para a primeira etapa do desenvolvimento, a equipe definiu a seguinte divisão de tarefas:

* **CICERO ANDREILSON SANTOS MENESES**
    * Responsável pela modelagem e implementação das classes relacionadas a **Produtos e Estoque**, incluindo CRUD de produtos, validações de atributos (preço, estoque, SKU) e métodos especiais.
    * Atuará também no apoio à persistência de dados.

* **CICERO JEFERSON SANTOS DE ARAÚJO**
    * Responsável pela estrutura geral do projeto e implementação das classes de **Cliente e Endereço**, com validações de email, CPF e unicidade.
    * Responsável pela organização do repositório GitHub e documentação inicial.

* **JOSLEY VINICIUS BASTOS DA SILVA**
    * Responsável pelo desenvolvimento das classes relacionadas ao **Carrinho de Compras e Itens do Carrinho**, incluindo regras de negócio para adição/remoção de itens e cálculo de subtotal.

* **LIVIA MARIA DE OLIVEIRA FERREIRA**
    * Responsável pela implementação das classes de **Pedido e Pagamento**, contemplando estados do pedido, cálculo de total, aplicação de frete e registro de pagamentos.

---

## 🛠️ Principais Classes do Sistema

Abaixo estão listadas as classes do projeto, seus atributos e métodos planejados:

### 1. Produto
Representa os itens vendidos na loja (físico ou digital).
* **Atributos:** SKU, nome, categoria, preço, estoque, ativo, peso (opcional).
* **Métodos:** Mostrar informações, comparar por SKU, atualizar estoque.

### 2. Cliente
Representa o usuário comprador da loja.
* **Atributos:** ID, nome, e-mail, CPF, lista de endereços.
* **Métodos:** Comparar por e-mail ou CPF.

### 3. Endereco
Dados de localização para entrega.
* **Atributos:** Rua, número, cidade, UF, CEP.

### 4. Carrinho
Gerencia a compra antes do fechamento.
* **Atributos:** ID do cliente, lista de itens.
* **Métodos:** Adicionar item, remover item, alterar quantidade, calcular subtotal. (Regra: validar estoque).

### 5. ItemCarrinho
Associa um produto ao carrinho.
* **Atributos:** SKU, nome, preço, quantidade.

### 6. Pedido
Representa a compra finalizada.
* **Atributos:** ID, cliente, itens, frete, desconto, total, status.
* **Métodos:** Calcular total, aplicar cupom, registrar pagamento, enviar, entregar, cancelar.

### 7. ItemPedido
Snapshot do produto no momento da compra.
* **Atributos:** SKU, nome, preço, quantidade.

### 8. Pagamento
Registro financeiro da transação.
* **Atributos:** ID, ID do pedido, forma de pagamento, valor, data.
* **Métodos:** Validar se o valor cobre o total e debitar estoque (status PAGO).

### 9. Cupom
Descontos aplicáveis.
* **Atributos:** Código, tipo (valor ou porcentagem), valor, validade.
* **Métodos:** Calcular desconto.

### 10. Frete
Cálculo de logística.
* **Atributos:** UF, cidade, faixa de CEP, valor.
* **Métodos:** Calcular frete baseado no endereço.
