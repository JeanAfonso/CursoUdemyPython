from dados import produtos, pessoas, lista


# funcao map vs uso de list comprehension
# # nova_lista = map(lambda x: x * 2, lista)
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))

# Criacão de função para aumentar os preços dos produtos
# da minha lista produtos.

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


# A funcão map percorre toda a lista e usa a funcao de aumento de preço
# e modificou todos os precos.
# precos = map(lambda p: p['preco'], produtos)
novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)


# Usando map e lambda em lista de pessoas para
# acessar o dado que eu quero

def aumenta_idade(pe):
    pe['nova_idade'] = round(pe['idade'] * 1.20)
    return pe


# nomes = map(lambda p: p['idade'] * 1.20, pessoas)
nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
