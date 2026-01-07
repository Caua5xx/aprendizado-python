#Revisão 1.5.
#Lista de Compras

lista = []

def mostrar_lista():
    print("")
    print("---------- Itens Na Lista ----------")
    lista.sort()
    for i in lista:
        print(i)

def lista_com_item():
    if not lista:
        print("Não há itens na lista!\n")
        return False
    return True

def adicionar_item():
    print("Qual item deseja adicionar?")
    item = input(">> ").strip().lower()
    if item in lista:
        print("Item já está na lista!")
        print("")
    else:
        lista.append(item)
        print(f"{item} foi adicionado à sua lista com sucesso!")
        print("")

def confirmar():
    while True:
        confirmacao = input(">> ").strip().lower()
        if confirmacao in ("sim", "s"):
            return True
        elif confirmacao in ("nao", "não", "n"):
            return False
        else:
            print("Resposta inválida! (digite sim ou não)")

while True:
    print("----------------- Lista de Compras -----------------")
    print("1 - Adicione um item")
    print("2 - Remova um item")
    print("3 - Veja os itens")
    print("4 - Sair")
    numero = input(">> ").strip()
    
    #Opção 1
    if numero == "1":
        print("")
        adicionar_item()
        while True:
            print("Adicionar outro? (sim ou não)")
            if confirmar():
                print("")
                adicionar_item()
            else:
                print("")
                break
    #Opção 2
    elif numero == "2":
        if lista_com_item():
            mostrar_lista()
            print("Qual item deseja remover?")
            item = input(">> ").strip().lower()
            if item in lista:
                print("")
                print(f"Tem certeza que deseja remover {item} da sua lista?")
                if confirmar():
                    lista.remove(item)
                    print("Item removido!")
                else:
                    print(f"{item} não foi removido!")
            else:
                print("Item não encontrado!")
        else:
            continue
        print("")
    #Opção 3
    elif numero == "3":
        if lista_com_item():
            mostrar_lista()
            print("")
        else:
            continue
    #Opção 4
    elif numero == "4":
        while True:
            print("")
            print("Tem certeza que deseja sair?")
            if confirmar():
                exit()
            else:
                print("")
                break
    else:
        print("Número desconhecido!")
        print("")


