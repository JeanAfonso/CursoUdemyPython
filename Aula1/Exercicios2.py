string = '012345678901234567890123456789012345678901234567890123456789'
n = 10
# lista = string[de i: até i + n(10)] para i no tamanho(de 0 até o tamanho(string), de n(10) em n(10)
lista = [string[i: i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(retorno)

