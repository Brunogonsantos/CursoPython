acumulador = 0
print('Bem vindo a Lanchonete do Bruno G Santos')

print('      **********Cardápio**********')
print('| Código |      Descrição          | Valor |')
print('|  100   |   Cachorro Quente       |  9,00 |')
print('|  101   |   Cachorro Quente Duplo | 11,00 |')
print('|  102   |       X-Egg             | 12,00 |')
print('|  103   |      X-Salada           | 12,00 |')
print('|  104   |      X-Bacon            | 14,00 |')
print('|  105   |      X-Tudo             | 17,00 |')
print('|  200   |    Refrigerante Lata    |  5,00 |')
print('|  201   |      Chá Gelado         |  4,00 |')

while True:
  codigo = input("Entre com código do produto:")
  if codigo == '100':
    acumulador = acumulador + 9
  elif codigo == '101':
    acumulador = acumulador + 11
  elif codigo == '102':
    acumulador = acumulador + 12
  elif codigo == '103':
    acumulador = acumulador + 12
  elif codigo == '104':
    acumulador = acumulador + 14
  elif codigo == '105':
    acumulador = acumulador + 17
  elif codigo == '200':
    acumulador = acumulador + 5
  elif codigo == '201':
    acumulador = acumulador + 4
  else:
    print('Código inválido')
    continue
  resposta = input('Deseja continuar? (s/n)')
  if resposta == 's':
    continue
  else:
    print('Total a ser pago é : {:.2f}' .format(acumulador))
    break