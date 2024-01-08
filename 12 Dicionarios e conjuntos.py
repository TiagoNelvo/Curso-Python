#Dicionários
coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}

coleta['Aedes aegypt']

coleta['Rhodnius montenegrensis'] = 11

print(coleta)

del(coleta)['Aedes albopictus']
print(coleta)

coleta.items()

coleta.keys()

coleta.values()

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

coleta.items()

print('---')

for especie, num_especimes in coleta.items():
    print(f'Especie: {especie}, número de especimes coletados: {num_especimes}')

print('---')

#Conjuntos(set)

biomoleculas = ('proteína', 'acidos nucleicos', 'carboidrato', 'lipideo', 'acidos nucleicos', 'carboidrato', 'carboidrato','carboidrato')
 
print(biomoleculas)

print(set(biomoleculas))
print('---')

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)

print(c3)

c1.difference(c2)
c2.difference(c1)