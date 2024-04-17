selector = 1
num_soda = 0
num_juice = 0
num_hamsimples = 0
num_hamduplo = 0
num_fries = 0
## Ler bebidas, valor total, lucro obtido (30% do valor total)
## Houve batatas vendidas? Qual hamburguer foi mais vendido

# Lê o que foi pedido
while selector != 0:
    pedido = int(input())
    match pedido:
        case 1:
            num_soda = num_soda + 1
        case 2:
            num_juice = num_juice + 1
        case 3:
            num_hamsimples = num_hamsimples + 1
        case 4:
            num_hamduplo = num_hamduplo + 1
        case 5:
            num_fries = num_fries + 1
        case 0:
            selector = 0

## Variáveis auxiliadoras e verificadoras
soda_sold = num_soda * 5
juice_sold = num_juice * 8.5
ham_sold = num_hamsimples * 25.80
hamduplo_sold = num_hamduplo * 28.40
fries_sold = num_fries * 15.00

total_value = soda_sold + juice_sold + ham_sold + hamduplo_sold + fries_sold
profit = (total_value * 0.3)

if num_fries != 0:
    was_fries_sold = 'Sim'
else:
    was_fries_sold = 'Não'


if num_hamsimples > num_hamduplo:
    most_ham_sold = 'Simples'
if num_hamduplo > num_hamsimples:
    most_ham_sold = 'Duplo'
if num_hamsimples == num_hamduplo and (num_hamsimples + num_hamduplo) != 0:
    most_ham_sold = 'Empate'
if num_hamsimples == 0 and num_hamduplo == 0:
    most_ham_sold = 'Nenhum'
## Fim das variáveis e início das "printagens"

print('- Relatório da Venda -')
print('Quantidade de bebidas vendidas: %i' % (num_soda + num_juice))
print('Valor total: R$ %.2f' % (total_value))
print('Lucro obtido: R$ %.2f' % (profit))
print('Batatas fritas vendidas? %s' % (was_fries_sold))
print('Hambúrguer mais vendido: %s' % (most_ham_sold))




            
