#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: add_days.py
# Description: Este programa agrega dias a una fecha establecida
# Author: Elkin Camilo Osorio Martinez

def add_days(date, days):

    from datetime import datetime, timedelta

    initial_date=("")

    formato1 = "%Y-%m-%d"
    date = datetime.strptime(date, formato1)

    days = timedelta(days=days)
    final_date = date + days

    return final_date.strftime(formato1)

def main():
    """ Main Program """
    initial_date = input("initial date (yyyy-mm-dd): ")
   
    days = int(input("days: "))
    final_date = add_days(initial_date, days)
    print("{} + {} days = {}".format(initial_date, days, final_date))

if __name__ == "__main__":
    main()
