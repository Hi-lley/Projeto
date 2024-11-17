print('Bem-vindos a Fábrica de Camisetas da Eshiley Mara Rodrigues')

#FUNÇÃO
def escolha_modelo():
      #LOOP
      while True:
            
            #DICIONÁRIO
            dict_modelos = {
                  "MCS": 1.80,
                  "MLS": 2.10,
                  "MCE": 2.90,
                  "MLE": 3.20
            }
            
            #ENTRADA
            print('\nEntre com o modelo desejado (Escreva apenas a abreviação): ',
                  '\n\nCamiseta Manga Curta Simples (MCS)',
                  '\nCamiseta Manga Longa Simples (MLS)',
                  '\nCamiseta Manga Curta Com Estampa (MCE)', 
                  '\nCamiseta Manga Longa Com Estampa (MLE)',)

            modelo_cliente = input('>> ')

            #CONDIÇÃO
            if modelo_cliente in dict_modelos.keys():
                  preco_un = dict_modelos[modelo_cliente]
                  return preco_un
                  
            else:
                  print('Modelo inexistente. Tente novamente.')

#FUNÇÃO
def num_camisetas():
      #LOOP
      while True:
            try:
                  qtd_cm = int(input('Entre com a quantidade de camisetas (Máx. 20000): ')) #se nao colocar no try ele da erro
                  
                  #CONDIÇÃO
                  if 20 > qtd_cm:
                        pct_desconto = 1
                        
                        #calculo da quantidade de camisetas que terão seu valor retirado
                        desconto = qtd_cm-(qtd_cm*pct_desconto)
                        return desconto
                  
                  elif 200 > qtd_cm >= 20:
                        pct_desconto = 0.05
 
                        #calculo da quantidade de camisetas que terão seu valor retirado
                        desconto = qtd_cm-(qtd_cm*pct_desconto)
                        return desconto
                  
                  elif 2000 > qtd_cm >= 200:
                        pct_desconto = 0.07

                        #calculo da quantidade de camisetas que terão seu valor retirado
                        desconto = qtd_cm-(qtd_cm*pct_desconto)
                        return desconto
                  
                  elif 20000 >= qtd_cm >= 2000:
                        pct_desconto = 0.12
                        
                        #calculo da quantidade de camisetas que terão seu valor retirado
                        desconto = qtd_cm-(qtd_cm*pct_desconto)
                        return desconto
                  
                  elif qtd_cm > 20000 or qtd_cm > -1:
                        print('Não aceitamos pedidos nessa quantidade de camisetas.',
                              '\n\nTente novamente.')
                  
            except ValueError:
                        print('Digite somente números.')

#FUNÇÃO
def escolha_frete():
      #LOOP
      while True:
            try:  #ENTRADA
                  print('\nEscolha o frete:',
                        '\n0 - Retirar o pedido na fábrica - Sem frete',
                        '\n1 - Frete por transportadora - R$100.00',
                        '\n2 - Frete por Sedex - R$200.00')
            
      
                  frete = (int(input('>> ')))

                  #CONDIÇÃO
                  if frete == 0:
                        return 0
                  elif frete == 1:
                        return 100
                  elif frete == 2:
                        return 200
                  else:
                        print('Tente novamente.')
                        
            except ValueError:
                        print('Digite somente números.')

#começo pelo pedido do modelo, contendo dicionário
preco_un = escolha_modelo()

#atribuindo O DESCONTO DA FUNÇÃO NA VARIÁVEL
desconto = num_camisetas()

#frete
frete = escolha_frete()

#SAÍDA
print(f'Valor total: R${(preco_un*desconto)+frete}')