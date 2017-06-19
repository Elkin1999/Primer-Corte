#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: primes.py
# Description: este programa separa una lista de numeros enteros en dos listas, una de primos y otra de no primos
# Author: Elkin Camilo Osorio Martinez
def es_primo(num):
    if num<=1:
        
        return False
    else:
        for i in range(2,num-1):
            if num%i==0:
                
                return False

    if num%1==0 and num%num==0:
        
        return True

def primees(numbers):
    
    
    numbers = list(numbers)
    
    lista_pri = []
    lista_nopri = []

    
    jj = (len(numbers))

    for i in range(jj):
        if (es_primo(int(numbers[i])) == False):
            lista_nopri.append(numbers[i])   
        else:
             lista_pri.append(numbers[i])      
           
    return lista_nopri, lista_pri

def main():
    """ Main Program """
    numbers= ((input("escribir numeros (separados por espacio): ")).split())
    # TODO: convert the string "1 2 3 4 5" into a list [1, 2, 3, 4, 5]
    (pri, nopri) = primees(numbers)
    print("{} = {} and {}".format(numbers, pri, nopri))

if __name__ == "__main__":
    main()