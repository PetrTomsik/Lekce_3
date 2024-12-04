import datetime

jmeno = "Albert"
druhe_jmeno = "Jura"
cislo = 30.4444444444444
print(f"Ahoj jsem {jmeno} a {druhe_jmeno} a je mi {cislo:.2f} let")   #f sting pred dám f
# pokud chces naformatot na dve desetiny cisla  (:.2f)


print(f"Promenna cislo >6 {cislo>6}")


# Prints today's date with help
# of datetime library


today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


print(f"'GeeksforGeeks'")
print(f"""Geeks"for"Geeks""")
print(f'''Geeks'for'Geeks''')

english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")

newline = ord('\n')

print(f"newline: {newline}")