# Tuplas

tupla = ('Homo Sapiens', 'Canis familiaris', 'Felis Catus')

print(tupla[0])
#retorna a a informação correspondente a posição
print('---')

print(tupla.index('Canis familiaris'))

print('---')

for elemento in tupla:
    print(elemento)
print('---')

# Listas
l1 = ['Homo Sapiens', 'Canis familiaris', 'Felis Catus']
l2 = [' Xenopus laevis', 'Ailupoda melanoleuca']

l3 = l1 + l2
print(l3)
print('---')

l2_2 = l2 * 2
print(l2_2)
print('---')

#adiciona na lista
l1[0:2]
l1.append('Gorila gorila')
print(l1)
print('---')

#retira da lista
l1.remove('Felis Catus')
print(l1)
print('---')


