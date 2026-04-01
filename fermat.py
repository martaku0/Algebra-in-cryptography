from decimal import Decimal
from math import sqrt, ceil
import time

def fermat(n):
  s = sqrt(n)
  if Decimal(s) % 1 == 0:
    return (int(s), int(s))

  a = ceil(s)
  while a <= n:
    b = sqrt(a**2 - n)
    if Decimal(b) % 1 == 0:
      return (int(a+b), int(a-b))
    a += 1

  return -1

n1 = 2101644002566781
n2 = 3593875791313441
n3 = 800090608581732401
n4 = 22601441855002489679

start = time.time()
f = fermat(n1)
end = time.time()
print(f, end - start, 'seconds')

'''
print(fermat(n1))
print(fermat(n2))
print(fermat(n3))
print(fermat(n4))

print(fermat(n1))

print(brute_force(n1))

print(fermat(n2))

print(brute_force(n2))

print(fermat(n3))

print(brute_force(n3))

print(fermat(n4))

print(brute_force(n4))
'''
