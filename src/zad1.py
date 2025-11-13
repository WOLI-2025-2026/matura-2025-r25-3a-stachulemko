# Stanisław Kępka

f = open("/workspaces/matura-2025-r25-3a-stachulemko/src/symbole.txt")

for linia in f:
    linia = linia.strip()
    length = len(linia)
    #print(linia)
    if linia == linia[::-1]:
        print(linia)
        break

f.close()