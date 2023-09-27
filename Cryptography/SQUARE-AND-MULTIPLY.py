#Python program to compute the Square-and-Multiply
# Alice encrypts the plaintext 9726 by computing 9726^3533 mod 11413

import math

#define the func to get the binary repr of a num
def getBinaryRepr(b):
    c = format(b,'b')
    print("binary represetation of b:",c)
    c1 = list(c)
    c1 = [int(num) for num in c1]
    return c1

#define the func SquareAndMultiply
def SquareAndMultiply(n,b,x):
    c = getBinaryRepr(b)
    l = len(c)
    z = 1
    ztemp = z 
    i = l-1
    #It is computed from l-1,so we need to reverse the array of c
    c.reverse()
    #print the calculation process as follow
    print("i   "," bi   "," z   ")
    while(i >= 0):
        ztemp = z
        z = (z*z)%n
        if(c[i]==1):
            z = (z*x)%n
            print(i,"   ",c[i],"   ",ztemp,"^2","*",x,"=",z)
        else:
            print(i,"   ",c[i],"   ",ztemp,"^2 =",z)
        i=i-1
    return z

#the initialization of example6.5
n = 11413
b = 3533
x = 9726 
ciphertext = SquareAndMultiply(n=n,b=b,x=x)
print("ciphertext:",ciphertext)





