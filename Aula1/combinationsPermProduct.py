# Combinations, Permutations e Product - itertools
# Combinaçao - Ordem não importa
# Permutação - Ordem importa
# Ambos não repetem valores unicos
# Produto - Ordem importa e repete valores unicos


from itertools import combinations, permutations, product

person = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for group in combinations(person, 2):
    print(group)

for group in permutations(person, 2):
      print(group)

for group in product(person, repeat=2):
     print(group)