#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: days_between.py
# Description: este programa calcula cuantos dias hay entre dos fechas establecidas.
# Author: Elkin Camilo Osorio Martinez

def days_between(fecha_inicial, fecha_final):
   
    from datetime import datetime, timedelta
    ini_date = ("")
    fin_date = ("")
    formato1 = "%Y-%m-%d"
    while True:
        try:
            if fecha_inicial == "":
                break
            if fecha_final == "":
                break
            fecha_inicial = datetime.strptime(fecha_inicial, formato1)

            fecha_final = datetime.strptime(fecha_final, formato1)

            if fecha_final >= fecha_inicial:
                days = fecha_final - fecha_inicial
                return days.days
            else:
                return print("escriba una fecha final, mayor o igual a la fecha inicial")
        except: 
            print ("no se puede hacer") 
        return 0           
def main():
    """ Main Program """
    ini_date = input("fecha inicial (yyyy-mm-dd): ")
    fin_date = input("fecha final (yyyy-mm-dd): ")
    # TODO: convert the strings dates ("yyyy-mm-dd") to your date structure
    days = days_between(ini_date, fin_date)
    print("hay {} dias entre {} y {}".format(days, ini_date, fin_date))

if __name__ == "__main__":
    main()

