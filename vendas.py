# Se for 0, fechar o programa
codig = []
name = []
quant = []
valor = []

n = 1 # Garante que entre no while
prt = 0 # Mostra qual produto deve ser mostrado no print
# Menu de seleção
while n != 0:
    n = int(input())

# Inserir os produtos
    if n == 1:
        insert = input()
        codig.append(insert.split(", ")[0])
        name.append(insert.split(", ")[1])
        quant.append(insert.split(", ")[2])
        valor.append(insert.split(", ")[3])
        # COLOCAR AQUI O PRINT
        prt += 1

    if n == 2:
        num_c = input()
        num_quant = input()

        for i in range(0, len(codig)):
            if codig[i] == num_c:
                if quant[i] == num_quant:
                    print("Disponível")
                    break
                else:
                    print("Não disponível")
                    break
            if (i + 1) == len(codig):
                print("Não tem o produto")
            
                
                
    
        
  
        
        
    
