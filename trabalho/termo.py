import dictionary


palavra = dictionary.sorteia()
print(palavra)
ver = False


template = ["_","_","_","_","_"]
tentativa = 0;

while tentativa < 6:
    
    user_input = input()
    for i in range(0,5):
        for j in range(0,5):
            if user_input[i] == palavra[j]:
                ver = True
    if ver == True:
        print("existe uma letra nessa palavra")
    else:
        print("não existe uma letra nessa palavra")
        
                
        
