from math import factorial as fa
from decimal import Decimal as de
from decimal import *

n = int(input())
getcontext().prec = n + 1

def pi(n):
    pi = de(0)
    k = 0
    while k < n:
        pi += (de(-1)**k) * (de(fa(6 * k)) / ((fa(k)**3) * (fa(3 * k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * de(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi

print(pi(n))
