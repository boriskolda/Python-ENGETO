# V této úloze vytvoř program, který potřebuje od uživatele start, stop a delitel.

# Po zapracování vypíše všechna celá čísla v intervalu od start, do stop, která jsou dělitelná hodnotou v delitel.

# Jednotlivé kroky, které program musí obsahovat:

# Vytvoř tyto proměnné:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# vysledek = list()
# start = 3
# stop = 9
# delitel = 3
# ověří jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance),
# pokud jsou int, vypiš oznámení dle ukázky níž,
# pokud alespoň jeden není int, vypiš oznámení dle ukázky níž a ukonči skript,
# jestli jsou jednotlivé hodnoty z intervalu dělitelné hodnotou v proměnné delitel, potom je přidej do zadaného seznamu vysledek,
# po skončení iterace všech hodnot vypiš výsledné hodnoty podle vzoru níže.

vysledek = list()
start = 3
stop = 9
delitel = 3

if not isinstance(start,int) or not isinstance(stop, int) or not isinstance(delitel, int):
    print("Zadané vstupy musí být čísla.")

else:
    for cislo in range(start, stop+1):
        if cislo % delitel == 0:
            vysledek.append(cislo)
            
    print(f"Zadaný rozsah: <{start}, {stop}>")
    print(f"Čísla dělitelná {delitel}: {vysledek}")
