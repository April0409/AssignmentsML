# Python program to demonstrate working of extended
# Euclidean Algorithm
import math	
# function for extended Euclidean Algorithm
def gcdExtended(a, b):
	a0 = a
	b0 = b
	t0 = 0
	t = 1
	s0 = 1
	s = 0
	q = int(math.floor(a0/b0))
	r = a0 - q * b0
	while r > 0 : 
		temp = t0 - q * t
		t0 = t
		t = temp
		temp = s0 - q*s
		s0 = s
		s = temp
		a0 = b0
		b0 = r
		q = int(math.floor(a0/b0))
		r = a0 - q * b0
	r = b0
	return r,s,t

# Driver code
a, b = 35,15
r, s, t = gcdExtended(a, b)
print("gcd(", a , "," , b, ") = ", r)
