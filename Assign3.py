#!python3
"""
Write a program that sorts the values in this list and prints
the 3 highest numbers. You may use multiple print statements,
but you should try to incorporate a for loop and use 1 print
statement instead.
"""



def find_largest_three(numbers):
    largest_three = [float('-inf')] * 3
    
    for i in numbers:
        if i > largest_three[0]:
            largest_three[2] = largest_three[1]
            largest_three[1] = largest_three[0]
            largest_three[0] = i
        elif i > largest_three[1]:
            largest_three[2] = largest_three[1]
            largest_three[1] = i
        elif i > largest_three[2]:
            largest_three[2] = i
            
    return largest_three


numbers = [3,4,6,1,3,6,12,33,15,2,22,9,17]
largest_three = find_largest_three(numbers)
print("The three largest numbers are:", largest_three)
