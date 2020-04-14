import os
import sys
os.chdir("C:\\Users\\jdealmeida\\Documents\\PC_PERSO\\ICPC\\ICPC_groupe6\\")

# distance_trip=input('Distance du trip : ')
# capacite_reservoir=input('Capacité du réservoir d essence : ')
# miles_reservoir=input('Combien de Miles/Réservoir d essence : ')
# cout_plein=input('Cout du plein d essence : ')
#nbr_stations=int(input('Nombre de stations : '))

# def miles_to_km(miles):
#     return miles*1,609
#
# print('-- Voiture --')
# print('Capacité du réservoir : ' + capacite_reservoir + 'L')
# print('Cout du plein à la ville de départ ' + cout_plein + '€')
# print('Kilomètres par plein : ' + miles_reservoir + 'm')

# print('-- Station --')
# print('Nombre de stations : ' + str(nbr_stations))

# print('-- Trip --')
# print('Distance du Trip : ' + distance_trip)

# from pathlib import Path
# os.chdir("C:/tests python")
#
# path = os.getcwd()
# print("Le répertoire courant est : " + path)
#
# repn = os.path.basename(path)
# print("Le nom du répertoire est : " + repn)

#__file__ = "ICPC_199.py"

# dir_path = os.path.dirname(os.path.abspath(__file__))
# dir_path2 = os.path.abspath(__file__)
# print(dir_path)
# print(dir_path2)

# print(os.path.join(os.getcwd(), __file__))

#
# path2 = os.path.realpath(__file__)
# print("Le chemin du script est : " + path2)

#print('sys.argv[0] =' + sys.argv[0])

# cout_station=[]
# distance_station=[]
# total_station=[]

# def definir_station(nbr):
#     for i in range(1,(nbr+1)):
#         print('\n')
#         cout = input('Cout en centimes du gallon d essence de la sation'+str(i)+' : ')
#         distance = input('Distance entre la ville de départ et la sation'+str(i)+' : ')
#         if cout == '':
#             break
#         else:
#             try:
#                 cout_station.append(int(cout))
#             except ValueError:
#                 cout_station.append(cout)
#         if distance == '':
#             break
#         else:
#             try:
#                 distance_station.append(int(distance))
#             except ValueError:
#                 distance_station.append(distance)

# def definir_station2(nbr):
#     for i in range(1,(nbr+1)):
#         print('\n')
#         cout = input('Cout en centimes du gallon d essence de la sation'+str(i)+' : ')
#         distance = input('Distance entre la ville de départ et la sation'+str(i)+' : ')
#         if cout == '':
#             break
#         else:
#             try:
#                 cout_station.append(int(cout))
#             except ValueError:
#                 cout_station.append(cout)
#         if distance == '':
#             break
#         else:
#             try:
#                 distance_station.append(int(distance))
#             except ValueError:
#                 distance_station.append(distance)

# def lire_fichier(fic):
#     mon_fichier = open(fic, "r")
#     contenu = mon_fichier.read()
#     print(contenu)
#     mon_fichier.close()

def parcourrir_fichier(fic):
    file = open(fic, "r")
    # utilisez readline() pour lire la première ligne
    line = file.readline()
    numLine = 0
    voiture=0
    while line:
        numLine = numLine+1
        if line == '-1':
            break
        else:
            # Distance entre la ville de départ et la ville de destination
            if(numLine==1):
                voiture = voiture +1
                print("Voiture n°"+str(voiture)+"\n",end='')
                print("Distance : "+line + "\n",end='')
            # Descriptif du véhicule
            elif(numLine==2):
                a, b, c, d = line.split(" ")
                print("Capacité du réservoir d'essence en gallon : " + str(a) + "\n",end='')
                print("Nombre de miles/gallon : " + str(b) + "\n",end='')
                print("Cout du remplissage du réservoir à la ville de départ : " + str(c) + "\n",end='')
                print("Nombre de station d'essence entre la ville de départ et d'arrivée : " + str(d) + "\n",end='')
                # Etapes
                for etape in range(1,int(d)+1):
                    line = file.readline()
                    e, f = line.split(" ")
                    print("Etape n°" + str(etape) + "\n",end='')
                    print("Distance de la station : " + str(e) + "\n",end='')
                    print("Prix du gallon (ctm) : " + str(f) + "\n",end='')
                numLine=0
        line = file.readline()
    file.close()

#while True:
#lire_fichier("C:\\Users\\jdealmeida\\Documents\\PC_PERSO\\ICPC\\ICPC_groupe6\\fichier.txt")
#parcourrir_fichier("C:\\Users\\jdealmeida\\Documents\\PC_PERSO\\ICPC\\ICPC_groupe6\\fichier.txt")
# definir_station(nbr_stations)
# print(cout_station)
# print(distance_station)
parcourrir_fichier("fichier.txt_old")