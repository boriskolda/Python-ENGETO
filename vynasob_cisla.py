
# Vytvoř tyto dvě proměnné:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# prvni_cislo = 5
# druhe_cislo = 5
# vytvoř funkci vynasob, která bude mít 2 parametry num1 a num2,
# vytvoř proměnnou vysledek, do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.

prvni_cislo = 5
druhe_cislo = 5

def vynasob(num1, num2):
    vysledek = num1 * num2
    return vysledek

print(f"Vysledek je: {vynasob(prvni_cislo, druhe_cislo)}")

