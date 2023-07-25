# V této úloze vytvoř program, který převede zadaný string na list.

# Jednotlivé kroky, které program musí obsahovat:

# Zapiš proměnnou vysledek, která obsahuje prázdný list,
# zapiš proměnnou zadana_cisla, která obsahuje datový typ str s hodnotou '1, 2, 3, 4, 5',
# rozděl hodnotu v proměnné zadana_cisla pomocí symbolu ,, výsledek ulož do proměnné cisla,
# postupně projdi hodnoty v proměnné cisla, očisti hodnoty a ulož je do proměnné vysledek,
# nakonec zobraz uložená čísla s doplňujícím textem: List:.


# Zadaná proměnná
vysledek = []
# Vstup
zadana_cisla = '1, 2, 3, 4, 5'
# Rozdělené hodnoty schované v proměnné "cisla"
cisla = zadana_cisla.split(',')
# Jednotlivé hodnoty projdi
for cislo in cisla:
    # .. očisti od mezer a ulož do proměnné "vysledek"
    ocistene_cislo = int(cislo.strip())
    vysledek.append(ocistene_cislo)
# Nakonec výsledek vypiš s doplňujícím textem "List:"
print('List:', vysledek)