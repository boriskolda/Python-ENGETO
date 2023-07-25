# ceník
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print(f"Sleva na Mercedes: {sleva_merc}")
print(f"Cena za dva Mercedesy je: {cena_2_merc}")
print(f"Cena za Mercedes a Rolls-Royce: {cena_merc_a_rolls}")
print(f"Cena za dva Rolls-Royce s příplatkovou výbavou: {cena_2_rolls_s_vybavou}")
print(f"Cena za Mercedes s příplatkovou výbavou: {cena_merc_s_vybavou}")
print(f"Cena za Mercedes po slevě: {merc_se_slevou}")