#Revisão 1.5.
#Lista de Compras

lista = []

while True:
    #Opções da lista
    print("----------------- Lista de Compras -----------------")
    print("1 - Adicione um item")
    print("2 - Remova um item")
    print("3 - Veja os itens")
    print("4 - Sair")
    numero = input(">> ").strip()
    
    #Opção 1
    if numero == "1":
        print("")
        print("Qual item deseja adicionar?")
        item = input(">> ").strip().lower()
        #verificar se item está na lista
        if item in lista:
            print("Item já está na lista!")
            print("")
        else:
            lista.append(item)
            print(f"{item} foi adicionado à sua lista com sucesso!")
            print("")
        #adicionar outro item
        while True:
            print("Adicionar outro? (sim ou não)")
            confirmacao = input(">> ").strip().lower()
            #se for adicionar outro item
            if confirmacao == "sim":
                print("")
                print("Qual item deseja adicionar?")
                item = input(">> ").strip().lower()
                #verificar se item já está na lista
                if item in lista:
                    print("Item já está na lista!")
                    print("")
                else:
                    lista.append(item)
                    print(f"{item} adicionado à sua lista com sucesso!")
                    print("")
            #se não for adicionar outro item
            elif confirmacao == "nao" or confirmacao == "não":
                print("")
                break
            #se a saida for indesejada
            else:
                print("")
                print(f"'{confirmacao}' não é uma opção!")
    #Opção 2
    elif numero == "2":
        #verificar se tem algo na lista
        if lista:
            print("")
            print("Qual item deseja remover?")
            lista.sort()
            for i in lista:
                print(i)
            item = input(">> ").strip().lower()
            #verificar se o item está na lista
            if item in lista:
                print("")
                print(f"Tem certeza que deseja remover {item} da sua lista?")
                confirmacao = input(">> ").strip().lower()
                if confirmacao == "sim":
                    lista.remove(item)
                    print("Item removido!")
                    print("")
                elif confirmacao == "não" or confirmacao == "nao":
                    print(f"{item} não foi removido!")
                    print("")
                else:
                    print("Confirmação inválida!")
                    print("")
            else:
                print("Item não encontrado!")
                print("")
        #se não tiver nada na lista
        else:
            print("A lista está vazia!")
            print("")
    #Opção 3
    elif numero == "3":
        #verificar se tem algo na lista, organizar e imprimir
        if lista:
            lista.sort()
            print("")
            print("---------- Itens Na Lista ----------")
            for i in lista:
                print(i)
            print("")
        #se não tiver item na lista
        else:
            print("Não há itens na lista!")
            print("")
    #Opção 4
    elif numero == "4":
        #confirmacao de saída
        while True:
            print("")
            print("Tem certeza que deseja sair?")
            confirmacao = input(">> ").strip().lower()
            if confirmacao == "sim":
                exit()
            elif confirmacao == "não" or confirmacao == "nao":
                print("")
                break
            else:
                print(f"'{confirmacao}' não é uma opção!")
                print("")
    #Se a opção não existir
    else:
        print("Número desconhecido!")
        print("")


