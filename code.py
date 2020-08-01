import string, random
def passgen(N):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + '0123456789' + '!@#$%^&*?') for i in range(N))
    
 # Prints a password 16 chars in length. woo.
 print(passgen(16))
