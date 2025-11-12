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





def vigenere_cipher(text, password):
	list_of_keys = [ord(char) for char in password]
	crypted_text = []
	for index, char in enumerate(text):
		current_key = list_of_keys[index%len(list_of_keys)]
		crypted_text.append(cesar_cipher(char,ord(current_key)))
	return crypted_text

def vigener_uncipher(text, password):
	original_text = []
	list_of_keys = [ord(char) for char in password]
	for index,char in enumerate(text):
		current_key = list_of_keys[index%len(list_of_keys)]
		original_text.append( cesar_uncipher(char,ord(current_key)))
	return original_text


