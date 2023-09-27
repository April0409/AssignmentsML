# Python program for RSA Parameter Generation
import math
import random

def ifPrime(n):
    flag = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = 0
            break
    return flag

# step 1: Generate two large primes, p and q, such that p != q
def genTwoPrime():
    p = random.randint(1000,6000) # random int between 1000 and 6000
    while (ifPrime(p) == 0):
        p = random.randint(1000,6000)
    q = random.randint(1000,6000)
    while (ifPrime(q) == 0):
        q = random.randint(1000,6000)
        if (q == p):
            q=4000 #repeat the random function if q==p
    return p,q

# step 2  n ← pq 
p,q = genTwoPrime()
n = p*q
# φ(n) ← (p − 1)(q − 1)
phi = (p-1)*(q-1)

# step 3  Choose a random b (1 < b < φ(n)) such that gcd(b, φ(n)) = 1
def randomB(phi):
    b = 2000 #generate a little bigger b
    while(b<phi):
        if (math.gcd(b, phi) == 1):
            break
        else:
           b += 1
    return b

# step 4  a ← b−1 mod φ(n)
def secretDecryptionExponent(b,phi):
    k = 1
    while( (k*phi+1)%b > 0):
       k += 1
       a = int((k*phi+1)/b)
    return a

#step5 The public key is (n, b) 
# The private key is (p, q, a)
b = randomB(phi)
a = secretDecryptionExponent(b,phi)
print("Public key:   b", b," n:",n)
print("Private key:  p：",p," q:",q," a:",a)

