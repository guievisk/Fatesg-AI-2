# 📊 Pesquisa: Bancos de Dados NoSQL (SENAI)

> Repositório criado para documentar o estudo sobre tecnologias de bancos de dados não-relacionais.

---

## 📋 Enunciado da Atividade
![Enunciado](ATIVIDADE.png)

---

## 1. Definição e Características

*   **O que caracteriza um NoSQL?** 
    Diferente dos bancos SQL, eles não utilizam tabelas rígidas. São caracterizados por esquemas flexíveis, alta escalabilidade horizontal e otimização para dados não estruturados.
*   **Vantagens:** 
    Flexibilidade, facilidade de expansão e alta performance para grandes volumes de dados.
*   **3 Situações Práticas:**
    1. Big Data e análise em tempo real.
    2. Gestão de Conteúdo (CMS) com atributos variáveis.
    3. Aplicações de IoT (Internet das Coisas).

---

## 2. Tipos de Bancos de Dados NoSQL

| Tipo | Descrição | Exemplos |
| :--- | :--- | :--- |
| **Documentos** | Armazena dados em JSON/BSON | MongoDB, CouchDB |
| **Chave-Valor** | Simples e ultrarrápido (chave única) | Redis, DynamoDB |
| **Colunas** | Otimizado para grandes volumes | Cassandra, HBase |
| **Grafos** | Focado em relacionamentos complexos | Neo4j, ArangoDB |

---

## 3. Comparação Prática

*   **Relacional vs. Grafos:** No relacional, as relações exigem "JOINs" lentos. Em grafos, a conexão é um dado nativo, sendo muito mais rápido para redes complexas.
*   **Redes Sociais:** O mais adequado é o **Banco de Grafos**, pois ele lida de forma nativa com amizades e conexões (nós e arestas).

---

## 4. Escalabilidade e Flexibilidade

*   **Escalabilidade Horizontal:** Consiste em adicionar mais servidores ao sistema (em vez de apenas um potente), permitindo que o banco cresça conforme a demanda.
*   **Flexibilidade de Schema:** É vital em bancos de documentos para permitir mudanças rápidas no software sem precisar migrar ou travar a base de dados.

---

## 5. Estudo de Caso: Netflix 🍿

A **Netflix** utiliza o **Apache Cassandra** para gerenciar o histórico de milhões de usuários. 
**Benefícios:** Isso garante que o serviço nunca fique fora do ar (alta disponibilidade) e que a sua lista de filmes carregue instantaneamente em qualquer lugar do mundo.
