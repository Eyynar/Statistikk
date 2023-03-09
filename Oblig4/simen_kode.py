#Oppgave 1 B
import random
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import math

antall_kast = int(input(f"Skriv inn antall kast du ønsker: "))
omganger = int(input(f"Skriv inn antall omganger du ønsker: "))
x = 0
result = {}
while x < omganger:
    sum_av_terning = 0
    for y in range(antall_kast):
        sum_av_terning += random.randint(1, 6)

    gjennomsnitt = sum_av_terning/antall_kast
    print(f"omgang: {x+1}, antall kast: {antall_kast}, sum av kastene: {sum_av_terning}, gjennomsnitt: {gjennomsnitt}")
    result[x+1] = [omganger, antall_kast, sum_av_terning, gjennomsnitt]
    x += 1

print(result)


# Oppgave 1 C
sum_av_gjennomsnitt = 0
for y in range(omganger):
    #print(result[y+1][3])
    sum_av_gjennomsnitt += result[y+1][3]

utvalgsgjennomsnitt = sum_av_gjennomsnitt/omganger
z = 0
for x in range(omganger):
    z += math.pow(result[x+1][3], 2)

utvalgsvarians = (z - omganger * (math.pow(utvalgsgjennomsnitt, 2)))/(omganger - 1)
print(f"utvalgsvarians: {utvalgsvarians}")
utvalgsstandardavvik = math.sqrt(utvalgsvarians)
print(f"utvalgsstandardavvik: {utvalgsstandardavvik}")
#utvalgsstandardavvik skal ligge rundt den utregningen under
print(1.71 / math.sqrt(antall_kast))