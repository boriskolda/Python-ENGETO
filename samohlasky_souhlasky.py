# V této úloze vytvoř program, který spočítá kolik samohlásek a souhlásek obsahuje zadaný string:

# Ukázka kódu
# ZKOPÍROVAT KÓD
# veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'


# Jednotlivé kroky, které program musí obsahovat:

# Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu ",
# proměnnou samohlasky, typu str, která obsahuje "aeiouy",
# proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". Slovník bude evidovat výskyty těchto hodnot,
# iteraci přes všechny znaky v proměnné veta,
# pokud znak není ani samohláska, ani souhláska, tak jej přeskoč,
# pokud je znak samohláska nebo souhlaska, inkrementuj ve slovníku vysledek správný klíče,
# nakonec vypiš konečný stav podle ukázky níže.

veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

samohlasky = "aeiouyáéíóůú"
vysledek = {"souhlasky": 0,"samohlasky":0}

for pismeno in veta:
    if pismeno in samohlasky:
        vysledek["samohlasky"]+=1
    elif pismeno.isalpha:
        vysledek["souhlasky"]+=1

print(f"Počet souhlásek: {vysledek['souhlasky']} | Počet samohlásek: {vysledek['samohlasky']}")


