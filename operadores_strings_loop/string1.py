nome = "vik"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "     xerecao    "

print(texto)
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())


menu = "pinto"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-i-r-o-c-a")

for letra in menu:
    print(letra, end="-")
    print()

print("-".join(menu))