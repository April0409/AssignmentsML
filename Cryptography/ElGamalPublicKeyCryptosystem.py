#Python program for ElGamal Public-key Cryptosystem 
import math
# Quick compute the modular exponentiation 
# Using square-and-multiply method
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

#Compute the Multiplicative inverse with extend-euclidean-algorithm
def mutilInv(b,n):
    a0 = n
    b0 = b
    t0 = 0
    t = 1
    q = int(math.floor(a0/b0))
    r = a0 - q * b0
    while r > 0 : 
        temp = t0 - q * t
        t0 = t
        t = temp
        a0 = b0
        b0 = r
        q = int(math.floor(a0/b0))
        r = a0 - q * b0
    t = t%n
    return t

#Encryption ek(x,k)=(y1,y2); y1 = α^k mod p; y2 = xβ^k mod p
def encryElgamal(p,α,a,x,k):
    β = power(α,a,p)
    y1 = power(α,k,p)
    y2 = power(β,k,p)
    y2 = ((x%p)*y2)%p
    return y1,y2

#Decryption dk(y1,y2) = y2(y1^a)^−1 mod p
def decryElgamal(y1,y2,a,p):
    x = power(y1,a,p)
    x = mutilInv(x,p)
    x = ((y2%p)*x)%p
    return x

#Initialization with example7.1
def main():
    p = 2579
    α = 2
    a = 765
    
    #Alice wished to send the message x = 1299
    #She said k = 853
    #p, α, and β are the public key
    #She did encryption and sent it to Bob
    x = 1299
    k = 853
    y1,y2 = encryElgamal(p,α,a,x,k)
    print("Ciphertext: ( y1 , y2 ) =","(",y1,",",y2,")")

    #Bob received the ciphertext y = (435, 2396), 
    # he computes with secret key a
    x = decryElgamal(y1,y2,a,p)
    print("Plaintext:",x)

if __name__ == '__main__':
    main()
