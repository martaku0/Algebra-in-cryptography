from math import sqrt   

def brute_force(n):
  p = 2
  while p <= sqrt(n):
    if n % p == 0:
      return (int(n/p), p)
    p += 1
  return -1

print(brute_force(2101644002566781))

