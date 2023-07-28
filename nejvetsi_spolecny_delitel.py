# NSD (GCD v angličtině) je zkratka pro největší společný dělitel (greatest common divisor).

# Tvým úkolem je vytvořit funkci najdi_gcd, která spočítá největší společný dělitel dvou celých čísel (int).

# Zadaná čísla jsou 12 a 16.

# Pomůcka, jak spočítat největší společný dělitel:

# hledáš největší společný dělitel pro čísla 12 a 16,
# nejprve použiješ modulo, abys zjistil zbytek 12 % 16, tedy 12,
# nyní vezmeš jako první číslo 16, tedy 16 % 12, kdy 12 představuje zbytek po prvním dělení. Zbytek po dělení 4,
# třetí krok se v podstatě opakuje, vezmu předchozí druhou hodnotu a zbytek po dělení, tedy 12 % 4, nyní je však zbytek 0, takže hledání je u konce,
# největší společný dělitel pro čísla 12 a 16 je 4.
# Jednotlivé kroky, které program musí obsahovat:

# Ulož zadaná čísla do proměnných:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# prvni_cislo = 12
# druhe_cislo = 16
# vytvoř uživatelskou funkci najdi_gcd s parametry x1, x2,
# najdi největšího společného dělitele a ulož jej do proměnné vysledek,
# vypiš obsah proměnné vysledek.

prvni_cislo = 15
druhe_cislo = 18

def najdi_gcd(x1, x2):
    
    while x2 > 1:
        nejvetsi_zbytek = x1 % x2

        if not nejvetsi_zbytek:
            break
        x1, x2 = x2, nejvetsi_zbytek
    
    return x2

vysledek = najdi_gcd(prvni_cislo, druhe_cislo)

print(vysledek)
