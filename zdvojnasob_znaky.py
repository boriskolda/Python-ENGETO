# Vytvoř uživatelskou funkci, která zdvojnásobí všechny znaky zadaného stringu.

# Program musí obsahovat tyto kroky:

# Vytvoř proměnnou vstup:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# vstup = 'Ahoj všem'
# vytvoř funkci zdvojnasob_vsechny_znaky, která bude mít jeden parametr zadani,
# vytvoř proměnnou vysledek do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.

vstup = 'Ahoj všem'

def zdvojnasob_vsechny_znaky(zadani):
    vysledek = ""
    for pismeno in zadani:
        vysledek += pismeno+pismeno
    return vysledek

print(zdvojnasob_vsechny_znaky(vstup))