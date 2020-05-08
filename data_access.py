import pokebase as pb
import pickle

data = None
local_pokemon_cache = {}


def load_team():
    team = []

    try:
        with open('data/team.bin', 'rb') as file:
            team = list(pickle.load(file))

    except FileNotFoundError:
        with open('data/team.bin', 'wb') as file:
            pickle.dump(team, file)

    return team


def save_team(team):
    with open('data/team.bin', 'wb') as file:
        pickle.dump(team, file)


def browse():
    global data
    if not data:
        data = pb.APIResourceList("pokemon")

    return data


def get_pokemon_data(name):
    try:
        result = local_pokemon_cache[name]
    except KeyError as e:
        local_pokemon_cache[name] = pb.pokemon(name)
        result = local_pokemon_cache[name]
    except Exception as e:
        raise e

    return result


def add_pokemon_to_team(pokemon):
    team = load_team()
    team.append(pokemon)
    save_team(team)
