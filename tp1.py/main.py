import string
def cesar_cipher(text, shift):
<<<<<<< HEAD
    cyphered_text = ""

    for char in text:
        cyphered_text += chr((ord(char) + key) % 1_1114_112)
    return cyphered_text

def cesar_uncipher(text, key):
    crypted_text = ""

    for char in text:
        crypted_text += chr((ord(char) - key) % 1_1114_112)
    return crypted_text

=======
    crypted_text = ""

    for char in text:
        crypted_text += chr((ord(char) + shift) % 1_1114_112)
    return crypted_text

def cesar_uncipher(crypted_message, key):
    return cesar_cipher(crypted_message, -key)

def hack_cesar_cipher(crypted_message,alphabet):
    for possible_key in range(0,1_1114_112):
        possible_uncryption = cesar_uncipher(crypted_message, possible_key)
        if possible_uncryption[0] in alphabet:
            print(possible_key)
            print(possible_uncryption)
            print("_"*20)



>>>>>>> 000d7ab (Mise à jour de main.py dans tp1)

