#!/usr/bin/env python3

def happy_new_year():
    sec = 10
    while sec >= 1:
        print(sec)
        sec -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    int_list = [1, 2, 3, 4, 5]
    for i in int_list:
        int_list.append(i**2) 
    return int_list


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

    
