#MAIN
print('\nBem-vindos a loja de marmitas da Eshiley Mara Rodrigues\n', 
      '\n ----------------------- CARDÁPIO -------------------------',
      '\n |  TAMANHO  |  BIFE ACEBOLADO(BA) |  FILÉ DE FRANGO (FF) |',
      '\n |     P     |       R$16.00       |        R$15.00       |',      
      '\n |     M     |       R$18.00       |        R$17.00       |',
      '\n |     G     |       R$22.00       |        R$21.00       |',
      '\n ----------------------------------------------------------',
     )

#VARIÁVEL
preco_t = []
            
#LOOP MAIN
while True:      
      
      #LOOP PARA A CATEGORIA SABOR
      while True:

            #ENTRADA
            sabor = input('\nSabor desejado (BA/FF): ')

            #CONDIÇÃO
            if sabor == 'BA':
                  break
            elif sabor == 'FF':
                  break
            else:
                  print('Sabor inválido.Tente novamente.')
      
      #LOOP PARA A CATEGORIA TAMANHO, ASSIM, NÃO PRECISA COLOCAR O SABOR NOVAMENTE     
      while True:

            #ENTRADA
            tamanho = input('\nTamanho desejado (P/M/G): ')
            preco = 0

            #CONDIÇÃO
            if sabor == 'BA' and tamanho == 'P':
                  preco = 16
                  break
            else:
                  if sabor == 'BA' and tamanho == 'M':
                        preco = 18
                        break
                  else: 
                        if sabor == 'BA' and tamanho == 'G':
                              preco = 22
                              break

            #CONDIÇÃO
            if sabor == 'FF' and tamanho == 'P':
                  preco = 15
                  break
            else:
                  if sabor == 'FF' and tamanho == 'M':
                        preco = 17
                        break
                  else: 
                        if sabor == 'FF' and tamanho == 'G':
                              preco = 21
                              break
                        else:
                              print('Tamanho inválido. Tente novamente.')

      
      #Estética da saída
      if sabor == 'BA':
            sabor = 'Bife Acebolado'
      if sabor == 'FF':
            sabor = 'Filé de Frango'
      
      #Saída main
      print(f'Pedido: {sabor} no tamanho {tamanho}: R${preco}')
      res = input('\nDeseja pedir mais alguma coisa (S/N)? ')

      #Continuar ou não no loop priNIPAL E, ADICIONA O PREÇO A UMA LISTA PARA CÁCULAR TOTAL
      if res == 'S':
            preco_t.append(preco)
            continue
      elif res == 'N':
            preco_t.append(preco)
            soma = sum(preco_t)
            print(f'Total a pagar: R${soma}')
            break