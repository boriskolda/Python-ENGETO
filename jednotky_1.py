# Prevodni pomery
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = int(input("kg na lb "))
km_pocet = int(input("km na mil "))
l_pocet = int(input("l na gal "))


print(f"{kg_pocet} kg je {kg_pocet*kg_lb} lb")
print(f"{km_pocet} kg je {km_pocet*km_mile} lb")
print(f"{l_pocet} kg je {l_pocet*l_gal} lb")