#Calculadora de Média Escolar

#Iniciando
confirmacao = input("Deseja calcular a média de nota? (sim/nao) ")

#Coletando os dados
while confirmacao == "sim":
    nome = input("Qual é o nome? ")
    materia = input("Qual é a matéria? ")
    nota1 = float(input("Qual é a 1° nota? "))
    nota2 = float(input("Qual é a 2° nota? "))
    media = (nota1 + nota2) / 2

#Verificando e Alertando nota
    if nota1 < 0 or nota1 > 25 or nota2 < 0 or nota2 > 25:
        print("Uma ou ambas as notas são inválidas!")
    elif media >= 20:
        print("Excelente nota!")
    elif 15 <= media < 20:
        print("Boa nota!")
    else:
        print("Reprovado!")

#Outra nota
    confirmacao = input("Deseja calcular a média de outra nota? (sim/nao) ")

#Encerrando
print("Programa encerrado.")
