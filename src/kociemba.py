import twophase.solver  as sv
import kociemba

cubestring = 'UFFRUDLULFLDRRULFRBFDLFBUUBFBDDDDRDBRFULLUDRLRLFRBBUBB'
rozwiazanie = sv.solve(cubestring,19,2)
print ("Rozwiązanie kostki:", rozwiazanie)

#Do wprowadzenia:
#cubestring = ['kod_kostki'] gdzie będzie pobierał wartości z kod_kostki i będzie interaktywnie kostke rozwiązywał generowanej według UFLRBD
