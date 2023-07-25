# V této úloze vytvoř program, který ti vypíše celá čísla od 1 do 100 (včetně 100).

# Jednotlivé kroky, které program musí obsahovat:

# Iterování čísel od 1 do 100,
# pokud bude číslo násobek 3, vypiš Fizz (místo čísla),
# pokud bude číslo násobek 5, vypiš Buzz (místo čísla),
# pokud bude číslo násobek 3 a zároveň násobek 5, vypiš FizzBuzz (místo čísla),
# pokud půjde o kterékoliv jiné číslo, vypiš jej.

for cislo in range(1,101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)

