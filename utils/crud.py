def read_friends(users: list)->None:
    print("Informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajmomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbę postów użytkownika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow,}
    lista.append(new_user)

def search_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            print(user)
