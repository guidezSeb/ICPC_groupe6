import os
import sys
import math

tab=[]
prix = []

entree=input("Votre ligne d'entrée : ")

def param(i):
    switch={
        0:'p',
        1:'a',
        2:'b',
        3:'c',
        4:'d',
        5:'n',
    }
    return switch.get(i,"Paramètre invalide")
def controle_entree():
    global tab
    for val in entree.split(" "):
        tab.append(int(val))
    if len(tab) != 6:
        print("Entrée incorrect - 6 paramètres requis - trouvés :",len(tab),"\n")
        exit(1)
    for i in range(0,len(tab)):
        print("-",param(i),"=",tab[i])
        if (i==0 and (int(tab[i])>1000 or int(tab[i])<1)) or (1<=i<= 4 and (int(tab[i])>1000 or int(tab[i])<0)) or (i==5 and (int(tab[i])>10**6 or int(tab[i])<1)):
            print("Erreur - Valeur de",param(int(i)), "incorrecte :",str(tab[i]))
            exit(1)


def traitement():
    global tab
    global prix
    for i in range(tab[5]):
        prix.append(float(tab[0]*(math.sin(tab[1]*i+tab[2])+math.cos(tab[3]*i+tab[4])+2)))
    #print(str(prix))
    max=0
    min=9999
    diff=0
    for val in prix:
        if val >= max:
            max=val
            min=val
        if val < min:
            min=val
        if (max - min) > diff and max!=0:
            diff=max-min
    return float(diff)

controle_entree()
print("Plus grande chute de prix :",traitement())