import random
import math
import copy

def sample(arraylike, n, replace = True):
    arrCopy = copy.copy(arraylike)
    output = [0] * n
    for i in range(n):
        index = random.randint(0, len(arrCopy)-1)
        output[i] = arrCopy[index]
        if not replace:
            arrCopy.pop(index)
    return output

def nCr(n, r):
    return (math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))
           
