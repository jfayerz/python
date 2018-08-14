#------------------------------------------------------------------------#
#---------------------Pair Columbus - Problem One------------------------#
#--Write three functions that compute the sum of the numbers in a given--#
#-----------list using a for-loop, a while-loop, and recursion-----------#
#------------------------------------------------------------------------#

list1 = [1, 2, 3, 4, 5]

def forLoop():
    x = 0
    for item in list1:
        x = x + item
    return x

print(forLoop())

def whileLoop():
    x = 0
    i = 0
    while x < len(list1):
        i = i + list1[x]
        x = x + 1
    return i

print(whileLoop())

def recurseSum():
    i = len(list1) - 1
    if i < 1:
        return i
    x = list1[i] + list1[i - 1]
    i = i - 1
    return x

recurseSum()
