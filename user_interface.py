from data_access import get_pokemon_data


def start():
    print("Welcome to the Pokemon Fantasy Team Builder!")
    print("--------------------------------------------")
    print("Use this application to browse your favorite pokemon and add them to your fantasy team. You can search for "
          "pokemon by using their name or Pokemon number. If you dont know any pokemon by name, use the browse "
          "command to see a paginated list.\n")
    print("Type \"help\" to see a list of commands.")


def help_():
    print("\nTODO: help command")


def get_input(message=""):
    return input(message)


def exit_():
    print("Goodbye")


def browse(data, page, page_size, length):
    for index, pokemon in enumerate(list(data)[(page - 1) * page_size: min(page * page_size, len(data) - 1)]):
        data = get_pokemon_data(pokemon["name"])
        print(data.id, data.name.title())

    print(f"Page: {page}/{length // page_size} \n"
          f"Navigation: next - Go to next page, "
          f"prev - Go to previous page, or enter page number")


def main_menu():
    print("Main Menu")
    print("_________")
    print("browse - View pokemon you can add to your team.")
    print("exit - Exit the Pokemon Fantasy Team Builder")
    print("add {pokemon name or number} - You can add pokemon to your team. Use the add command followed by the name "
          "of the pokemon or the pokemons ID.")
    print("remove - To remove pokemon from your team, use the remove command followed by the pokemons position in "
          "your team. TODO:remove by name.")
    print("view - View your team of pokemon.")


def refresh():
    pass
