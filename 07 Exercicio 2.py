#Variaveis

m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
m3 = float(input('Digite a terceira nota: '))

#Media

media_notas = (m1 + m2 + m3)/3
print(media_notas)

#Código

if media_notas >= 0.0 and media_notas <= 4.0:
    print('Reprovado')
elif media_notas >= 4.1 and media_notas <= 6.0:
    exame = float(input('Digite a nota do exame'))
    if exame >= 6.0:
        print('Aprovado')
    else:
        print('Reprovado')
else:
    print('Aprovado')