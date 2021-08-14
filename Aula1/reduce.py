from dados import produtos, pessoas, lista
from functools import reduce

# A função reduce serve pra "reduzir" um iterável (como uma lista) a um único valor.

soma_lista = reduce(lambda ac,, i: i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))