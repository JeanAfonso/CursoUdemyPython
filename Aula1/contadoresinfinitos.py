from itertools import count
# count se vc nao colocar limite cria-se um laço infinito
# contador = count(start=5, step=0.1)
#
# for valor in contador:
#     print(round(valor, 2))
#
#     if valor >= 10 or valor <= -10:
#         break

contador = count()
lista = ['Jean', 'Afonso', 'Mota']
lista = zip(contador, lista)
print(list(lista))