# Stanisław Kępka

f = open("/workspaces/matura-2025-r25-3a-stachulemko/src/symbole.txt")

plik = open("/workspaces/matura-2025-r25-3a-stachulemko/src/wyniki/zad1output.txt", "w")
for linia in f:
    linia = linia.strip()
    length = len(linia)
    #print(linia)
    if linia == linia[::-1]:
        plik.write(linia)
        plik.close()
        break

f.close()

