#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    
    while n > 0:
        remain = n % 2
        n = n//2
        arr.append(remain)
    
    count,result = 0,0
    
    for i in range(0,len(arr)):
        if arr[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
    
    print(result)