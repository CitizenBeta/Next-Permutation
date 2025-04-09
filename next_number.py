# File Name: next_number.py
# Author: Zhang Anjun
# Date: 2025-04-09
# Version: 1.1
# © 2025 Zhang Anjun. All rights reserved.

from sys import exit

# Copyright notice
def copyrightNotice():
    print("")
    print("Author: Zhang Anjun")
    print("Version: 1.1")
    print("© 2025 Zhang Anjun. All rights reserved.")
    print("")

# Shared functions
def listSwap(f,i,j):
    f[i], f[j] = f[j], f[i]

# Check if f is ascending (>=) from f[start] to f[end]
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

# Check if f is descending (<=) from f[start] to f[end]
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
    
# Next Number
def smallerNum(f, length):
    i = length - 1
    while i != 0:
        if ifAscending(f, i, length-1):
            i = i - 1
        else:                                   # f[i] is the first digit that is in descending order
            j = length - 1
            while f[i] <= f[j]:                 # f[j] is the first bigger digit after f[i] (Right to Left)
                j = j - 1
            listSwap(f, i, j)                   # Swap f[i] and f[j]
            reverseSegment(f, i+1, length-1)    # Reverse digits after f[i]
            return f
    return f

def biggerNum(f, length):
    i = length - 1
    while i != 0:
        if ifDescending(f, i, length-1):        # f[j] is the first digit that is in descending order
            i = i - 1
        else:
            j = length - 1
            while f[i] >= f[j]:                 # f[j] is the first smaller digit after f[i] (Right to Left)
                j = j - 1
            listSwap(f, i, j)                   # Swap f[i] and f[j]
            reverseSegment(f, i+1, length-1)    # Reverse digits after f[i]
            return f
    return f

def splitNumber(num):
    i = 0
    f = []
    while i != len(num):
        f.append(int(num[i]))
        i = i + 1
    return f

num = input("Enter a number: ")
f = splitNumber(num)

print("The next smaller number is:", smallerNum(f, len(f)))
f = splitNumber(num)
print("The next bigger number is:", biggerNum(f, len(f)))
copyrightNotice()
input("Press Enter to exit. ")
exit(0)