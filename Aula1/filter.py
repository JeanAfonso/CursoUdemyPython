from dados import produtos, pessoas, lista

# Funcão filter cria um filtro dos dados que eu quero
# e retorna true ou false
# Pegar o numeros maiores que 5 e coloca na nova lista
# e o que for menor ela exclui da nova lista
# nova_lista = filter(lambda x: x > 5, lista)
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))


# Filtrando produtos que o preco sejam maiores que 50


def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
    return True


# novo_produto = filter(lambda p: p['preco'] > 50, produtos)
novo_produto = filter(filtra, produtos)

for produto in novo_produto:
    print(produto)

print()
# Checando se a pessoa é maior de idade

def maior_idade(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

maioridade = filter(maior_idade, pessoas)

for pesso in maioridade:
    print(pesso)