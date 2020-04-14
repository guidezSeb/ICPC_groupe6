import os
import sys
os.chdir("C:\\Users\\jdealmeida\\Documents\\PC_PERSO\\ICPC\\ICPC_groupe6\\")

class Voiture:
    nom = 0
    distance = 0
    capacite = 0
    mile_g = 0
    cout_remp = 0
    nb_stations = 0
    etapes = []

def parcourrir_fichier(fic):
    file = open(fic, "r")
    # utilisez readline() pour lire la première ligne
    line = file.readline()
    line_v = line[:-1]
    numLine = 0
    voiture = 0
    voitures = []
    while line:
        numLine = numLine+1
        if line == '-1':
            break
        else:
            # Distance entre la ville de départ et la ville de destination
            if(numLine==1):
                voiture = voiture +1
                ma_voiture=Voiture()
                #print("Voiture n°"+str(voiture)+"\n",end='')
                ma_voiture.nom=voiture
                #print("Distance : "+line + "\n",end='')
                ma_voiture.distance=float(line_v)
            # Descriptif du véhicule
            elif(numLine==2):
                liste = line_v.split(" ")
                a, b, c, d=float(liste[0]), float(liste[1]), float(liste[2]), float(liste[3])
                #print("Capacité du réservoir d'essence en gallon : " + str(a) + "\n",end='')
                ma_voiture.capacite=a
                #print("Nombre de miles/gallon : " + str(b) + "\n",end='')
                ma_voiture.mile_g=b
                #print("Cout du remplissage du réservoir à la ville de départ : " + str(c) + "\n",end='')
                ma_voiture.cout_remp=c
                #print("Nombre de station d'essence entre la ville de départ et d'arrivée : " + str(d) + "\n",end='')
                ma_voiture.nb_stations=d
                # Etapes
                for etape in range(1,int(d)+1):
                    line = file.readline()
                    line_v = line[:-1]
                    liste =  line_v.split(" ")
                    e, f = float(liste[0]), float(liste[1])
                    ma_voiture.etapes.append([e,f])
                voitures.append(ma_voiture)
                numLine=0
        line = file.readline()
        line_v = line[:-1]
    file.close()
    for ma_voiture in voitures:
        print(ma_voiture.nom, type(ma_voiture.nom))
        print(ma_voiture.distance, type(ma_voiture.distance))
        print(ma_voiture.capacite, type(ma_voiture.capacite))
        print(ma_voiture.mile_g, type(ma_voiture.mile_g))
        print(ma_voiture.cout_remp, type(ma_voiture.cout_remp))
        print(ma_voiture.nb_stations, type(ma_voiture.nb_stations))
        for etape in range(1,(int(ma_voiture.nb_stations)+1)):
            print(str(etape)+": " + str(ma_voiture.etapes[etape-1]), type(ma_voiture.etapes[etape-1]), "\n")
    #print(ma_voiture.etapes)

parcourrir_fichier("fichier.txt_old")