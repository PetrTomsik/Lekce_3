print(f"True or False {True or False}") # False
print(f"False or False {False or False}") # False
print(f"True and False {False and False}") # False

print(f"True and False {True and False or True}") # prvni se udela and a pak or


# základní operace s retezci
retezec = "Dnes je velmi pekne počasí"
print(retezec.index("e"))   #vypise dvojku
print(retezec.index("D"))
print(f"len retezec {len(retezec)}") # delka retezce

# vyhledáná v textu
#funkce input() nám vrátí vepsaný text

retezec2 = input("Vložte řetezec")
retezec3 = input("Hledas řetezec")
#print(f"Vlozil si text: {retezec2}")
#print(f'Hledáš v textu: {retezec3}')
print(f'retezec index(){retezec2.index(retezec3)}') #uvozovky se musí strídat
print(f'Vlozil si text: {retezec2} a budeme hledat {retezec3}')
print(f'řetezec je dlouhy {len(retezec2)}')


#{} pravý alt B


