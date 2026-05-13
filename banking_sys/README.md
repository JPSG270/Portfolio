
# SISTEMA BANCÁRIO v01

 Sistema bancário para usuário único, contendo ações de depósito,saque, extrato e saída.Feito com base em estruturas básicas,condicionais e de repetição.


## TECNOLOGIAS UTILIZADAS
Python 3.12;VSCode
## COMO EXECUTAR
Com base nas opções apresentadas,d(depósito),s(saque),e(extrato),q(saída), o usuário deve inserir no terminal uma dessas opções:

Depósito:o usuário deve depositar um valor para inserir ao saldo pessoal.

Saque:o usuário pode inserir um valor de saque de até R$500,00, além disso, ele pode fazer até 3 saques diários, ou seja, em uma execução esta ação pode ser realizada até 3 vezes.

Extrato:ao selecionar esta opção o usuário tem acesso visual a todas as transições feitas,desde saques até depósitos.

Saída:ao selecionar, o usuário encerra a operação.
## Aprendizados
Neste projeto de sistema bancário, trabalhei com estruturas básicas, de repetição e condicionais.Além disso, também obtive experiência em análise e tratamento de erros.
# BANKING SYSTEM v01

A single-user banking system featuring deposit, withdrawal, statement, and exit operations. Developed using fundamental programming concepts, conditional logic, and loops.

TECHNOLOGIES USED:
Python 3.12

VS Code

HOW TO RUN
Based on the menu options—d (deposit), s (withdraw), e (statement), and q (exit)—the user must enter the corresponding letter in the terminal.

Deposit: Enter a positive value to add to your personal balance.

Withdraw: You can withdraw up to R$ 500.00 per transaction. There is a daily limit of 3 withdrawals per session.

Statement: Displays a visual history of all transactions made (deposits and withdrawals) and the current balance.

Exit: Ends the application.

KEY LEARNINGS
In this banking system project, I practiced core Python syntax, including while loops and if/elif/else conditionals. Additionally, I gained experience in requirement analysis and basic error handling (such as validating input values and business rules).

# 🏦 SISTEMA BANCÁRIO v02 — Otimizado com Funções

Esta é a segunda versão do sistema bancário, evoluindo de um script linear para um modelo **modularizado com funções**. O foco desta versão foi a organização do código e a implementação de novas funcionalidades para suportar múltiplos usuários e contas bancárias.

## 🚀 Novidades da Versão 02

*   **Modularização:** O código foi totalmente refatorado em funções, seguindo boas práticas de programação.
*   **Cadastro de Usuários:** Possibilidade de registrar clientes com Nome, Data de Nascimento, Endereço e CPF (validado como chave única).
*   **Abertura de Contas:** Criação de contas correntes (Agência 0001) vinculadas a usuários cadastrados.
*   **Segurança nos Argumentos:** Uso de regras específicas do Python para garantir que dados financeiros sejam passados corretamente (argumentos posicionais e nomeados).

---

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.12
*   **Ambiente:** VS Code

---

## 📋 Como Executar

O sistema funciona via terminal. Ao iniciar, você deve primeiro cadastrar um usuário para depois criar uma conta.

### Funções de Gerenciamento:
*   **`[nu]` Novo Usuário:** Solicita os dados pessoais. O sistema impede CPFs duplicados e exige exatamente 11 dígitos.
*   **`[nc]` Nova Conta:** Vincula uma conta a um CPF já existente no sistema.

### Funções Financeiras:
*   **`[d]` Depósito:** Adiciona valores ao saldo. Requer argumentos estritamente **posicionais**.
*   **`[s]` Saque:** Permite retiradas de até R$ 500,00, com limite de 3 saques por sessão. Requer argumentos estritamente **nomeados** por segurança.
*   **`[e]` Extrato:** Exibe de forma visual o histórico de transações e o saldo atualizado.
*   **`[q]` Sair:** Encerra a execução do programa.

---

## 🧠 Aprendizados Evoluídos

Nesta etapa, o projeto permitiu o aprofundamento em conceitos avançados de Python:

1.  **Assinatura de Funções:** Aprendizado sobre o uso da barra (`/`) para argumentos posicionais e do asterisco (`*`) para argumentos nomeados (Keyword-only).
2.  **Encapsulamento:** Divisão de responsabilidades, onde cada função executa apenas uma tarefa específica.
3.  **Estruturas de Dados Complexas:** Manipulação de listas contendo dicionários para representar bancos de dados em memória.
4.  **Tratamento de Fluxo:** Uso de `continue`, `break` e `return` para gerenciar loops de validação de dados.

---

## 🌎 Banking System v02 (English Summary)

The second version of the banking system features a complete **functional refactor**. It introduces multi-user support and account management.

**Key Features:**
- **Functional Programming:** Code organized into reusable blocks.
- **User & Account Linking:** Accounts are now tied to a unique CPF identifier.
- **Parameter Safety:** Implemented positional-only and keyword-only arguments to prevent data mismatch.

**Technical Skills:** Advanced function signatures, data structure management, and refined logic flow.
