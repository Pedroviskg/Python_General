inicial = input()
final = input()
soma = 0

try:
    inicial = int(inicial)
    final   = int(final)
except:
    print('Entrada inválida')
else:
    menor = int(inicial)
    maior = int(final)
    if final < inicial:
        maior = inicial
        menor = final
    for i in range(menor, maior + 1):
        soma = soma + i
        
    if (menor + maior) % 2 == 0:
        mediana = int((menor + maior)/2)
        print('Início do intervalo:',inicial)
        print('Fim do intervalor:', final)
        print('Somatório do intervalo:',soma)
        print('Metade do intervalo:',mediana)
    else:
        mediana_1 = int((menor + maior)/2 - 0.5)
        mediana_2 = int((menor + maior)/2 + 0.5)
        print('Início do intervalo:',inicial)
        print('Fim do intervalor:', final)
        print('Somatório do intervalo:', soma)
        print('Metade do intervalo:' ,mediana_1,'e',mediana_2)
