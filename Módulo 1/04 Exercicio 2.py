tempo = float(input('Quantas horas durou a viajem?'))
velocidade = float(input('Qual a velocidade média durante a viagem?'))
distancia = tempo * velocidade
litros_usados = distancia / 12
print('O tempo gasto foi de: ', tempo, 'horas')
print('A velocidade foi de: ', velocidade, 'km/h')
print('A distância foi de: ', distancia, 'kilometros')
print('A quantidade de combustível gasta foi ', round(litros_usados,1), 'litros')