import random
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
           
