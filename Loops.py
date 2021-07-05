#!/bin/python3

import math
import os
import random
import re
import sys


def ChallangeDef(inp):
    for i in range(1,11):
        print(str(inp) + " x " + str(i) + " = " + str(inp * i))
    

if __name__ == '__main__':
    n = int(input().strip())
    ChallangeDef(n)

    