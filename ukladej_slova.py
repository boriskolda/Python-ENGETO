# V této úloze vytvoř program, který ukládá slova, která mají délku čtyři znaky. Jakmile uloží tři taková slova, skončí.

# Jednotlivé kroky, které program musí obsahovat:

# Definuj novou proměnnou slova, kam budeš slova ukládat,
# zapiš proces, který ukládá ukládá vstupy uživatele do proměnné slovo,
# tento proces pracuje tak dlouho, dokud proměnná slova neobsahuje tři unikátní slova,
# pokud je uživatelem vybrané slovo již součástí objektu slova, potom vypiš zprávu "Slovo <slovo> už je uložené",
# pokud není uživatelem vybrané slovo dlouhé čtyři znaky, vypiš zprávu "Slovo není dlouhé čtyři znaky",
# pokud je uživatelem vybrané slovo dlouhé čtyři znaky, potom jej přidej do proměnné slova,
# jakmile proces skončí (proměnná slova obsahuje tři hodnoty), vypiš zprávu "Už mám uložené tři slova".

slova = []

while len(slova) < 3:
    zadani = input('ZADEJ SLOVO ZE ČTYŘ:')
    if len(zadani) == 4 and zadani not in slova:
        slova.append(zadani)
    elif zadani in slova:
        print(f'Slovo {zadani} už je uložené')
    else:
        print('Slovo není dlouhé čtyři znaky')
else:
    print('Už mám uložené tři slova')
