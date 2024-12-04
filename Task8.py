import datetime

jmeno = "Albert"
druhe_jmeno = "Jura"
cislo = 30.4444444444444
print(f"Ahoj jsem {jmeno} a {druhe_jmeno} a je mi {cislo:.2f} let")   #f sting pred dám f

# Prints today's date with help
# of datetime library


today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


print(f"'GeeksforGeeks'")
print(f"""Geeks"for"Geeks""")
print(f'''Geeks'for'Geeks''')