# Usando o For
#variaveis
nota = media = soma = 0

#Código
for _ in range(1, 6):
    nota = float(input('Digite a nota: '))
    soma += nota
    media = soma / 5
print('A média é: ', media)
print('---')

# Usando o While
#variaveis
nota = media = soma = 0
numero = 1

#Código
while numero <= 5:
    nota = float(input('Digite a nota: '))
    soma += nota
    numero += 1
    media = soma / 5
print('A media é: ', media)
print('---')
