lista_produtos = []
codigos_cadastrados = set()
tupla_disponiveis = ("Alimento", "Bebida", "Tecnologia", "Objeto Doméstico", "Limpeza", "Outros")

while True:
    querer = input("Você quer entrar no sistema? ").lower()
    if querer != "sim":
        print("Ok, você não quer entrar no sistema")
        break

    print("-----Você entrou no sistema-----")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Buscar Produto")
    print("4 - Atualizar Produto")
    print("5 - Excluir Produto")
    print("6 - Verificar Categorias")
    print("0 - Sair")

    try:
        valor_escolha = int(input("O que você quer fazer no sistema? "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if valor_escolha == 1:
        print("Essas são as categorias disponíveis para o seu produto")
        for i, cat in enumerate(tupla_disponiveis, start=1):
            print(f"{i} - {cat}")
        categoria = int(input("Qual categoria você quer que seu produto se encaixe?(1 até 6) "))
        while categoria < 1 or categoria > 6:
            print("Valor inválido, insira um correto.")
            categoria = int(input("Qual categoria você quer que seu produto se encaixe?(1 até 6) "))

        codigo = int(input("Qual o código do produto? "))
        while codigo in codigos_cadastrados:
            print("Esse código já está cadastrado, insira outro código.")
            codigo = int(input("Qual o código do produto? "))

        nome = str(input("Qual o nome do produto? "))
        preco = float(input("Qual o preço do produto? "))
        while preco < 0:
            print("Valor incorreto, selecione um valor válido.")
            preco = float(input("Qual o preço do produto? "))

        quantidade = int(input("Qual a quantidade do produto? "))
        while quantidade < 0:
            print("Valor inválido, coloque um valor válido.")
            quantidade = int(input("Qual a quantidade do produto? "))

        codigos_cadastrados.add(codigo)
        produto = {
            "Código": codigo,
            "Nome": nome,
            "Preço": preco,
            "Quantidade": quantidade,
            "Categoria": tupla_disponiveis[categoria - 1]
        }
        lista_produtos.append(produto)
        print("Produto cadastrado com sucesso.")
        print("----------------------------------------------------------------------------------------")

    elif valor_escolha == 2:
        if not lista_produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("Listagem dos produtos:")
            for p in lista_produtos:
                print(p)
                print("----------------------------------------------------------------------------------------")

    elif valor_escolha == 3:
        nome_buscar = str(input("Qual o nome do produto que você quer buscar? ")).lower()
        encontrado = False
        for produto in lista_produtos:
            if produto["Nome"].lower() == nome_buscar:
                print("Produto encontrado:")
                print(produto)
                print("----------------------------------------------------------------------------------------")
                encontrado = True
        if not encontrado:
            print("Produto não encontrado.")

    elif valor_escolha == 4:
        if not lista_produtos:
            print("Nenhum produto disponível para atualização.")
        else:
            for p in lista_produtos:
                print(p)
                print("----------------------------------------------------------------------------------------")
            nome_atualizar = str(input("Qual o nome do produto que você quer atualizar? ")).lower()
            for produto in lista_produtos:
                if produto["Nome"].lower() == nome_atualizar:
                    print("1 - Código")
                    print("2 - Nome")
                    print("3 - Preço")
                    print("4 - Quantidade")
                    atributo = input("Qual atributo você quer mudar? ")

                    if atributo == "1" or atributo == "código":
                        novo_codigo = int(input("Qual o novo valor do seu código? "))
                        while novo_codigo in codigos_cadastrados:
                            print("Esse código já está cadastrado, insira outro.")
                            novo_codigo = int(input("Qual o novo valor do seu código? "))
                        codigos_cadastrados.remove(produto["Código"])
                        codigos_cadastrados.add(novo_codigo)
                        produto["Código"] = novo_codigo

                    elif atributo == "2" or atributo == "nome":
                        novo_nome = str(input("Qual o novo nome do seu produto? "))
                        produto["Nome"] = novo_nome

                    elif atributo == "3" or atributo == "preço":
                        novo_preco = float(input("Qual o seu novo preço: "))
                        produto["Preço"] = novo_preco

                    elif atributo == "4" or atributo == "quantidade":
                        nova_quantidade = int(input("Qual a nova quantidade do seu produto? "))
                        produto["Quantidade"] = nova_quantidade

                    print("Atualização feita com sucesso.")
                    print("----------------------------------------------------------------------------------------")
                    break
            else:
                print("Produto não encontrado para atualização.")

    elif valor_escolha == 5:
        if not lista_produtos:
            print("Nenhum produto disponível para exclusão.")
        else:
            for p in lista_produtos:
                print(p)
            print("----------------------------------------------------------------------------------------")
            produto_excluir = str(input("Qual o nome do produto que você quer excluir? ")).lower()
            encontrado = False
            for produto in lista_produtos[:]:
                if produto["Nome"].lower() == produto_excluir:
                    lista_produtos.remove(produto)
                    codigos_cadastrados.discard(produto["Código"])
                    encontrado = True
                    print("Exclusão feita com sucesso.")
                    print("----------------------------------------------------------------------------------------")
            if not encontrado:
                print("Produto não encontrado para exclusão.")

    elif valor_escolha == 6:
        print("Categorias disponíveis:")
        for i, cat in enumerate(tupla_disponiveis, start=1):
            print(f"{i} - {cat}")
        categoria_verificar = int(input("Qual categoria você quer verificar?(1 até 6) "))
        while categoria_verificar < 1 or categoria_verificar > 6:
            print("Valor inválido, insira um correto.")
            categoria_verificar = int(input("Qual categoria você quer verificar?(1 até 6) "))
        categoria_escolhida = tupla_disponiveis[categoria_verificar - 1]
        encontrados = [p for p in lista_produtos if p["Categoria"] == categoria_escolhida]
        if encontrados:
            print(f"Produtos cadastrados na categoria {categoria_escolhida}:")
            for p in encontrados:
                print(p)
        else:
            print("Nenhum produto nessa categoria.")

    elif valor_escolha == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, selecione uma opção existente.")
