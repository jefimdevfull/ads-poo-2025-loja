# Sistema de Loja Virtual Simplificada

Este repositório contém o projeto da disciplina de Programação Orientada a Objetos (POO) do curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Universidade Federal do Cariri (UFCA).

O objetivo é desenvolver um sistema de linha de comando (CLI) para uma loja virtual, aplicando conceitos como herança, encapsulamento, polimorfismo e composição.

---

## 👥 Distribuição de Responsabilidades da Equipe

Para a primeira etapa do desenvolvimento, a equipe definiu a seguinte divisão de responsabilidades, visando uma melhor organização, produtividade e integração dos componentes do sistema:

* **CICERO ANDREILSON SANTOS MENESES**
    * Responsável pela modelagem e implementação das classes relacionadas a **Produtos e Estoque**, incluindo CRUD de produtos, validações de atributos (preço, estoque, SKU) e métodos especiais aplicáveis.
    * Atuará também no apoio à persistência de dados dessas entidades.

* **CICERO JEFERSON SANTOS DE ARAÚJO**
    * Responsável pela estrutura geral do projeto, definição da arquitetura orientada a objetos e implementação das classes de **Cliente e Endereço**, com validações de email, CPF e unicidade.
    * Ficará responsável pela organização do repositório GitHub e documentação inicial (README).

* **JOSLEY VINICIUS BASTOS DA SILVA**
    * Responsável pelo desenvolvimento das classes relacionadas ao **Carrinho de Compras e Itens do Carrinho**, incluindo regras de negócio para adição, remoção, alteração de quantidade, cálculo de subtotal e validações de estoque.

* **LIVIA MARIA DE OLIVEIRA FERREIRA**
    * Responsável pela implementação inicial das classes de **Pedido e Pagamento**, contemplando estados do pedido, regras de transição, cálculo de total, aplicação de frete e registro de pagamentos, conforme os requisitos definidos no projeto.

> A equipe atuará de forma colaborativa, realizando revisões cruzadas de código e integrando as funcionalidades desenvolvidas individualmente.

---

## 🛠️ Principais Classes do Sistema

Abaixo estão listadas as classes mapeadas para a arquitetura do projeto, seus principais atributos e responsabilidades:

### 1. Produto
Representa os itens vendidos na loja. Pode ser especializado em **Produto Físico** ou **Produto Digital**.
* **Atributos:** SKU (identificador único), nome, categoria, preço, estoque, status (ativo/inativo) e peso (opcional).
* **Responsabilidades:** Exibir informações, comparação entre produtos (por SKU) e atualização de estoque.

### 2. Cliente
Representa o usuário comprador da loja.
* **Atributos:** ID, nome, e-mail, CPF e lista de endereços.
* **Responsabilidades:** Identificação única e validação de dados (E-mail/CPF).

### 3. Endereco
Composição utilizada pela classe Cliente para dados de entrega.
* **Atributos:** Rua, número, cidade, UF e CEP.

### 4. Carrinho
Gerencia a intenção de compra do cliente antes do fechamento do pedido.
* **Atributos:** ID do cliente associado e lista de itens.
* **Responsabilidades:** Adicionar/remover itens, alterar quantidades e calcular o subtotal provisório. Valida se a quantidade solicitada não excede o estoque.

### 5. ItemCarrinho
Classe associativa que liga um produto ao carrinho.
* **Atributos:** SKU, nome do produto, preço unitário (no momento da adição) e quantidade.

### 6. Pedido
Representa a consolidação da compra.
* **Atributos:** ID, cliente, lista de itens, valor do frete, desconto aplicado, valor total e status (CRIADO, PAGO, ENVIADO, ENTREGUE, CANCELADO).
* **Responsabilidades:** Calcular total final, aplicar cupons, processar transições de status e gerenciar estorno de estoque em caso de cancelamento.

### 7. ItemPedido
Garante o histórico do preço do produto no momento da compra (snapshot).
* **Atributos:** SKU, nome, preço congelado e quantidade.

### 8. Pagamento
Registra as transações financeiras do pedido.
* **Atributos:** ID, ID do pedido, forma de pagamento, valor e data.
* **Responsabilidades:** Validar se o valor pago cobre o total do pedido e acionar a baixa de estoque.

### 9. Cupom
Permite a aplicação de descontos no pedido.
* **Atributos:** Código, tipo (valor fixo ou percentual), valor do desconto e data de validade.
* **Responsabilidades:** Calcular o valor a ser descontado do total.

### 10. Frete
Responsável pelo cálculo do custo de envio.
* **Atributos:** Tabela de valores por UF, cidade ou faixa de CEP.
* **Responsabilidades:** Calcular o custo de envio baseado no endereço do cliente.
