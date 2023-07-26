# V této úloze vytvoř program, který seřadí abecedně zadaný seznam jmena.

# poznámka. bez použití funkce sorted nebo metody seznamů sort .

# Jednotlivé kroky, které program musí obsahovat:

# Vytvo proměnnou jmena, která je dat. typ list a obsahuje:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# jmena = [
#  'Michal', 'Pepa', 'Honza',
#  'Pavel', 'Lukas', 'Matej',
#  'Iva', 'Klara', 'Jana',
#  'Honza', 'Vasek','Milan',
#  'Michal'
# ]
# vytvoř kopii proměnné jmena, do proměnné kopie_jmen,
# iteruj přes zadaný seznam jmena,
# vytvoř vnitřní (nestovanou) smyčku, která bude sledovat hodnotu indexu o jedna vyšší než aktuální hodota indexu z první smyčky,
# pokud je hodnota v listu na indexu z první smyčky vyšší než hodnota na indexu druhé smyčky, aktualizuj pořadí hodnot v listu,
# vypiš seřazenou podobu seznamu jmena

jmena = [
 'Michal', 'Pepa', 'Honza',
 'Pavel', 'Lukas', 'Matej',
 'Iva', 'Klara', 'Jana',
 'Honza', 'Vasek','Milan',
 'Michal'
]
print("Původní seznam:")
print(jmena)

kopie_jmen = list(jmena)

for i in range(len(kopie_jmen)):

    for j in range(i + 1, len(kopie_jmen)):

        if kopie_jmen[i] > kopie_jmen[j]:
            kopie_jmen[i], kopie_jmen[j] = kopie_jmen[j], kopie_jmen[i]

print("Seřazený seznam:")
print(kopie_jmen)