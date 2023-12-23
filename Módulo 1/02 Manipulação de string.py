a = 'casaco'
print(a)

#Maíusculo

maiuscula = a.upper()
print(maiuscula)

#minuscula

minuscula = maiuscula.lower()
print(minuscula)

#Primeira letra Maíuscula

capital = a.capitalize()
print(capital)

#Metade da palavra em maiusculo

metade_palavra = a[0:4]
print(metade_palavra)
# [0:3] parte da posição 0 indo até a 3

metade_palavra2 = a[3:]
print(metade_palavra2)
#[3:] a variavel parte da 3 posição ou terceira letra

#substituição dentro da variavel

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('o', 'a')
print(c)

#Pesquisa a posição da letra na variável

c1 = c.find('s')
print(c1)
#2
c2 = c.find('a')
print(c2)
#1
#find para letra q n existe na palavra
c3 = c.find('b')
print(c3)

#Contar o tamanho do texto presente na variavel
e = ' casaco '
print(len(e))

#remover os espaços antes e depois
f = e.strip()
print(f)
print(len(f))

#Concatenação
n1 = 13
n2 = 16
print('Dividindo {n1} por {n2} o resultado é {n1/n2}')
#inserindo o f(formatação), passa a exibir os valores ao invés das variaveis
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')