class Exercicios:
    def __init__(self):
        print('-')

    def exercicio1(self):
        nome_funcionario = "Fulano"
        idade = 30
        salario = 5000.00
        cargo = "Gerente"
        turno = "matutino"
        setor = "Vendas"

    def exercicio2(self):
        nome_escola = "Escola Militar"
        estado = "São Paulo"
        num_professores = 20
        cidade = "São Paulo"
        num_militares = 10
        logradouro = "Rua das Escolas, 123"
        num_alunos = 500
        colegio_militar = True
        disciplinas = ["Matemática", "Português", "História", "Geografia"]

    def exercicio3(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5

        print(valor1 + valor2)
        print(valor1 + valor2 + valor4)
        print(valor1 + valor2 - valor5)
        print(valor1 + int(valor3))
        print(valor1 * valor2)
        print((valor4 * valor2) / 2)
        print((valor1 + valor2 + valor4 + valor5) / 4)

    def exercicio4(self):
        v1 = 2
        v2 = 3
        v3 = 5
        v4=6

        soma_valores = v1 + v2 + v3 + v4
        media_valores = soma_valores / 4

    def exercicio5(self):
         nota1 = 64
         nota2 = 45
         nota3 = 60

         media_notas = (nota1 + nota2 + nota3) / 3

         if media_notas >= 60:
             print("Aluno aprovado")
         else:
             print("Aluno reprovado")

    def exercicio6(self):
         # Supondo que exista uma variável booleana chamada certificado_aprovacao
         certificado_aprovacao = True

         if certificado_aprovacao:
             print("Aluno foi aprovado com certificado")
         else:
             # Supondo que exista uma variável chamada aprovado
             aprovado = True

             if aprovado:
                 print("Aluno apenas aprovado")
             else:
                 print("Aluno reprovado")

exercicios = Exercicios()
exercicios.exercicio1()
exercicios.exercicio2()
exercicios.exercicio3()
exercicios.exercicio4()
exercicios.exercicio5()
exercicios.exercicio6()

