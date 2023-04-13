# -*- coding: utf-8 -*-

from math import *

while True:
    print("\n*****MENU******\n1=PŘEVOD ÚHLOVÝCH STUPŇŮ NA RADIÁNY\n2=PŘEVOD RADIÁNŮ NA ÚHLOVÉ STUPNĚ\nCOKOLI JINÉHO=KONEC")
    v=int(input("Zadejte volbu:"))
    if v==1:
        print("Zvolili jste si PŘEVOD  ÚHLOVÝCH STUPŇŮ NA RADIÁNY")
        a=int(input("Zadejte stupně: "))
        print(a," úhlových stupňů je ",radians(a),"radiánů.")
        continue
    elif v==2:
        print("Zvolili jste si PŘEVOD RADIÁNŮ NA ÚHLOVÉ STUPNĚ")
        a=int(input("Zadejte radiány: "))
        print(a," radiánů je ",degrees(a),"úhlových stupňů.")
        continue
    else:
        print("KONEC")
    break