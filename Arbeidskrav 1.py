# -*- coding: utf-8 -*-
"""
Arbeidskrav 1 

Amalie Zedell


Sammenligning av årlige kostnader ved elbil sammenliknet med bensinbil

"""

Km = 10000  # [Km/året, lik for begge]

T = 8.38  # [Trafikkforsikringsavgift kr/dag, lik for begge]



Fe = 5000  # [Forsikring Elbil]

Foe = 0.2  #[Forbruk Elbil, kWh/km]

Sp = 2  #[Strømpris, kr/kWh]

Be = 0.1  # [Bomavgift Elbil, kr/km]



Fb = 7500  # [Forsikring Bensinbil]

Db = 1  # [Drivstoff Bensinbil, kr/km]

Bb = 0.3  # [Bomavgift Bensinbil, kr/km]



E = (Be + Sp*Foe)*Km + T*365 + Fe
print("Elbil =",E)


B = (Db + Bb)*Km + T*365 + Fb
print("Bensinbil =",B)

print("Differansen er:",E - B)