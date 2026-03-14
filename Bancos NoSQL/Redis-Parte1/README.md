Redis CLI - Exercícios Práticos (SENAI/FATESG)
Este repositório contém a execução dos comandos práticos de Redis (Interface de Linha de Comando) realizados durante a disciplina de Banco de Dados Não Relacional do curso de Tecnologia em Inteligência Artificial.

🚀 Objetivo
Demonstrar a manipulação de diferentes tipos de dados no Redis, incluindo Strings, Listas, Hashes e Contadores, utilizando comandos fundamentais via CLI.

🛠️ Comandos Executados
1. Manipulação de Strings
Utilizado para armazenar e recuperar valores simples.

Bash
SET nome "Joao"
GET nome
Resultado: Armazena a string "Joao" na chave nome e a recupera em seguida.

2. Trabalho com Listas
Gerenciamento de coleções ordenadas de dados.

Bash
LPUSH frutas "maca" "banana" "laranja"
LRANGE frutas 0 -1
Resultado: Adiciona três elementos à lista frutas e exibe todos os itens.

3. Estruturas de Hash (Dicionários)
Armazenamento de objetos estruturados com múltiplos campos.

Bash
HSET usuario:123 nome "Maria" idade "30" cidade "Sao Paulo"
HGETALL usuario:123
Resultado: Cria um objeto de usuário com ID 123 contendo nome, idade e cidade.

4. Contadores Atômicos
Utilização do Redis para incremento de métricas em tempo real.

Bash
SET visitas 0
INCR visitas
INCR visitas
GET visitas
Resultado: Inicializa um contador e realiza dois incrementos sucessivos, resultando no valor 2.

💻 Ambiente de Execução
OS: Windows 11

Interface: Redis-CLI via PowerShell/CMD

Local: C:\Program Files\Redis

Desenvolvido por: Guilherme
Curso: Tecnologia em Inteligência Artificial - SENAI/FATESG (2026)
