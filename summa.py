#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even.py
# Description: This module separates a list of integers into two lists (odd, even)
# Author: Diego Fernando Marin
a = int(input("escriba el numero a:"))
b = int(input("escriba el numero b:"))
suma = 0 
p=0
if a > b:
	print("a debe ser mayor que b")
else: 
	for x in range(a,b+1):
		suma+= x**2 + 2*6
	print (suma)