import dictionary

#Seleciona a palavra dentro do dicionário dado por dictionary.py
palavra = dictionary.sorteia()
print(palavra)
lista_palavra = []

#Define a posição de cada letra em uma lista:
for i in range(0,5):
        lista_palavra.append(palavra[i])
print(lista_palavra)



template = ["_","_","_","_","_"]
palavras_tentadas = []
tentativa = 0;

while tentativa < 2:
    
    user_input = input()
    
#Verifica se a palavra digitada é válida
    no_word = False
    ver = False
    if dictionary.existe(user_input) == False:
        print("Entrada inválida")
        no_word = True
        
    if no_word == False:
        for i in range(0,5):
            for j in range(0,5):
                if user_input[i] == palavra[j]:
                    ver = True
                    if user_input[i] == palavra[j]:
                            template[i]  = user_input[j].upper()
                    elif user_input[i] != palavra[j]:
                            template[i]  = user_input[j].lower()
                    palavras_tentadas.append(template)     
                else:
                    ver = False
        print(template)  

        
                








    if no_word == False:
            tentativa = tentativa + 1

            
    
    
        
                
        
