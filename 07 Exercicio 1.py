n = int(input('Digite a idade da criança'))

if n >= 0 and n <= 12:
    print('Criança')
elif n > 12 and n <= 17:
    print('Adolescente')
elif n >= 18:
    print('Adulto')