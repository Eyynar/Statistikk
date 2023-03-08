import math

populasjon = int(input(f"Skriv inn utvalgets størrelse: "))
andel = int(input(f"Skriv inn andelen av utvalget: "))
KI_prosent = int(input(f"Skriv inn konfidensintervallet i prosent (uten prosent tegn): "))

KI_prosent = KI_prosent/100

alpha = 1 - KI_prosent
alpha_halv = round(alpha/2,3)

p_hat = andel/populasjon

forutsetning = populasjon *(p_hat) *(1-p_hat)

if forutsetning < 5:
    print(f"Forutsetningen er ikke oppfylt med at {populasjon} * {p_hat}*(1-{p_hat}) = {forutsetning} >= 5")
else:
    print(f"Forutsetningen er oppfylt med at {populasjon} * {p_hat}*(1-{p_hat}) = {forutsetning} >= 5")

z_value = {0.025 : 1.960 , 0.100 : 1.282, 0.050: 1.642, 0.010 : 2.326, 0.005 : 2.576, 0.001 : 3.090 }

z = z_value[alpha_halv] * math.sqrt((p_hat*(1-p_hat))/populasjon)

print(f"{KI_prosent*100}% KI med {populasjon} som utvalgets størrelse = \n[{p_hat - z} , {p_hat+z}]")
