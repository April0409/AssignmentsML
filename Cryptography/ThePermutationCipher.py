#Python program for The Permutation Cipher
import math
#Input the key from example 2.7
key = input('please enter the key：')

# Encryption: eπ(x1, . . . , xm) = (xπ(1), . . . , xπ(m))
def encryPermutation(msg):
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    #the colum num of msg matrix   
    col = len(key)

    # compute the row number of the permutation 
    row = int(math.ceil(msg_len / col))

    # fill the empty of the msg_list with "_" 
    emptyNum = int((row * col) - msg_len)
    msg_lst.extend('_' * emptyNum)

    #contruct msg matrix row by row
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]
    
    #construct ciper matrix
    cipher = []
    for _ in range(row):
        cipher += [[None] * col]

    #encrypting with π(x) permutation
    k_index = 0
    for _ in range(col):
        #use curr_index  as π(x)-box
        curr_idx = key_lst.index(key[k_index])

        for j in range(row):
            cipher[j][k_index] = matrix[j][curr_idx]
        k_index += 1 

    #tran-str
    ciphertext = ''.join(sum(cipher, []))
    return ciphertext


#Decryption:dπ(y1, . . . , ym) = (yπ^−1(1), . . . , yπ^−1(m))
def decryPermutation(cipher):
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))

    ##contruct cipher_msg matrix
    emptyNum = int((row * col) - msg_len)
    msg_lst.extend('_' * emptyNum)
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]
    
    # construct de_ciper matrix
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    #decrypting with permutation
    plaintext = ""
    k_index = 0
    for _ in range(col):
        #use curr_index  as π(x)-box
        curr_idx = key.index(key_lst[k_index]) 

        for j in range(row):
            dec_cipher[j][k_index] = matrix[j][curr_idx]
        k_index += 1
    
    plaintext = ''.join(sum(dec_cipher, []))
    return plaintext

#input the msg from example 2.7
msg = input('please input the message：')
cipher = encryPermutation(msg)
print("ciphertext:",cipher.upper())
plaintext = decryPermutation(cipher)
print("plaintext:",plaintext)