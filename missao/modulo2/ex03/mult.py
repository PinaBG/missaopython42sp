#!/usr/bin/env python3

numero_1 = int(input("Enter the first number: \n"))
numero_2 = int(input("Enter the second number: \n"))

multiplicacao = numero_1 * numero_2

print(f"{numero_1} x {numero_2} = {multiplicacao}")

if(multiplicacao > 0):
    print("The result is positive.")
elif(multiplicacao < 0):
    print("The result is negative.")
else:
    print("The result is positive and negative.")
