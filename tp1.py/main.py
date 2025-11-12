import string
def cesar_cipher(text, key):
    if type(text) == str and type(key) == int : 
        return "".join([chr((ord(char) + key) % 1_1114_112) for char in text])
    else:
        raise TypeError


def cesar_uncipher(text, key):
    if type(text) == str and type(key) == int:
        return "".join([chr((ord(char) - key) % 1_1114_112) for char in text])
    else:
        raise TypeError

    for char in text:
        crypted_text += chr((ord(char) - key) % 1_1114_112)
    return crypted_text

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

if __name__ == "__main__":
    message = "le chocolat est bon"
    cyphered_text = cesar_cipher(message, 32)
    print(cyphered_text)

    initial_message = cesar_uncipher(cyphered_text, 32)
    print(initial_message)
    
    hack_cesar_cipher(cyphered_text, alphabet=string.printable)


def vigenere_cipher (text, password):
    list_of_keys=[ord(char) for char in password]
  crypted_text = []
  length = len(list_of_keys)
  for index, char in enumerate(text):
    current_key= list_of_keys[index % length]
    crypted_text.append(chr((ord(char) + current_key) % 1114111))
  return "".join(crypted_text)

def vigenere_decipher(text, password):
    key_values = [ord(char) for char in password]
    decrypted_chars = []
    key_length = len(key_values)

    for index, char in enumerate(text):
        current_key = key_values[index % key_length]
        decrypted_chars.append(chr((ord(char) - current_key) % 1114111))

    return "".join(decrypted_chars)

