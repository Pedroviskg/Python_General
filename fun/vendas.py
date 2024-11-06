# Listas vazias
key   = []
name  = []
quant = []
price = []

#Definindo o preço inicial como 0
sold  = 0

n = 1   # Garante que entre no while

# Menu de seleção
while n != 0:
    n = int(input())

# Inserir os produtos
    if n == 1:
        insert = input()
        key.append(insert.split(", ")[0])
        name.append(insert.split(", ")[1])
        quant.append(insert.split(", ")[2])
        price.append(insert.split(", ")[3])
        
# Verificador de compra
    if n == 2:
        insert = input()
        num_key = insert.split(", ")[0]
        num_quant = insert.split(", ")[1]

        for i in range(0, len(key)):
            if key[i] == num_key:
                q_convert_to_int = int(quant[i])
                n_convert_to_int = int(num_quant)
                if q_convert_to_int >= n_convert_to_int:
                    total = float(price[i]) * float(num_quant)
                    print("VALOR DA COMPRA: R$ %.2f" % (total))
                    sold += total
                    quant[i] = int(quant[i]) - int(num_quant)
                    if quant[i] == 0:
                        del quant[i]
                        del name[i]
                        del price[i]
                        del key[i]
                    break
                else:
                    print("Quantidade insuficiente")
                    break
            if (i + 1) == len(key):
                print("Produto inválido")
                
# Exibe o item                
    if n == 3:
        for i in range(0, len(key)):
            c_price = float(price[i])
            print("ID: %s, NOME: %s, QUANTIDADE: %s, VALOR: R$ %.2f" % (key[i], name[i], quant[i], c_price))
            
print("TOTAL VENDIDO: R$ %.2f" % (sold))
                

                
            
                
                
    
        
  
        
        
    
