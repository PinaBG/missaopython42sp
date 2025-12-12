#!/usr/bin/env python3

numero = int(input("Enter a number less than 25\n"))

if(numero > 25):
    print("Error")
else:
    while numero <= 25:
        print("Inside the loop, my variable is " + str(numero))
        numero += 1;
