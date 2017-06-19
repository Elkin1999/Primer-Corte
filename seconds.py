#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: seconds.py
# Description: This module convert seconds to years, months, days, hours, minutes and seconds
# Author: Elkin Camilo Osorio MArtinez

result_str = "{} seconds es equivalente a {} years, {} months, {} days, {} hours, {} minutes and {} seconds"

def convert_seconds(seconds):
    
    secs = seconds % 60
    seconds = seconds // 60
    minutes = seconds % 60 
    seconds = seconds // 60
    hours = seconds % 24
    seconds = seconds // 24
    days =seconds % 30
    seconds =seconds // 30
    months = seconds % 12
    seconds = seconds // 12
    years = seconds 

    fechatotal = (years, months, days, hours, minutes,secs)

    return fechatotal

def main():
    """ Main Program """
    seconds = int(input("number of seconds: "))
    (years, months, days, hours, minutes, secs) = convert_seconds(seconds)
    print(result_str.format(seconds, years, months, days, hours, minutes, secs))

if __name__ == "__main__":
    main()

