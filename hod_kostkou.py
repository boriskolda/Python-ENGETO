# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude simulovat hod kostkou.

# Program musí obsahovat:

# Naimportuj knihovnu random,
# vytvoř proměnnou min_hodnota a ulož do ní int 1,
# vytvoř proměnnou max_hodnota a ulož do ní int 6,
# vytvoř řízenou nekonečnou smyčku,
# nejprve vypiš: "Házím kostkou..",
# vytvoř proměnnou kostka_hodnota, které bude náhodně přiřazeno int od min_hodnota do max_hodnota,
# následně doplň oznámení: "Na kostce je: <hodnota>",
# pokud kostka_hodnota bude obsahovat hodnotu 6, hod se provede znovu,
# pokud padne jiné číslo, než 6 program se ukončí.

from random import randrange

min_hodnota = 1
max_hodnota = 6

while True:
    print("Házím kostkou..")
    kostka_hodnota = randrange(min_hodnota, max_hodnota+1)
    print(f"Na kostce je: {kostka_hodnota}")
    if kostka_hodnota == 6:
        continue
    else:
        break