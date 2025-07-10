#Lista de compras

#Itens e Quantidades
lista_item = []
lista_quantidade = []

#Repetição
while True:

#Lista de compra    
    print("=== Lista de Compras ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")

    questao = int(input(">> "))

    #Se resposta for "1"    
    if questao == 1:
        item = input("Qual item deseja adicionar? ")
        lista_item.append(item)
        quantidade = input("Qual a quantidade? ")
        lista_quantidade.append(quantidade)
        print("")

    #Se resposta for "2"
    elif questao == 2:
        item = input("Qual item deseja remover? ")
        lista_item.remove(item)
        quantidade = input("Qual quantidade deseja remover? ")
        lista_quantidade.remove(quantidade)
        print("")
    
    #Se resposta for "3"
    elif questao == 3:
        print("")
        i = 0
        while i < len(lista_item):
            print(lista_quantidade[i], "-", lista_item[i])
            i += 1
        print("")
    
    #Se resposta for "3"
    elif questao == 4:
        print("")
        print("Encerrando...")
        print("")
        break
    
    #Se resposta não for nenhuma anterior
    else:
        print("Valor inválido!")
        questao2 = input("Deseja continuar?(sim/nao) ")
        if questao2 == "sim" or questao2 == "Sim":
            print("=== Lista de Compras ===")
            print("1 - Adicionar item")
            print("2 - Remover item")
            print("3 - Ver lista")
            print("4 - Sair")
            questao = int(input(">> "))
        else:
            break
            
