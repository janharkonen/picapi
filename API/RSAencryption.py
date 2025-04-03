def get_power_modulo(m, p, n):
    #this returns c in the equation c === m^p mod n
    c = 1
    for i in range (0, p):
        c = c*m
        if c > n:
            c = c % n
    return c

def encrypt(message: str, d: int, n: int):
    #d is private
    #n is public
    encrypted_message = []
    for char in message:
        unicode = ord(char)

        #tässä encryptataan
        encrypted_unicode = get_power_modulo(unicode, d, n)
        
        encrypted_message.append(encrypted_unicode)
    return encrypted_message

def decrypt(encrypted_message: str, e: int, n: int):
    #e is public
    #n is public
    decrypted_message = []
    for unicode in encrypted_message:

        #tässä decryptataan
        decrypted_unicode = get_power_modulo(unicode,e,n)
        
        decrypted_char = chr(decrypted_unicode)
        decrypted_message.append(decrypted_char)
    return ''.join(decrypted_message)

if __name__ == '__main__':
    message = 'ThisMessageIsOK'
    encrypted_message = encrypt(message, 53, 527)
    decrypted_message = decrypt(encrypted_message, 77, 527)
    print('message: ', repr(message))
    print('encrypted_message: ', repr(encrypted_message))
    print('decrypted_message: ', repr(decrypted_message))