import dictionary

#Texto de boas-vindas
def boas_vindas():
    print("TERMO", end="\n \n")
    print("Regras:")
    print("* Uma palavra de 5 letras, 6 tentativas.")
    print("* Caso a palavra inserida tenha a mesma letra na mesma posição da palavra a ser adivinhada, ela aparecerá em maíusculo.")
    print("* Caso a palavra inserida tenha uma letra em comum com a palavra a ser adivinhada, mas está na posição errada, ela aparecerá em minúsculo.")
    print("* Letras podem ou não aparecer mais de uma vez. Palavras repitidas contam como posição errada.")
    print("* Letras sem correlação com a palavra a ser adivinhada são representadas por um _.", end="\n \n")
    print("Obs.: Números e caracteres especiais NÃO são aceitos!", end="\n \n")

#Pergunta ao jogador se ele quer jogar de novo
def jogar_novamente():
    print("Deseja jogar de novo? (sim: s, não: n)")
    opcao = input()
    if (opcao == "s" or opcao == "n") and len(opcao) == 1:
        if opcao == "s":
            boas_vindas()
            main()
        if opcao == "n":
            print("Obrigado por jogar!")
    else:
        print("Entrada não reconhecida. Certifique-se que você digiou com s ou com n (em minúsculo)")
        jogar_novamente()

#Texto caso o jogador seja vitorioso ou perdedor
def vitoria():
    print("Parabéns, você ganhou o jogo!")
    jogar_novamente()
def perdeu(palavracerta):
    print("Você perdeu! A palavra certa era",palavracerta)
    jogar_novamente()

#Mostra as palavras tentadas
def mostrar_tentativas(palavras_tentadas):
        for k in range(len(palavras_tentadas)):
            print(palavras_tentadas[k])

#Programa principal
def main():
    #Seleciona a palavra dentro do dicionário dado por dictionary.py
    palavra = dictionary.sorteia()
    print(palavra)

    template = [["_","_","_","_","_"]]
    palavras_tentadas = []
    tentativa = 0

    while tentativa < 6:
        print("Digite a palavra: ")
        user_word = input()
        user_input = user_word.lower()

        
    #Verifica se a palavra digitada é válida e define booleanas de controle
        invalid_word = False
        ver = False
        ganhou = False
        
        if dictionary.existe(user_input) == False:
            print("Entrada inválida")
            invalid_word = True
        if user_input.isalpha():
            invalid_word = False
        if len(user_input) < 5:
            invalid_word = True

        if invalid_word == False:
                
            for i in range(0,5):
                if user_input[i] == palavra[i]:
                    template[tentativa][i] = user_input[i].upper()

                elif user_input[i] in palavra:
                    template[tentativa][i] = user_input[i].lower()

            template.append(["_","_","_","_","_"])
            palavra_jogada = " ".join(template[tentativa])
            palavras_tentadas.append(palavra_jogada)
        
            mostrar_tentativas(palavras_tentadas)
            if user_input == palavra:
                ganhou = True

        if invalid_word == False:
                tentativa = tentativa + 1
                print("")
        if ganhou == True:
            vitoria()
            break
    if ganhou == False:
        perdeu(palavra)

boas_vindas()           
main()   
    
        
                
        
