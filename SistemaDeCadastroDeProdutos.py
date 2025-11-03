tupla_disponiveis = ("Alimento", "Bebida", "Tecnologia", "Objeto Doméstico", "Limpeza", "Outros")
lista_produtos = []
codigos_cadastrados = set()

print("Bem-vindo ao sistema de gerenciamento de produtos!")

while True:
    print("\n----- MENU PRINCIPAL -----")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Atualizar Produto")
    print("5 - Excluir Produto")
    print("0 - Sair")

    try:
        valor_escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    if valor_escolha == 0:
        print("Saindo do sistema...")
        break

    elif valor_escolha == 1:
        print("\nEssas são as categorias disponíveis para o seu produto:")
        for i, cat in enumerate(tupla_disponiveis, start=1):
            print(f"{i} - {cat}")

        try:
            codigo = int(input("Qual o código do produto? "))
        except ValueError:
            print("Código inválido. Deve ser um número inteiro.")
            continue

        while codigo in codigos_cadastrados:
            print("Esse código já está cadastrado. Digite outro.")
            codigo = int(input("Qual o código do produto? "))

        nome = input("Qual o nome do produto? ").strip()
        try:
            preco = float(input("Qual o preço do produto? "))
            quantidade = int(input("Qual a quantidade do produto? "))
        except ValueError:
            print("Preço ou quantidade inválidos. Tente novamente.")
            continue

        try:
            categoria_num = int(input("Escolha o número da categoria: "))
            if 1 <= categoria_num <= len(tupla_disponiveis):
                categoria = tupla_disponiveis[categoria_num - 1]
            else:
                print("Número de categoria inválido. Será classificado como 'Outros'.")
                categoria = "Outros"
        except ValueError:
            categoria = "Outros"

        codigos_cadastrados.add(codigo)
        lista_produtos.append({
            "Código": codigo,
            "Nome": nome,
            "Preço": preco,
            "Quantidade": quantidade,
            "Categoria": categoria
        })

        print("Produto cadastrado com sucesso.")
        print("-" * 80)

    elif valor_escolha == 2:
        if not lista_produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nLista de produtos:")
            for produto in lista_produtos:
                print(produto)
                print("-" * 80)

    elif valor_escolha == 3:
        nome_buscar = input("Qual o nome do produto que você quer buscar? ").lower()
        encontrado = False
        for produto in lista_produtos:
            if nome_buscar == produto["Nome"].lower():
                print("\nProduto encontrado:")
                print(produto)
                print("-" * 80)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif valor_escolha == 4:
        if not lista_produtos:
            print("Não há produtos para atualizar.")
            continue

        print("\nProdutos disponíveis para atualização:")
        for produto in lista_produtos:
            print(produto)
            print("-" * 80)

        nome_atualizar = input("Qual o nome do produto que você quer atualizar? ").lower()
        for produto in lista_produtos:
            if nome_atualizar == produto["Nome"].lower():
                print("\nEscolha o atributo para atualizar:")
                print("1 - Código")
                print("2 - Nome")
                print("3 - Preço")
                print("4 - Quantidade")
                print("5 - Categoria")

                try:
                    atributo = int(input("Número do atributo: "))
                except ValueError:
                    print("Valor inválido.")
                    break

                if atributo == 1:
                    novo_codigo = int(input("Novo código: "))
                    while novo_codigo in codigos_cadastrados:
                        print("Esse código já existe. Digite outro.")
                        novo_codigo = int(input("Novo código: "))
                    codigos_cadastrados.remove(produto["Código"])
                    produto["Código"] = novo_codigo
                    codigos_cadastrados.add(novo_codigo)

                elif atributo == 2:
                    novo_nome = input("Novo nome: ").strip()
                    produto["Nome"] = novo_nome

                elif atributo == 3:
                    novo_preco = float(input("Novo preço: "))
                    produto["Preço"] = novo_preco

                elif atributo == 4:
                    nova_quantidade = int(input("Nova quantidade: "))
                    produto["Quantidade"] = nova_quantidade

                elif atributo == 5:
                    print("\nCategorias disponíveis:")
                    for i, cat in enumerate(tupla_disponiveis, start=1):
                        print(f"{i} - {cat}")
                    try:
                        nova_categoria_num = int(input("Número da nova categoria: "))
                        if 1 <= nova_categoria_num <= len(tupla_disponiveis):
                            produto["Categoria"] = tupla_disponiveis[nova_categoria_num - 1]
                        else:
                            print("Categoria inválida. Será 'Outros'.")
                            produto["Categoria"] = "Outros"
                    except ValueError:
                        produto["Categoria"] = "Outros"

                else:
                    print("Atributo inválido.")
                    break

                print("Atualização feita com sucesso.")
                print("-" * 80)
                break
        else:
            print("Produto não encontrado.")

    elif valor_escolha == 5:
        if not lista_produtos:
            print("Não há produtos para excluir.")
            continue

        print("\nProdutos disponíveis para exclusão:")
        for produto in lista_produtos:
            print(produto)
            print("-" * 80)

        produto_excluir = input("Qual o nome do produto que você quer excluir? ").lower()
        encontrado = False
        for produto in lista_produtos:
            if produto["Nome"].lower() == produto_excluir:
                lista_produtos.remove(produto)
                codigos_cadastrados.remove(produto["Código"])
                print("Produto excluído com sucesso.")
                print("-" * 80)
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    else:
        print("Opção inválida. Escolha um número de 0 a 5.")
