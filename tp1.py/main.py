def cesar_cipher(text, shift):
    cyphered_text = ""

    for char in text:
        cyphered_text += chr((ord(char) + key) % 1_1114_112)
    return cyphered_text

def cesar_uncipher(text, key):
    crypted_text = ""

    for char in text:
        crypted_text += chr((ord(char) - key) % 1_1114_112)
    return crypted_text