def repetir(palavra, palavra_vazia = True, repeticoes = 3):
    repeticoes = int(repeticoes)
    if palavra_vazia == "":
        while repeticoes != 0:
            print(palavra)
            repeticoes = repeticoes - 1
    else:
        while repeticoes != 0:
            print(palavra)
            print(palavra_vazia)
            repeticoes = repeticoes - 1
def main():
  p_1 = str(input())
  p_2 = str(input())
  rep = input()
  
  if rep != "":
      repetir(p_1,p_2,rep)
  if rep == "":
      repetir(p_1,p_2)
main()
