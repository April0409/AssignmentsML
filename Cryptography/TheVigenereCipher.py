# Python code to implement
# Vigenere Cipher

# Encryption
#eK(x1, x2, . . . , xm) = (x1 + k1, x2 + k2, . . . , xm + km)
def enVigenere(string, key):
	k = len(key)
	cipher_text = ""
	for i in range(len(string)):
		#ASCII code of lower letter range from 97-122
		msgIndex = ord(string[i]) - 97

		#shif with 'add' key[i]
		x = (msgIndex + (key[i%k])) % 26
		x += ord('A')

		#return str
		cipher_text += "" . join(chr(x))
	return cipher_text

# Decryption
#dK(y1, y2, . . . , ym) = (y1 − k1, y2 − k2, . . . , ym − km)
def deVigenere(cipher_text, key):
	k = len(key)
	plain_text = ""
	for i in range(len(cipher_text)):
		#ASCII code of upper letter range from 65-90
		msgIndex = ord(cipher_text[i]) - 65
		
		#shif with 'minus' key[i]
		y = (msgIndex - (key[i%k])) % 26
		y += ord('a')

		# return str
		plain_text += "" . join(chr(y))
	return plain_text
	
#input with example 2.4
if __name__ == "__main__":
	msg = input('please input the message：')
	keyword = input('please enter the key：')
	keyword  = keyword.split(",")
	key = list(map(int, keyword))
	
	cipher_text = enVigenere(msg,key)
	print("Ciphertext :", cipher_text)

	plain_text = deVigenere(cipher_text,key)
	print("Plaintext :",plain_text)
