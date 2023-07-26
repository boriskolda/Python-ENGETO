# V této úloze vytvoř program, který si od uživatele nejprve vyžádá aritmetický operátor a následně čísla, se kterými celý zápis vypočítá.

# Po každé operaci se program uživatele zeptá zda chce provést další operaci nebo chce program ukončit.

# Jednotlivé kroky, které program musí obsahovat:

# Vytvoř nekonečnou smyčku
# uživatel může vybrat operátor, dostupné jsou "+", "-",
# vstup uživatele ulož do proměnné operation,
# pokud hodnota v proměnné operation není ("+", "-"), vypiš "Nezadali jste platný operátor, zkuste to znovu" a vrátí se na začátek běhu programu,
# pokud je hodnota v proměnné - ("+", "-"), dovol uživateli zadat vstupy do proměnných number_1 a number_2,
# spoj hodnoty v number_1, choice a number_2, vypočítej výsledek a vypiš např. 1 + 9 = 10,
# zeptá se uživatele zda chce provést další operaci pokud ano program se vrátí na začátek běhu, pokud ne program se ukončí.

while True:
    print('Sčítání:    "+",')
    print('Odčítání:   "-",')
    print('----------------------')


    operation = input("Vyber si operaci: ")
    if operation not in ("+","-"):
        print("Nezadali jste platný operátor, zkuste to znovu.")
        continue

    number_1 = int(input("Zadej první číslo: "))
    number_2 = int(input("Zadej druhé číslo: "))
    
    if operation == "+":
        print(f"{number_1} {operation} {number_2} = {(number_1 + number_2)}")
    elif operation == "-":
        print(f"{number_1} {operation} {number_2} = {(number_1 - number_2)}")
    
    choice = input("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne):")
    if choice == 'a':
        continue
    else:
        print('Ukončuji...')
        break