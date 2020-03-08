import pokebase as pb
import pickle


def load_team():
    with open('data/team.bin', 'rb') as file:
        team = pickle.load(file)
    return team


def browse():
    return pb.APIResourceList("pokemon")


def get_pokemon_data(name):
    return pb.pokemon(name)
