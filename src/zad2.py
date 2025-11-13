


f = open("/workspaces/matura-2025-r25-3a-stachulemko/src/symbole.txt")

tab = []
end = 0
count2 =0 
tabCount = []
for linia in f:
    count2 +=1
    linia = linia.strip()
    tab.append(linia)
    if(len(tab)==3):
        lastOne = ""
        count = 0
        for i in range(0,len(tab[0])):
            if(tab[0][i]==tab[1][i]==tab[2][i]):
                tmp = tab[0][i] + tab[1][i] +tab[2][i]
                if(tmp != lastOne):
                    lastOne = tmp
                    count = 1
                else:
                    count +=1
            else:
                lastOne = ""
                count =0
            if(count==3):
                lastOne = ""
                count =0 
                end+=1
                tabCount.append([count2-1,i])
        lastElemnt1 = tab[1]
        lastElemnt2 = tab[2]
        tab.clear()
        tab.append(lastElemnt1)
        tab.append(lastElemnt2)

all= ""
for elem in tabCount:
    all += f"{elem[0]} {elem[1]} "
print(all)