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

def recurseSum(n):   
    if len(n)==0:
        return 0
    else:
        return n[0] + recurseSum(n[1:])
    # Slicing (1:) creates a new list but doesn't change the 
    # original list.  It creates a list with the items from 
    # the index, in this case 1:, forward and continues on
    # so the original list is 1,2,3,4,5, the slice list
    # index is 1:. so the slice list becomes 2,3,4,5
    # then, because this is a recursive function it keeps 
    # calling that over and over again until the len of 'n' 
    # (the slice list) becomes 0, at which point the "if"
    # condition triggers

print recurseSum(list1)
