from functools import partial
import operations
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Fantasy Team Builder ")

current_page = 1
current_length = 255
current_page_size = 10
button_list = []

main_text = tk.Text(root)
bottom_bar = tk.Frame(root, height="20")

main_frame = tk.Frame(root, height="300", width="300")
main_frame.columnconfigure(0, weight=1)

Can1 = tk.Canvas(main_frame, bg="Yellow")
F2 = tk.Frame(Can1, bg="Blue", bd=2, relief=tk.GROOVE)

vsbar = tk.Scrollbar(main_frame, orient="vertical", command=Can1.yview)

next_button = tk.Button(bottom_bar, text="Next", command=lambda: browse_next())
prev_button = tk.Button(bottom_bar, text="Prev", command=lambda: browse_previous())

browse_text_variable = tk.StringVar()
browse_text = tk.Label(root, height="5", textvariable=browse_text_variable)


def start():
    welcome_text = """\nWelcome to the Pokemon Fantasy Team Builder!
--------------------------------------------
Use this application to browse your favorite 
pokemon and add them to your fantasy team.
you can search for pokemon by using their 
name or Pokemon number. If you dont know any 
pokemon by name, use the browse command 
to see a paginated list."""
    print(welcome_text)

    # Welcome Text
    main_text.pack(fill=tk.X, expand=tk.YES, side=tk.TOP)
    main_text.insert(tk.END, welcome_text)

    bottom_bar.pack()

    browse_button = tk.Button(bottom_bar, text="Browse Pokemon", command=lambda: operations.browse(start=True))
    view_team_button = tk.Button(bottom_bar, text="View Team", command=view_team)
    browse_button.pack(in_=bottom_bar, side=tk.LEFT)
    view_team_button.pack(in_=bottom_bar, side=tk.LEFT)

    root.mainloop()


def init_browse():
    main_text.destroy()

    browse_text.pack(fill=tk.X, side=tk.TOP)
    browse_text_variable.set("Click on a pokemon to add them to your team.\n Click next to continue to the next page.\n")

    Can1.grid(row=3, column=0, sticky=(tk.N, tk.W))

    F2.grid(row=0, column=0, sticky=(tk.N, tk.W))
    vsbar.grid(row=3, column=1)
    Can1.configure(yscrollcommand=vsbar.set, scrollregion=Can1.bbox("all"))

    next_button.pack(in_=bottom_bar, side=tk.RIGHT)
    prev_button.pack(in_=bottom_bar, side=tk.LEFT)


def browse(data, page_size, length, page=None):
    global current_page, button_list, current_length
    current_length = length

    if page is None:
        page = current_page

    for button in button_list:
        button.destroy()
    button_list = []

    i = 0
    for index, pokemon in enumerate(list(data)[(page - 1) * page_size: min(page * page_size, len(data) - 1)]):
        button = tk.Button(F2, height="2", anchor="w", command=partial(add_pokemon_name, pokemon["name"]), text=f"{((page-1)*page_size)+index+1}. {pokemon['name'].title()}")
        button.pack(fill=tk.X, expand=tk.YES, side=tk.TOP)
        button_list.append(button)
        i += 1

    main_frame.pack(side=tk.TOP)

    print(f"Page: {page}/{length // page_size} \n"
          f"Navigation: next - Go to next page, "
          f"prev - Go to previous page, or enter page number")


def browse_next():
    global current_page
    global current_length
    global current_page_size

    if 0 < current_page < (current_length // current_page_size):
        current_page+=1
    operations.browse()


def browse_previous():
    global current_page
    global current_length
    global current_pagesize

    if 1 < current_page <= (current_length // current_page_size):
        current_page -= 1
    operations.browse()


def add_pokemon_name(pokemon):
    try:
        operations.add(pokemon)
    except:
        raise Exception("Could not add pokemon to team")

    browse_text_variable.set(f"{pokemon.title()} has been added to your team")


def remove_pokemon_name(name):
    operations.remove(name)


def view_team():
    global button_list
    team = operations.view_team()

    # clear ui
    for button in button_list:
        button.destroy()
    button_list = []

    # Create new buttons
    Can1.grid(row=3, column=0, sticky=(tk.N, tk.W))

    F2.grid(row=0, column=0, sticky=(tk.N, tk.W))
    # vsbar.grid(row=3, column=1)
    Can1.configure(yscrollcommand=vsbar.set, scrollregion=Can1.bbox("all"))
    for index, member in enumerate(team):
        button = tk.Button(F2, height="2", anchor="w", command=partial(remove_pokemon_name, member),
                           text=f"{index+1}. {member.title()}")
        button.pack(fill=tk.X, expand=tk.YES, side=tk.TOP)
        button_list.append(button)

    # New labels
    browse_text.pack(fill=tk.X, side=tk.TOP)
    browse_text_variable.set(f"Click on a Pokemon to remove them from your team."
                             f"")
    main_text.destroy()
    # Remove from team functionality

    main_frame.pack(side=tk.TOP)


def invalid_pokemon_name():
    print("That pokemon name could not be recognized. Try again or type \"exit\" to return.")
