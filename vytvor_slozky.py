# Pomocí modulu os napiš takový kód, který v aktuálním umístění vytvoří tyto tři prázdné adresáře:

# obrazky,
# texty,
# gify.
# Program musí:

# Nahrát knihovnu os,
# vytvořit proměnnou jmena_slozek, kam vložíš stringy "obrazky", "texty", "gify",
# projít jednu hodnotu za druhou z proměnné jmena_slozek,
# ověřit, jestli daný string neexistuje a není adresářem,
# pokud existuje, vypsat oznámení "Složka již existuje!"
# pokud neexistuje, vytvořit složku a vypsat oznámení "Tvořím novou složku: <jmeno>".
# závěrem vypsat: "Všechny složky existují".

from os import mkdir
from os import listdir

jmena_slozek = ["obrazky", "texty", "gify"]

for jmeno in jmena_slozek:
    if jmeno not in listdir():
        mkdir(jmeno)
        print(f"Tvořím novou složku: {jmeno}")
    else:
        print("Složka již existuje!")

print("Všechny složky existují")

