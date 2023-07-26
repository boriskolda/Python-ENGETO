# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude napsat hru kámen, nůžky, papír.

# Program musí obsahovat:

# Naimportuj modul random,
# vytvoř list moznosti s hodnotami 'kamen', 'nuzky', 'papir',
# vytvoř proměnnou hrac a ulož do ní hodnotu "kamen",
# vytvoř proměnnou pocitac, které bude náhodně přiřazen prvek z listu moznosti
# pokud hráč vyhraje, vypiš "Vyhrál jsi!", pokud prohraje, vypíš "Prohrál jsi:(", v případě remízy vytiskni "Nerozhodně".

from random import choice

moznosti = ["kamen", "nuzky", "papir"]

hrac = "kamen"

pocitac = choice(moznosti)

print(f"Hráč: {hrac}")
print(f"Počítač: {pocitac}")

if hrac == "kamen" and pocitac == "kamen":
    print("Nerozhodně")
elif hrac == "kamen" and pocitac == "papir":
    print("Prohrál jsi :(")
else:
    print("Vyhrál jsi!")

