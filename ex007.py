# @author: lucvsbraga

aux = int(input('Número de notas que serão avaliadas: '))
notas = []
for i in range(aux):
    notas.append(float(input(f'Digite uma nota {i+1}: ')))

media = sum(notas) / len(notas)

print(f'Média: {media}')
