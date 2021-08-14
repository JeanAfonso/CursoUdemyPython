# Tratamento de exceções
# Pode se fazer try e except dentro de try e except tbm

try:
    a = 1/0
except NameError as erro:
    print('Erro do Desenvolvedor, fale com ele')
except (IndexError, KeyError) as erro:
    print('Erro de Indice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    a = None

print(a)