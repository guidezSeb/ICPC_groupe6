#PROBLEME H de 1995 100% fonctionnel résultat attendu OK
import os
import sys
import re
os.chdir("C:\\Users\\jdealmeida\\Documents\\PC_PERSO\\ICPC\\ICPC_groupe6\\")

texte_brut=[]
texte=[]
texte_final=[]
texte_over9000=[]

def test_entier(x):
  try:
    int(x)
    return True
  except ValueError:
    return False

def parcourrir_fichier(fic):
    file = open(fic, "r")
    line = file.readline()
    #line_v = line[:-1]
    global texte
    while line:
        if line == '0':
            break
        else:
            brut=re.split(r'(\W+)',line)
            for x in brut:
                if(x!=''):
                    texte_brut.append(x)
            mots = re.split(';|,|\'|-|\.|\t|\n|\s',line)
            for mot in mots:
                if(mot!=''):
                    texte.append(mot)
        line = file.readline()
    file.close()

def decompression_fichier():
    index=0
    global texte_final
    texte_trt=list(texte)
    for mot in texte_trt:
        if test_entier(mot):
            word=texte_trt[index-int(mot)]
            texte_trt[index]=word
            texte_trt.pop(index-int(mot))
            texte_trt.insert(0,word)
        texte_final.append(texte_trt[index])
        index+=1

def ecrire_fichier():
    fichier = open("resultat.txt", "w")
    for mot in texte_over9000:
        fichier.write(mot)
    fichier.close()

def replace_ponctuation():
    global texte_over9000
    index_ponct=0
    index_mot=0
    for mot in texte:
        for i in range (index_ponct,len(texte_brut)):
            if(mot == texte_brut[i]):
                texte_over9000.append(texte_final[index_mot])
                index_ponct+=1
                break
            else:
                texte_over9000.append(texte_brut[i])
                index_ponct+=1
        index_mot+=1
    for j in range (index_ponct,len(texte_brut)):
        texte_over9000.append(texte_brut[j])


parcourrir_fichier("H_1995.txt")
decompression_fichier()
replace_ponctuation()
ecrire_fichier()