#!/usr/bin/env python3

import temp_conv
#  calls for conversion function
def display_title():
    print("Temperature Converter")
    #  display title when launch 
def display_menu():
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    #  display menu for user options
def main():
    display_title()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ")
        #  request a user input
        #  and performs calculations based on option
        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = temp_conv.fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is approximately {celsius}°C\n")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = temp_conv.celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is approximately {fahrenheit}°F\n")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose from 1, 2, or 3.")
            
   
   
   
if __name__ == "__main__":
    main()