distance_trip=input('Distance du trip : ')
capacite_reservoir=input('Capacité du réservoir d essence : ')
miles_reservoir=input('Combien de Miles/Réservoir d essence : ')
cout_plein=input('Cout du plein d essence : ')
nbr_stations=input('Nombre de stations : ')

def miles_to_km(miles):
    return miles*1,609

print('-- Voiture --')
print('Capacité du réservoir : ' + capacite_reservoir + 'L')
print('Cout du plein ' + cout_plein + '€')
print('Kilomètres par plein : ' + miles_reservoir + 'm')

print('-- Station --')
print('Nombre de stations : ' + nbr_stations)

print('-- Trip --')
print('Distance du Trip : ' + distance_trip)