#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even.py
# Description: This module separates a list of integers into two lists (odd, even)
# Author: Elkin Camilo Osorio Martinez
string, lista, nueva = (input(">"), [], [])
for h in string:
        contador=0
        sumcont=0
        for s in string:
                if h == s:
                        contador += 1
                sumcont+=1
                fre = contador / sumcont
                porcentaje= fre*100          
        lista.append("%s:%s:%s"%(h,contador,porcentaje))
out = [nueva.append(nn) for nn in lista if nn not in nueva]
print ("Repeticiones:")
for salida in nueva: print (salida,"%")