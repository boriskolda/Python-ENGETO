MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print("===================================")

cislovani = 1
for i in MESTA:
    if len(i) == 4:
        print(cislovani, "-", i, "   |", CENY[cislovani-1])
    elif len(i) < 7:
        print(cislovani, "-", i, "  |", CENY[cislovani-1])
    else:
        print(cislovani, "-", i, "|", CENY[cislovani-1])
    cislovani += 1

lokalita = int(input("VYBERTE CISLO LOKALITY: "))-1
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
narozeni = input("ROK NAROZENI: ")
email = input("EMAIL: ")
heslo = input("HESLO: ")
              
print("===================================")
print(f"LISTEK DO: {MESTA[lokalita]} CENA: {CENY[lokalita]}")
print(f"DEKUJI, {jmeno} NA MAIL {email} TI PRIJDE KRATKY DOTAZNIK")