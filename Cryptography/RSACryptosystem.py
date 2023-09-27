# Python program for RSA Cryptosystem.
# example 6.5
import math
#calculate Bob's secret decryption exponent a
def secretDecryptionExponent(b,phi):
	print("phi:",phi)
	a0 = phi
	b0 = b
	t0 = 0
	t = 1
	q = int(a0/b0)
	r = a0 - q * b0
	while r > 0 : 
		temp = t0 - q * t
		t0 = t
		t = temp
		a0 = b0
		b0 = r
		q = int(a0/b0)
		r = a0 - q * b0
	t = t%phi
	return t

#initialization with example6.5
p = 101
q = 113
n = p*q
phi = (p-1)*(q-1)
b = 3533 
a = secretDecryptionExponent(b,phi)
print("Public key:   b", b," n:",n)
print("Private key:  p：",p," q:",q," a:",a)

#Alice wants to encryption the plaintext 9726
#encrypted ek(x) = (x ^ b) % n with public key b
x = 9726
y = pow(x, b) % n
print("Ciphertext = ", y)

#Bob Decrypted dk(y) = (y ^ a) % n with secrect key a
x = pow(y, a) % n
print("Plaintext = ", x)