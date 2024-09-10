import requests

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/1')
data = response.json()

data_types = data['types'] # Supondo que 'data' é o dicionário com os dados do Pokémon

types_list = []

# Tipos do pokemon
for type_info in data_types:
    types_list.append(type_info['type']['name'])

# Nome do pokemon
print(f"Nome do Pokémon: {data['name']}")
print(f"Tipos do Pokémon: {', '.join(types_list)}")