import numpy as np
import math


# simple selection sort
def selectSort(arr):
    for i in range(len(arr)):
        m = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[m]: m = j
        (arr[i], arr[m]) = (arr[m], arr[i])
    return arr


# check if integer x > 0 is prime
def isPrime(x):
    if x < 2: return False
    if x > 2 and x % 2 == 0: return False
    for i in range(3, int(np.sqrt(x))+1, 2):
        if x % i == 0: return False
    return True


# return ordered list of prime factors of integer n
def primeFactors(n):
    temp, i = n, 2
    factors = []

    if n == 1: return [1]
    if isPrime(n): return [n]

    while i < int(np.sqrt(temp))+1:
        if temp % i == 0:
            factors.append(i)
            temp //= i
            i = 2
        else: i += 1

    if temp > 1: factors.append(int(temp))
    return factors


# returns ordered list of factors of integer x
def factorsList(n):
    factors = []
    if n == 0: return [0]
    if n == 1: return [1]

    factors.append(1)
    for i in range(2, int(np.sqrt(n))+1):
        if n%i == 0:
            factors.append(i)
            if i != n//i: factors.append(n//i)
    factors.append(n)
    return selectSort(factors)


# return reverse-ordered list of digits of integer x
def digitList(x):
    digits = []
    while x != 0:
        digits.append(x % 10)
        x -= x % 10
        x //= 10
    return digits


# return maximum and its index in list of integers as list
def maxAndIndex(arr):
    max = arr[0]
    ind = 0
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            ind = i
    return max, ind


# returns n choose k for integers n > k
def chooseFunction(n, k):
    nume, denom1, denom2 = 1, 1, 1
    for i in range(1, n+1):
        nume *= i
        if i <= k: denom1 *= i
        if i <= n-k: denom2 *= i
    return nume // (denom1*denom2)
