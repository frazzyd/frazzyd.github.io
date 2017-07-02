# Script:  caesar.py
# Desc:    Encrypt and decrypt text with a Caesar cipher
#          using defined character set with index
# Author:  Fraser Dumayne
# Created: 26/09/2016
##########################################################

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # Character Set - Set of characters for encryption/decryption
numchars = len(charset)    # Number of characters available - referred to for wrapping around
        
def caesar_encrypt(plaintext, key):
    """Encrypting a string by altering characters based on alphabetical position"""
	
    print '[*] ENCRYPTING: %s' % (plaintext)
    
    plaintext = plaintext.upper()    # Convert plaintext to upper case characters to avoid using both upper and lower
    ciphertext = ''    # Initialise ciphertext as an empty string   

    for chars in plaintext:    # Iterate through each character in the message ('plaintext') being encrypted
        if chars in charset:    # Make sure that each character exists in the Character Set so that it can be altered correctly
            char_pos = (charset.find(chars) + key) % numchars    # Return the position of the character in the Character Set a number ('key') of places forward
            ciphertext = ciphertext + charset[char_pos]    # Add the new character to the end of the ciphertext
        else:    # The character will remain the same if it isn't located in the Character Set
            ciphertext = ciphertext + chars
 
    print 'Key: %d | Result: %s' % (key, ciphertext.replace(' ', ''))   # Print result without spaces for added security
    return ciphertext    # Returns ciphertext so it can be reused

def caesar_decrypt(ciphertext, key):
    """Reversing the process of encryption"""
    
    ciphertext = ciphertext.upper()
    plaintext= '' 
    
    for chars in ciphertext:    # Iterate through each character in the given message ('ciphertext') to be decrypted
        if chars in charset:
            char_pos = (charset.find(chars) - key) % numchars   # Return the position of the character in the character set a number ('key') of places back
            plaintext = plaintext + charset[char_pos]   # Add the new character to the end of plaintext
        else:
            plaintext = plaintext + chars
            
    print 'Key: %d | Result: %s' % (key, plaintext)
    return plaintext    # Returns plaintext so it can be reused

def caesar_crack(ciphertext):
    """Use all possible keys to decrypt a message for human analysis"""
    
    print '[*] CRACKING: %s' % (ciphertext)
    
    for potential_keys in range(numchars):    # Iterate through character set for every possible key
        crack = caesar_decrypt(ciphertext, potential_keys)    # Call the decrypt function
        
def main():
    # Test Cases
    key = 2    # Number of places to move a character (e.g. if key=3 then A would become D for encryption)
    plain1 = 'Hello Suzanne'    # String to be encrypted
    cipher1 = 'IQQfOQtpKpIGXGtaQPG'    # String to be decrypted
    crackme = 'PBATENGHYNGVBAFLBHUNIRPENPXRQGURPBQRNAQGURFUVSGJNFGUVEGRRA' # String to be cracked
    
    # Call functions with test cases
    caesar_encrypt(plain1, key)
    print '[*] DECRYPTING: %s' % (cipher1)
    caesar_decrypt(cipher1, key)
    caesar_crack(crackme)

# Boilerplate
if __name__ == '__main__':
    main()

