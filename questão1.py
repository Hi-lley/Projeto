print('Bem-vindos a loja da Eshiley Mara Rodrigues')

#Entrada de dados do valor do pedido e quantidade de parcelas
valor_pedido = float(input('Digite o valor do pedido: R$'))
quant_parc = int(input('Digite a quantidade de parcelas: '))

#CONDIÇÃO
if 4 > quant_parc :
    juros = 1
elif 6 > quant_parc >= 4:
    juros = 1.04
elif 9 > quant_parc >= 6:
    juros = 1.08
elif 13 > quant_parc >= 9:
    juros = 1.16
else:    
    juros = 1.32

#CÁLCULO
valor_parc = (valor_pedido * juros)/quant_parc
valor_t_parc = valor_parc * quant_parc

#Saída personalizada
if juros == 1:
    print(f'O valor das parcelas é de: R${valor_parc}')
    print(f'O valor total das parcelas é de: R${valor_t_parc}')
else:
    print(f'O valor das parcelas com juros é de: R${valor_parc}')
    print(f'O valor total das parcelas com juros é de: R${valor_t_parc}')