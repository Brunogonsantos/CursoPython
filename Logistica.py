#********** Começo da Função dimensoesObjeto ***********
def dimensoesObjeto():
    while True:
        try:
          larg = float(input('Qual largura do Objeto (cm):'))
          compri = float(input('Qual comprimento do Ojeto (cm):'))
          alt = float(input('Qual altura do Objeto em (cm):'))
          dimE = alt * compri * larg
          if 0 <= dimE < 1000:
            return 10
          elif 1000 <= dimE < 10000:
            return 20
          elif 10000 <= dimE < 30000:
            return 30
          elif 30000 <= dimE < 100000:
            return 50
          else:
            print('Valor não aceito')
            continue
        except ValueError:
          print('Pare de digitar valores não numéricos. Tente novamente')
          continue
#********** Fim da Função dimensoesObjeto **********
#********** Começo da Função pesoObjeto ***********
def pesoObjeto():
  while True:
    try:
      peso = float(input('Qual peso do Objeto?'))
      if peso <= 0.1:
       return 1
      elif 0.1 <= peso < 1:
        return 1.5
      elif 1 <= peso < 10:
         return 2
      elif 10 <= peso < 30:
          return 3
      else:
        print('Valor inválido')
    except ValueError:
      print('Pare de digitar valores não numéricos. Tente novamente')
      continue
#********** Fim da Função pesoObjeto **********
#********** Começo da Função rotaObjeto ********

def rotaObjeto():
  print('SR - De São Paulo até Rio de Janeiro')
  print('BS - De Brasília até São Paulo')
  print('RS - De Rio de Janeiro até São Paulo')
  print('SB - De São Paulo até Brasília')
  print('BR - De Brasília até Rio de Janeiro')
  print('RB - Rio de Janeiro até Brasília')
  rota = input('Qual rota desejada?')
  if rota == 'SR':
    return  1
  elif rota == 'BS':
    return  1
  elif rota == 'RS':
    return 1.2
  elif rota == 'SB':
    return 1.2
  elif rota == 'BR':
    return 1.5
  elif rota == 'RB':
    return 1.5
  else:
    print('Rota inválida!')


#********** Fim da Função rotaObjeto **********
#********** Começo da Main**********
print('Bem Vindo a Companhia de Logistica Bruno Gonçalves dos Santos S.A')
dimen = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimen * peso * rota
print ('O Valor Total a pagar: R$ {:.2f}'.format(total))


#********** Fim da Main**********
