#  💻Mini Projetos em Python — Controle de Produtos e Alunos

Este repositório contém dois sistemas desenvolvidos em Python como parte da disciplina Programação I, do curso de Bacharelado em Engenharia de Software.
Os projetos têm como objetivo aplicar os conceitos de estruturas de repetição e estruturas de dados em programas funcionais, interativos e bem estruturados.

# 🛒 Projeto 1 – Sistema de Cadastro de Produtos (Mini Controle de Estoque)

## 🧠 Descrição

O sistema foi desenvolvido para auxiliar uma pequena loja no controle de seus produtos.
Ele permite cadastrar, listar, buscar, atualizar e excluir produtos, garantindo que não existam códigos duplicados e que todas as informações sejam armazenadas de forma organizada.

Cada produto é representado por um dicionário, e todos os produtos são armazenados em uma lista.
As categorias são definidas em uma tupla, e os códigos já cadastrados são controlados através de um set, evitando repetições.

## ⚙️ Funcionalidades

1 - Cadastrar produto: adiciona um novo produto com código, nome, preço, quantidade e categoria.

2 - Listar produtos: exibe todos os produtos cadastrados com suas informações.

3 - Buscar produto: permite procurar um produto pelo nome.

4 - Atualizar produto: altera informações de um produto existente.

5 - Excluir produto: remove um produto da lista e do set de códigos.

0 - Sair: encerra o sistema.

## 💾 Estruturas de dados utilizadas

list → para armazenar todos os produtos.

dict → para guardar as informações de cada produto (código, nome, preço, quantidade).

tuple → para armazenar as categorias disponíveis.

set → para registrar códigos já utilizados, evitando duplicatas.

## 💬 Exemplo de uso
```Python
-------Bem-vindo ao Sistema de Cadastro de Produtos----------

1 - Cadastrar Produto
2 - Listar Produtos
3 - Buscar Produto
4 - Atualizar Produto
5 - Excluir Produto
0 - Sair

```
O que você quer fazer no sistema? 1
Qual o código do produto? 101
Qual o nome do produto? Arroz
Qual o preço do produto? 7.99
Qual a quantidade do produto? 10
Qual a categoria do produto (1-5)? 1
✅ Produto cadastrado com sucesso!

# 🎓 Projeto 2 – Sistema de Controle de Alunos e Notas
## 🧠 Descrição

O segundo sistema foi desenvolvido para uma escola fictícia e tem como objetivo registrar alunos, armazenar notas e calcular médias, ajudando professores a acompanhar o desempenho dos estudantes.

Cada aluno é identificado por uma matrícula (chave) e possui suas notas armazenadas em uma tupla dentro de um dicionário principal.
O programa permite consultar médias, identificar aprovados e reprovados, e gerar relatórios personalizados.

# ⚙️ Funcionalidades

1 - Cadastrar aluno: registra um novo aluno com nome e matrícula.

2 - Registrar notas: permite inserir as notas de um aluno específico.

3 - Listar alunos e médias: mostra todos os alunos com suas respectivas médias.

4 - Buscar aluno: exibe as notas e a média de um aluno específico.

5 - Mostrar aprovados e reprovados: separa os alunos conforme a média (≥7 aprovado, <7 reprovado).

6 - Relatórios: permite escolher entre:

Alunos cadastrados

Médias individuais

Aprovados e reprovados

0 - Sair: encerra o sistema.

## 💾 Estruturas de dados utilizadas

dict → dicionário principal com a matrícula como chave e a tupla de notas como valor.

list → lista temporária para coletar as notas antes de transformá-las em tupla.

set → armazena os nomes dos alunos cadastrados, evitando duplicações.

tuple → usada para guardar as notas de cada aluno de forma imutável.

## 💬 Exemplo de uso
```Python
1 - Cadastrar aluno
Digite o nome: Ana
Digite a matrícula: 2025
Aluno cadastrado com sucesso!

2 - Registrar notas
Digite a matrícula do aluno: 2025
Digite a primeira nota: 8
Digite a segunda nota: 7.5
Digite a terceira nota: 9
Notas registradas com sucesso!

3 - Listar alunos e médias
Ana - Média: 8.16
```

# 📚 Conceitos aplicados nos projetos

Estruturas de repetição (while, for)

Estruturas de dados (list, dict, set, tuple)

Condicionais (if, elif, else)

Funções de entrada e saída (input(), print())

Validação de dados e tratamento de duplicidades

Organização lógica e uso de menus interativos

# 🧑‍💻 Autores

Projeto desenvolvido por [Emanuel Cândido da Silva Lima] e [Rainan Araujo],
como parte da avaliação prática para a disciplina Programação I – Python.
