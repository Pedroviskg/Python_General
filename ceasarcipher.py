letras = "abcdefghijklmnopqrstuvwxyz"
def cifra(palavra, chave, codificar = True):
  lista_palavra = []
  for i in range(0,len(palavra)):
    lista_palavra.append(palavra[i])
  for j in range(0,len(palavra)):
    for k in range(0,len(letras)):
      if lista_palavra[j] == letras[k]:
        break;
    if codificar == True:
      lista_palavra[j] = letras[(k + chave) % 26]
    else:
      lista_palavra[j] = letras[(k - chave) % 26]
    
  palavra_junta = "".join(lista_palavra)
  if codificar == True:
    return print("Saída codificada:", palavra_junta)
  else:
    return print("Saída decodificada:", palavra_junta)

def main():
  palavra_codificar   = str(input())
  palavra_decodificar = str(input())
  chave_escolhida     = int(input())

  if palavra_codificar != "":
    cifra(palavra_codificar, chave_escolhida, codificar = True)
  if palavra_decodificar != "":
    cifra(palavra_decodificar, chave_escolhida, codificar = False)

main()


