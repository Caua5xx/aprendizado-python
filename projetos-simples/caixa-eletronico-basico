#Simulador de Caixa Eletrônico - Versão Básica
saldo = 0

while True:

#opções
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Encerrar")

    questao = int(input(">>"))

#opção 1
    if questao == 1:
        print("Saldo atual: R$ ", saldo)
#opção 2
    elif questao == 2:
        valor = float(input("Digite o valor do depósito: "))
        if valor <= 0:
            print("Valor inválido")
        else:
            print("Depósito realizado com sucesso!")
            saldo += valor
#opção 3
    elif questao == 3:
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        else:
            print("Saldo realizado!")
            saldo -= valor    
#opção 4
    elif questao == 4:
        print("Encerrando programa...")
        break
#opção indesejada
    else:
        print("Opção inválida")
    
