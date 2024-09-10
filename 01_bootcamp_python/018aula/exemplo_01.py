import requests
from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> Pokemon:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    data = response.json()

    data_types = data['types'] # Supondo que 'data' é o dicionário com os dados do Pokémon

    types_list = []

    # Tipos do pokemon
    for type_info in data_types:
        types_list.append(type_info['type']['name'])

    return Pokemon(name=data['name'], type=', '.join(types_list))


# Testes
if __name__ == "__main__":

    # Menu para escolher o Pokémon
    while True:
        try:
            id_pokemon = int(input("\nEscolha um Pokémon para ver informações:\nDigite o ID do Pokémon (Digite 0 para sair): "))

            if id_pokemon == 0:
                print("Encerrando o programa.")
                break

            pokemon = pegar_pokemon(id_pokemon)
            print(f"O nome do pokémon é {pokemon.name} e seu(s) tipo(s) {pokemon.type}")

        except ValueError:
            print("ID inválido. Digite um número inteiro/válido")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")

