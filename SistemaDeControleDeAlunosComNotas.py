sair = 'ficar'
AlunoMatricula = {}
MatriculaNota = {}
Nomes = set()
Matriculas = set()

while sair == "ficar":

  print('\n1 - Cadastrar aluno \n2 - Registrar notas \n3 - Listar alunos e médias \n4 - Buscar aluno \n5 - Mostrar aprovados e reprovados \n6 - Relatórios \n0 - Sair')

  try:


    usuario = int(input('\nUsuario: '))


    if usuario == 1:

      Aluno = input("\nNome do Aluno: ")
      Aluno_validado = False

      while Aluno_validado == False:

        if Aluno in Nomes:
          print('\nEsse aluno já foi registrado!')
          Aluno = input("\nDigite o nome de outro aluno: ")
        else:
          Nomes.add(Aluno)
          Aluno_validado = True

      Matricula = int(input("\nMatricula(Apenas numeros): "))
      Matricula_validada = False

      while Matricula_validada == False:

        if Matricula in Matriculas:
          print('\nEssa Matricula já foi registrada!')
          Matricula = int(input("\nNova matricula(Apenas numeros): "))
        else:
          Matriculas.add(Matricula)
          Matricula_validada = True

      AlunoMatricula[Aluno] = Matricula
      print("\nAluno Cadastrado com Sucesso!")


    elif usuario == 2:

      Lista = []
      print('\n1 - Nome do Aluno \n2 - Matricula do Aluno')
      registro = int(input('\nUsuario: '))

      if registro == 1:

        Aluno = input("\nNome do Aluno: ")

        for i in range(1,4):

          Nota = float(input(f"Nota {i}: "))
          Lista.append(Nota)

        MatriculaNota[AlunoMatricula[Aluno]] = tuple(Lista)

      elif registro == 2:

        Matricula = int(input("\nMatricula: "))

        for i in range(1,5):

          Nota = float(input(f"Nota {i}: "))
          Lista.append(Nota)

        MatriculaNota[Matricula] = tuple(Lista)

      print("\nNotas Cadastradas com Sucesso!")


    elif usuario == 3:

      for aluno, matricula in AlunoMatricula.items():

        if matricula in MatriculaNota:

          notas = MatriculaNota[matricula]
          media = sum(notas) / len(notas)
          print(f"\nAluno: {aluno} | Matrícula: {matricula} | Notas: {notas} | Média: {media:.2f}")
        else:
          print(f"\nAluno: {aluno} | Matrícula: {matricula} | Notas não registradas.")

      if not Nomes:
        print('\nBanco de dados vazio...')


    elif usuario == 4:

      print('\n1 - Buscar nome de aluno \n2 - Buscar matricula do aluno')
      registro = int(input('\nUsuario: '))

      if registro == 1:

        Aluno = input('\nNome do aluno: ')

        if Aluno in AlunoMatricula:

            matricula = AlunoMatricula[Aluno]

            if matricula in MatriculaNota:

                notas = MatriculaNota[matricula]
                media = sum(notas) / len(notas)
                print(f"\nAluno: {Aluno} | Matrícula: {matricula} | Notas: {notas} | Média: {media:.2f}")
            else:
                print(f"\nAluno: {Aluno} | Matrícula: {matricula} | Notas não registradas.")

        else:
            print("\nAluno não está no banco de dados!")


      if registro == 2:

        Matricula = int(input("\nMatrícula: "))
        encontrado = False

        for aluno, matricula in AlunoMatricula.items():

            if Matricula == matricula:

                encontrado = True

                if Matricula in MatriculaNota:

                    notas = MatriculaNota[Matricula]
                    media = sum(notas) / len(notas)
                    print(f"\nAluno: {aluno} | Matrícula: {matricula} | Notas: {notas} | Média: {media:.2f}")
                else:
                    print(f"\nAluno: {aluno} | Matrícula: {matricula} | Notas não registradas.")
                break

        if not encontrado:
            print("\nAluno não está no banco de dados!")


    elif usuario == 5:

      encontrado = False

      for aluno, matricula in AlunoMatricula.items():

        if matricula in MatriculaNota:

          encontrado = True
          notas = MatriculaNota[matricula]
          media = sum(notas) / len(notas)
          if media >= 7:
            print(f"\nAluno: {aluno} APROVADO!")
          else:
            print(f"\nAluno: {aluno} REPROVADO!!")

      if not encontrado:
            print("\nBanco de dados vazio!")


    elif usuario == 6:

      print('\n1 - Alunos Cadastrados \n2 - Medias Individuais \n3 - Aprovados e Reprovados')
      registro = int(input("\nUsuario: "))

      if registro == 1:

        for aluno, matricula in AlunoMatricula.items():

          print(f"\nAluno: {aluno} | Matrícula: {matricula}")

        if not Nomes:
          print('\nBanco de dados vazio...')

      elif registro == 2:

        for aluno, matricula in AlunoMatricula.items():

          if matricula in MatriculaNota:

            notas = MatriculaNota[matricula]
            media = sum(notas) / len(notas)
            print(f"\nAluno: {aluno} | Média: {media:.2f}")
          else:
            print(f"\nAluno: {aluno} | Sem notas")

        if not Nomes:
          print('\nBanco de dados vazio...')

      elif registro == 3:

        encontrado = False

        for aluno, matricula in AlunoMatricula.items():

          if matricula in MatriculaNota:

            encontrado = True
            notas = MatriculaNota[matricula]
            media = sum(notas) / len(notas)
            if media >= 7:
              print(f"\nAluno: {aluno} APROVADO!")
            else:
              print(f"\nAluno: {aluno} REPROVADO!!")

        if not encontrado:
            print("\nBanco de dados vazio!")


    elif usuario == 0:
      sair = "a"
      

  except ValueError:
    print('\nValor invalido!')