#Cofrinho digital com repetição simples.
questao = input("Deseja depositar uma quantia no cofrinho? (sim/nao) ")
total = 0

while questao == "sim":
    valor_deposito = float(input("Quanto deseja depositar? R$"))
    if valor_deposito <= 0:
        print("Valor inválido!")
    else:
        total += valor_deposito
    questao = input("Deseja depositar uma quantia no cofrinho? (sim/nao) ")

print("Total economizado: ", "R$",total)
print("Programa encerrado.")
