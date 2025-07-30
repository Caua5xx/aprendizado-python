# Contador de Vogais
while True:
    vogais = 0

    # Solicita uma palavra ou frase ao usuário
    print("Digite uma palavra ou frase, e direi quantas vogais tem.")
    palavra = input(">> ")

    # Conta quantas vogais (com e sem assento) possuem na entrada
    for letra in palavra:
        if letra.lower() in "aeiouáãàâèéêìíóõôòúùû":
            vogais += 1
    
    # Exibe o total de vogais encontradas
    print("A sua palavra/frase contém:", vogais, "vogais")
    print("")
    
    # Pergunta ao usuário se desejar continuar
    while True:
        print("Deseja continuar? (sim/nao)")
        continuar = input(">> ").strip().lower()
    
        if continuar == "sim":
            print("")
            break # Sai do loop de confirmação e reinicia o programa
        elif continuar == "não" or continuar == "nao":
            print("")
            print("Encerrando programa...")
            exit() # Encerra o programa completamente
        else:
            print("")
            print("Desculpa, não entedi.")
            print("")
  
