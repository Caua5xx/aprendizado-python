#Classificador de Nota Escolar com Alerta

#Coletando os dados
aluno = input("Digite seu nome: ")
materia = input("Digite a matéria: ")
nota = float(input("Digite sua nota: "))

#Mostrando os dados
print("Aluno: ", aluno)
print("Matéria: ", materia)
print("Nota: ", nota)

#Validando os dados
if nota < 0 or nota > 25:
    print("Nota Inválida!")
elif nota <= 5:
    print("Alerta Crítico!")
elif nota <= 10:
    print("Alerta Vermelho!")
elif nota <= 15:
    print("Alerta Laranja!")
elif nota <= 20:
    print("Alerta Amarela!")
else:
    print("Tudo Certo!")
