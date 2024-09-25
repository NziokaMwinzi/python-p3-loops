#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while(i>0):
        print(f"{i}")
        i -= 1
    else:
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_lists=list()
    for num in int_list:
        new = num * num
        int_lists.append(new)
    return int_lists
    

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)
            
    



