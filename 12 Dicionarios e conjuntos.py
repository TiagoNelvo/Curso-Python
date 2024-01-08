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

for especie, num_especimes in coleta.items():
    print(f'Especie: {especie}, número de especimes coletados: {num_especimes}')

