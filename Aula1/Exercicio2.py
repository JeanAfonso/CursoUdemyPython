cart = [('Produto 1', 20), ('Produto 2', 30), ('Produto 3', 50)]

# total = soma([flutuante de valor(y) para chave(x), valor(y) no carrinho])
total = sum([float(y) for x, y in cart])

print(total)