import string

def cesar_cipher(text, key):
	if type(text) == str and type(key) == int:
		return "".join([chr((ord(char) + key) % 1_114_112) for char in text])
	else:
		raise(TypeError)


def cesar_uncipher(crypted_text, key):
		return cesar_cipher(crypted_text, -key)


def hack_cesar_cipher(crypted_text, alphabet):
	if type(crypted_text) == str and type(alphabet) == str:
		for possible_key in range(0, 1_114_112):
			possible_uncryption = cesar_uncipher(crypted_text, possible_key)
			if possible_uncryption[0] in alphabet:
				print(possible_key)
				print(possible_uncryption)
				print("_"*20)
	else:
		raise(TypeError)

#if __name__ == "__main__":
    # message = "le chocolat est bon"
    #cyphered_text = cesar_cipher(message, 32)
    #print(cyphered_text)

   # initial_message = cesar_uncipher(cyphered_text, 32)
   #print(initial_message) 
   # hack_cesar_cipher(cyphered_text, alphabet=string.printable)



def vigenere_cipher(text, password):
    list_of_keys = [ord(char) for char in password]
    crypted_text = []

    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_text.append(cesar_cipher(char, current_key))

    return "".join(crypted_text)


def vigenere_uncipher(text, password):
    original_text = []
    list_of_keys = [ord(char) for char in password]
    for index, char in enumerate(text):
        current_key = list_of_keys[index % len(list_of_keys)]
        decrypted_char = cesar_uncipher(char, current_key)
        original_text.append(decrypted_char)
    return "".join(original_text)



