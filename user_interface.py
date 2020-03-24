from data_access import get_pokemon_data, load_team


def start():
    print("\nWelcome to the Pokemon Fantasy Team Builder!")
    print("--------------------------------------------")
    print("Use this application to browse your favorite \n"
          "pokemon and add them to your fantasy team.\n"
          "You can search for pokemon by using their \n"
          "name or Pokemon number. If you dont know any \n"
          "pokemon by name, use the browse command \n"
          "to see a paginated list.")


def help_():
    print("\nTODO: help command")


# TODO: Use this method more often.
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
    print("\n\n\nMain Menu")
    print("_________")
    print("browse - View pokemon you can add to your team.")
    print("exit - Exit the Pokemon Fantasy Team Builder")
    print("add {pokemon name or number} - You can add pokemon to your team. Use the add command followed by the name "
          "of the pokemon or the pokemons ID.")
    print("remove - To remove pokemon from your team, use the remove command followed by the pokemons position in "
          "your team. TODO:remove by name.")
    print("view team - View your team of pokemon.")


def refresh():
    pass


def add_pokemon_name():
    return input("Enter the name of the pokemon you wish to add: ")


def added_pokemon(name):
    print(f"{name} has been added to your team!")
    input("\nPress enter to continue...")


def remove_pokemon_name():
    team = load_team()
    return input(f"Enter the name of the pokemon you want to remove from your team? {team}").lower()


def view_team(team):
    if team:
        print("\n\nYour Team:")
        for index, pokemon in enumerate(team):
            print(f"{index+1}. {pokemon}")
    else:
        print("\n\nYour team is empty!")
    input("\nPress enter to continue...")


def invalid_pokemon_name():
    print("That pokemon name could not be recognized. Try again or type \"exit\" to return.")
