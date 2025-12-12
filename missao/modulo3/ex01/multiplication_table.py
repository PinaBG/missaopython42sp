#!/usr/bin/env python3

numero = int(input("Enter a number \n"))

count = 0
while count < 10:
    print(str(count) + " x " + str(numero) + " = " + str(count * numero))
    count +=1
