import json

d1 = {
    'Pessoa 1': {
        'Nome': 'Jean',
        'Idade': '30',
    },
    'Pessoa 2': {
        'Nome': 'Juliana',
        'Idade': '31',
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)