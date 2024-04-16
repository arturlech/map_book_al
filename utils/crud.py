def read_friends(users: list)->None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajmomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')
