import pokebase as pb
import pickle


def load_team():
    with open('data/team.bin', 'rb') as file:
        team = list(pickle.load(file))
    return team


def save_team(team):
    with open('data/team.bin', 'wb') as file:
        pickle.dump(team, file)



def browse():
    return pb.APIResourceList("pokemon")


def get_pokemon_data(name):
    try:
        data = pb.pokemon(name)

    except Exception as e:
        return False

    return data


def add_pokemon_to_team(pokemon):
    team = load_team()
    team.append(pokemon)
    save_team(team)
