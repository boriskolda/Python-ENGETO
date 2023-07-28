# V této úloze vytvoř program, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu.

# Na konci by měl program vypsat absolutní hodnotu rozdílu mezi těmito součty.

# Jednotlivé kroky, které program musí obsahovat:

# Máme seznam čísel:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# cisla = [1, 2, 3, 4, 5, 6, 7, 8]
# sečteme všechna sudá čísla a výsledek uložíme do proměnné suda,
# sečteme všechna lichá čísla a výsledek uložíme do proměnné licha,
# nakonec získáme rozdíl mezi těmito dvěma součty (proměnná vysledek),
# měli bychom zajistit, že výsledek nebude záporné číslo (k tomu by ti mohly pomoci built-in funkce pro numerické typy, zmiňované v první lekci).
# Tvým ukolem je zjistit, jak iterovat každým prvkem v seznamu čísel, ne psát součet manuálně.


cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0

for cislo in cisla:
    if int(cislo) % 2 == 0:
        suda += cislo
    elif int(cislo) % 2 != 0:
        licha += cislo

vysledek = abs(suda - licha)

print(f"Rozdíl je: {vysledek}")

