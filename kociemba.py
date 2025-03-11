import twophase.solver  as sv
import kociemba

cubestring = 'UFFRUDLULFLDRRULFRBFDLFBUUBFBDDDDRDBRFULLUDRLRLFRBBUBB'
rozwiazanie = sv.solve(cubestring,19,2)
print ("Rozwiązanie kostki:", rozwiazanie)