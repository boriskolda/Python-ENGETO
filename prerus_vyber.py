# V této úloze vytvoř program, který uživateli umožní vybrat ze zadaných hodnot. Pokud zapíše cokoliv jiného, program jej upozorní a nechá jej vybírat tak dlouho, dokud nezadá validní hodnotu.

# Jednotlivé kroky, které program musí obsahovat:

# Definovat objekt ovoce, který obsahuje unikátní stringy "jablko", "banan", "citron", "pomeranc",
# vypsat uživateli všechno uložené ovoce v proměnné ovoce spojené znaky ", ",
# vybrat si ovoce z nabídky pomocí funkce input do proměnné vyber s ohlášením "VYBER Z DOSTUPNÉHO OVOCE:",
# pokud si uživatel nevybere z nabídky, vypsat: "Ovoce není v nabídce." a nechat jej vybírat tak dlouho, pokud nezadá jeden ze stringů v proměnné ovoce,
# pokud si uživatel vybere jednu z možností v ovoce, potom program vypíše "Bezva, toto ovoce je v nabídce.".
# Ukázka průběhu:

ovoce = {"jablko", "banan", "citron", "pomeranc"}

print("Dostupné ovoce:", ", ".join(ovoce))


while True:
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE:")
    if vyber in ovoce:
        print("Bezva, toto ovoce je v nabídce")
        break
    else:
        print("Ovoce není v nabídce")
        