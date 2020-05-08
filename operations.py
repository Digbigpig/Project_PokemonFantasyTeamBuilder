import user_interface as ui
import data_access as db

current_page = 1


def browse(pokemon_data=None, page_size=10, start=False):
    if pokemon_data is None:
        pokemon_data = db.browse()
    if start:
        ui.init_browse()
    ui.browse(pokemon_data, page_size, pokemon_data.count)


def add(pokemon):
    db.add_pokemon_to_team(pokemon.title())


def remove(pokemon):

    team = db.load_team()
    team.remove(pokemon.title())
    db.save_team(team)
    ui.view_team()


def view_team():
    return db.load_team()

