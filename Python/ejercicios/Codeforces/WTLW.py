palabras = input()
for _ in range(int(palabras)):
    palabra = input()
    if(len(palabra) > 10):
        print(palabra[0] + str(len(palabra)-2) + palabra[-1])
    else:
        print(palabra)

#4 3 2 1
#4 2 3 1
#A B C D
#A C B D