# -*- coding: utf-8 -*-

import math

while True:
    print("\nVítejte v programu pro výpočet kořene/ů kvadratické rovnice.")
    a=int(input("Zadejte hodnotu a:"))
    b=int(input("Zadejte hodnotu b:"))
    c=int(input("Zadejte hodnotu c:"))
    d=(b**2)-4*a*c
    if a == 0:
        print("\nRovnice není kvadratická, ale lineární!")
    elif d < 0:
        print("\nRovnice nemá v oboru reálných čísel řešení!")
    elif d == 0:
        x=-b/(2*a)
        print("\nKvadratická rovnice má jeden kořen.")
        print("Kořen kvadratické rovnice je:",x)
    else:    
        x=(-b-(math.sqrt(d)))/(2*a)
        y=(-b+(math.sqrt(d)))/(2*a)
        print("\nKvadratická rovnice má 2 kořeny.")
        print("První kořen kvadratické rovnice je:",x)
        print("Druhý kořen kvadratické rovnice je:",y)