#Tratando a sequência recebida
sequencia = 'tatgctttcc#tataggtctg#ctattcaatg'
dna_list = sequencia.split('#')
print(dna_list)

#Convertendo
for dna in dna_list:
  rna = dna.replace('t','u')
  print('DNA {} -> RNA {}'.format(dna, rna))
