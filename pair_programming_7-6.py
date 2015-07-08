# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:17:14 2015

@author: naomi
"""

def balance_paren(arg):
    left = arg.count("(")
    right = arg.count(")")
    left_count = 0    
    right_count = 0
    for i,a in enumerate(arg):
        if a == '(':
            left_count += i
        else:
            right_count += i
    verdict = lambda x,y,w,z: True if x==y and w < z else False
    return verdict(left,right,left_count,right_count)
    
print balance_paren(str(raw_input("Please input paren: ")))


def pair(input_str):
    counts=0
    for idx,elem in enumerate(input_str):
        if elem=='(':
            counts=counts+1
        else:
            counts=counts-1
        
        if counts<0:
            return False
    
    if counts>0:
        return False
    return True