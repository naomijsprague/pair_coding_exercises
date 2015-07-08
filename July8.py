# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:18:02 2015

@author: naomi
"""

def prime_factor(number):
    largest = 0
    previous = []
    for i in range(2,number):
        if number % i == 0:
            for n in range(2,i+1):
                if i % n != 0:
                    if n > largest:
                        largest = n
    return largest                   
                    
                    

number = 82
print prime_factor(number)


def prime_divisor(number):
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            number /= divisor
        else:
            divisor += 1
            return number

print prime_divisor(4637582)       



