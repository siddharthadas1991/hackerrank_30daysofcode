#!/bin/python3

import math
import os
import random
import re
import sys

def CodStatement(N) :
    if N %2 !=0 :
        print("Weird")
    else :
        if N <=5 and N>=2 :
            print("Not Weird")
        elif (N <=20 and N >=6):
            print("Weird")
        elif N >20 :
            print("Not Weird")
            

if __name__ == '__main__':
    N = int(input().strip())
    CodStatement(N)



    
        