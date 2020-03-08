import user_interface as ui
import data_access as db


def start():

    team = db.load_team()
    run = True
    ui.start()

    while run:
        ui.main_menu()
        command = ui.get_input()

        if command == "exit":
            run = False
            exit_()

        elif command == "help":
            help_()

        elif command == "browse":
            browse()

        elif command == "add":
            add()

        elif command == "view team":
            view_team(command)

        elif command == "remove":
            remove(command)

        ui.refresh()


def help_():
    ui.help_()


def exit_():
    ui.exit_()


def browse():
    browsing = True
    page = 1
    page_size = 10
    pokemon = db.browse()
    ui.browse(pokemon, page, page_size, len(pokemon))

    while browsing:
        command = ui.get_input()

        if command == "exit":
            browsing = False

        elif command == "next" and 0 < page < (len(pokemon) // page_size):
            page += 1
            ui.browse(pokemon, page, page_size, len(pokemon))

        elif command == "prev" and 1 < page < (len(pokemon) // page_size):
            page -= 1
            ui.browse(pokemon, page, page_size, len(pokemon))

        else:
            try:
                page_num = int(command)
                if 0 < int(page_num) < (len(pokemon) * page_size):
                    page = page_num
                    ui.browse(pokemon, page, page_size, len(pokemon))

            except Exception as e:
                ui.browse(pokemon, page, page_size, len(pokemon))


def add(pokemon):
    pass


def view_team():
    pass


def remove(pokemon):
    pass
