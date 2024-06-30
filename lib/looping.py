#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        if(i == 1):
            print("Happy New Year!")
        
        i -= 1

happy_new_year()

    


        

    

def square_integers(int_list):
    squared = [element * element for element in int_list]
    return squared
    
print(square_integers([1, 2, 3, 4, 5]))

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
fizzbuzz()

