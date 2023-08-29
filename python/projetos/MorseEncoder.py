#definindo a conversão
def convert_to_morse(code):
  code = code.replace('1','.---- ')
  code = code.replace('2','..--- ')
  code = code.replace('3','...-- ')
  code = code.replace('4','	....- ')
  code = code.replace('5','..... ')
  code = code.replace('6','-.... ')
  code = code.replace('7','--... ')
  code = code.replace('8','---.. ')
  code = code.replace('9','----. ')
  code = code.replace('0','----- ')
  return code

#recebendo os dados
lock_code = input(str('O que deseja converter?'))
print('Código inicial: {}'.format(lock_code))

#convertendo
morse = convert_to_morse(lock_code)
print('O seu código em morse fica: {}'.format(morse))
