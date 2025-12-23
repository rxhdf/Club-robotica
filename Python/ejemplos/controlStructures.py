#condicionales
robux = 20
if robux == 18:
    print("Jovencito")
else:
    print("Femboy666")

#bucles o ciclos
lista = [1, "silla", 3, 4, "mesa"]

for i in lista:
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

#funciones
def juanelcaballo(comida):
    if(comida == "Pan" or comida == "Pasto"):
        print("Ta nutrido")
    else:
        print("Ta desnutrido")

print(juanelcaballo("Pizza"))