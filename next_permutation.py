# File Name: next_permutation.py
# Author: Zhang Anjun
# Date: 2025-04-13
# Version: 1.4
# © 2025 Zhang Anjun. All rights reserved.

from sys import exit

# Copyright notice
def copyrightNotice():
    print("")
    print("Author: Zhang Anjun")
    print("Version: 1.4")
    print("© 2025 Zhang Anjun. All rights reserved.")
    print("")

def listSwap(f,i,j):
    f[i], f[j] = f[j], f[i]

# Check if f is ascending (<=) from f[start] to f[end]
def ifAscending(f, start, end):
    if end - start == 0:
        return True
    i = start
    while f[i] <= f[i+1] and i != end-1:
        i = i + 1
    if f[i] > f[i+1]:
        return False
    else:
        return True

# Check if f is descending (>=) from f[start] to f[end]
def ifDescending(f, start, end):
    if end - start == 0:
        return True
    i = start
    while f[i] >= f[i+1] and i != end-1:
        i = i + 1
    if f[i] < f[i+1]:
        return False
    else:
        return True

def reverseSegment(f, start, end):
    i = 0
    stop = ((end-start)+1) // 2
    while i != stop:
        listSwap(f, start+i, end-i)
        i = i + 1
    return f

def findRightSmaller(f, length, i):
    j = length - 1
    while f[j] >= f[i]:
        j = j - 1
    return j

def findRightBigger(f, length, i):
    j = length - 1
    while f[j] <= f[i]:
        j = j - 1
    return j

# Next smaller permutation
def smallerNum(f, length):
    i = length - 2
    while i != -1:
        if ifAscending(f, i, length-1):         # f[i] is the first digit that is in descending order
            i = i - 1
        else:
            j = findRightSmaller(f, length, i)  # f[j] is the first smaller digit after f[i] (Right to Left)
            listSwap(f, i, j)                   # Swap f[i] and f[j]
            reverseSegment(f, i+1, length-1)    # Reverse digits after f[i]
            return f
    return f

# Next bigger permutation
def biggerNum(f, length):
    i = length - 2
    while i != -1:
        if ifDescending(f, i, length-1):        # f[i] is the first digit that is in descending order
            i = i - 1
        else:
            j = findRightBigger(f, length, i)   # f[j] is the first bigger digit after f[i] (Right to Left)
            listSwap(f, i, j)                   # Swap f[i] and f[j]
            reverseSegment(f, i+1, length-1)    # Reverse digits after f[i]
            return f
    return f

def splitNum(num):
    i = 0
    f = []
    while i != len(num):
        f.append(int(num[i]))
        i = i + 1
    return f

num = input("Enter a number: ")
f = splitNum(num)
print("The next smaller permutation is:", smallerNum(f.copy(), len(f)))
print("The next bigger permutation is:", biggerNum(f.copy(), len(f)))
copyrightNotice()
input("Press Enter to exit. ")
exit(0)