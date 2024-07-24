def info_triangulo(altura, base, char):

    linha = 1
    spaces = altura*(" ")
    while linha <= base+2:
        if linha == 1 or linha == base+2:
            print((altura+2)*char)
        else:
            print(char + spaces + char)
        linha = linha + 1

def main():
    user_altura = int(input())
    user_base   = int(input())
    user_char   = str(input())
    info_triangulo(user_altura, user_base, user_char)

main()
    
    
