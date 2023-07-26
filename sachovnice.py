# V této úloze vytvoř program, který vypíše šachovnici (střídání černých '#' a bílých ' ' polí).

# Jednotlivé kroky, které program musí obsahovat:

# Vytvoř tyto vstupní proměnné:
# Ukázka kódu
# ZKOPÍROVAT KÓD
# velikost = 10
# sachovnice = []
# symboly = ['#',' ']
# iteruj přes jednotlivé řádky šachovnice (velikost),
# každém kroce iterace vytvoř proměnnou rada,
# následně iteruj přes jednotlivé buňky,
# vytvoř pomocnou proměnnou index, která vybere pomocí proměnné symbols aktuální pozici, (ať vytvoříš střídavě pole " " a "#"),
# postupně přidávej jednotlivé symboly do proměnné rada,
# na konci řádku přidej rada do proměnné sachovnice,
# na závěr spoj jednotlivé hodnoty v proměnné sachovnice pomocí \n a vypiš její obsah.

velikost = 15
sachovnice = []
symboly = ['#',' ']

# for j in range(0, velikost):
#     for i in range(0,velikost):
#         if j % 2 == 0:
#             if i % 2 == 0:
#                 print(symboly[0], end="")
#             else:
#                 print(symboly[1], end="")
#         else:
#             if i % 2 == 0:
#                 print(symboly[1], end="")
#             else:
#                 print(symboly[0], end="")
#     print("")

rada = ""

for j in range(0, velikost):
    for i in range(0,velikost):
        if j % 2 == 0:
            if i % 2 == 0:
                rada += symboly[0]
            else:
                rada += symboly[1]

        else:
            if i % 2 == 0:
                rada += symboly[1]
            else:
                rada += symboly[0]

    sachovnice.append(rada)
    rada = ""
    
# print(sachovnice)

for i in sachovnice:
    print(i)