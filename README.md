# 🏦 Banco Python Console

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-concluído-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Projeto de um **sistema bancário simples** em Python, executado no console, com funcionalidades de depósito, saque e extrato, organizadas em funções para prática de programação estruturada.

---

## 📌 **Funcionalidades**

- 💰 Realizar depósitos
- 💸 Realizar saques com limite por operação e quantidade diária
- 📄 Exibir extrato de movimentações
- 🚪 Sair do sistema

---

## 🚀 **Tecnologias Utilizadas**

- Python 3.10+
- VS Code ou IDE de sua preferência

---

## ⚙️ **Como Executar**

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/banco-python-console.git

Regras de negócio
O saque tem limite máximo de R$ 500 por operação.

São permitidos até 3 saques por dia.

O valor do depósito e do saque deve ser positivo.

O CPF é utilizado para identificar usuários únicos.

Estrutura do código
menu(): Exibe o menu e recebe a opção do usuário.

depositar(): Realiza depósito na conta.

sacar(): Realiza saque, validando saldo, limites e número de saques.

exibir_extrato(): Mostra o extrato das transações.

criar_usuario(): Cadastra novo usuário.

filtrar_usuario(): Busca usuário pelo CPF.

criar_conta(): Cria uma nova conta para um usuário existente.

listar_contas(): Lista todas as contas cadastradas.

main(): Função principal que controla o fluxo do programa.

Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Faça commit das suas alterações (git commit -m 'Adicionar nova feature').

Faça push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.
