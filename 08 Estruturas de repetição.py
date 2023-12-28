# Estruturas de Repetição

for numero in range(1, 6):
    print(numero)
    #(1, n) vai até n-1

print()    

for numero in range(5, 0, -1):
    print(numero)
    
print()

soma = 0
for numero in range(1, 6):
    soma = soma + numero
    print(soma)
print()
print(soma)

palavra = 'sorvete'
for letra in palavra:
    #print(letra)
    if letra == 'v':
        print('Achou a letra v')

for i in range(0, 5):
    print(i)
    print('___')
    for j in range(0, 3):
        print(j)
    print()