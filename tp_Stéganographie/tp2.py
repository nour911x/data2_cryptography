import cv2
import numpy as np

# exercises 1 et 2 


# Charger l'image
image1 = cv2.imread("C:\\Users\\ThinkPad\\Downloads\\ninjastars.jpg") #imread() lit mon image et la stocke sous forme d’un tableau numPy , chaque pixel contient trois valeurs bleu roige vert

if image1 is None:
    print("Erreur : impossible de charger l'image")
else:
    print(" Image chargée")
    print(f"  Taille originale : {image1.shape}") # .shape pour obtenir les dimensions de l'image

    # Nouvelles dimensions
    image_finale = cv2.resize(image1, (800, 600))#resize() pour redimensionner l'image
    
    # Convertir en gris
    image_gris = cv2.cvtColor(image_finale, cv2.COLOR_BGR2GRAY)
    # on convertis l’image en gris parce que c plus facile 1 seule valeur par pixel
    print(f"  Taille finale grise : {image_gris.shape}")
    
    # Afficher l'image finale
    cv2.imshow("Image Finale", image_gris)      #imshow() ouvre une fenêtre avec l’image
    cv2.waitKey(0)                              #waitKey(0) attend que j'appuie sur une touche.
    cv2.destroyAllWindows()                     #destroyAllWindows() ferme toutes les fenêtres.



# Fonction : afficher un pixel

def afficher_pixel(image, x, y):
    valeur = image[y, x] # image[y, x]  lit la valeur du pixel
    valeur_binaire = format(valeur, '08b') # transforme la valeur en binaire sur 8 bits
    print(f"\nPixel à ({x}, {y})")
    print(f"Valeur : {valeur}")
    print(f"Binaire : {valeur_binaire}")
    print(f"LSB : {valeur_binaire[-1]}") #récupère le bit le moins significatif

afficher_pixel(image_gris, 100, 50) #On l’appelle pour voir un pixel



# EXERCICE 3 : Encodage LSB1


# Question 3.1 : Texte  binaire
def texte_vers_binaire(texte):
    binaire = ''.join(format(ord(char), '08b') for char in texte) #ord(char) obtient le code ASCII de chaque caractère , format(..., '08b') convertit ce code en une chaîne binaire sur 8 bits , ''.join(...) concatène toutes ces chaînes binaires en une seule grande chaîne.
    print(f"\nTexte '{texte}' → {len(binaire)} bits")
    return binaire

# Question 3.2 : Convertir pixels en pairs
def convertir_pixels_pairs(image):
    image_paire = image.copy()
    image_paire = image_paire & 0xFE #0xFE = 254 (décimal) = 11111110 (binaire) met le dernier bit à 0 et rend la valeur paire
                
    pixels_modifies = np.sum(image != image_paire) # on compare pixel par pixel les deux images ,l'image original et limage paire , Le résultat est un tableau booléen (True / False) / pixels_modifies = le nombre total de pixels qui ont été modifiés pour devenir pairs.
    print(f"\nPixels modifiés : {pixels_modifies} / {image.size}")
    return image_paire

# Question 3.3 : Encoder un message LSB1
def encoder_message_lsb1(image, message):
    message_binaire = texte_vers_binaire(message)
    delimiteur = '0' * 32 #Cette ligne crée une chaîne composée de 32 zéros consécutifs ,on va  s’en servir comme marqueur de fin de message. 
    message_complet = message_binaire + delimiteur
#Vérifie que le message tient dans l’image.
    if len(message_complet) > image.size:
        raise ValueError("message trop long pour l'image")
    
    print(f"Capacité : {image.size} bits") #La capacité = nombre total de pixels = nombre total de bits qu’on peut cacher
    print(f"Message : {len(message_complet)} bits") #compte le nombre total de bits du message à cacher.
    print(f"Utilisation : {len(message_complet)/image.size*100:.2f}%") #le pourcentage d’utilisation.
    
    image_encodee = image.copy()
    pixels = image_encodee.flatten() #flatten() transforme le tableau 2D en tableau 1D c plus facile pour parcourir les pixels dans une seule liste
    
    for index, bit in enumerate(message_complet):
        #On ne modifie le pixel que si le bit à cacher est un '1'.
        if bit == '1':
            pixels[index] = pixels[index] | 1 # OR binaire  | 1 : Si le dernier bit est 0 → devient 1 , Si le dernier bit est déjà 1 → reste 1


    
    image_encodee = pixels.reshape(image.shape)
    print(" Message encodé ")
    return image_encodee



# EXERCICE 4 : Décodage LSB1
#on récupère le dernier bit de chaque pixel pour reconstruire le message binaire.

def decoder_message_lsb1(image):
   
    print("\n  Décodage du message ")
    
    pixels = image.flatten()
    bits = [str(pixel & 1) for pixel in pixels] # On convertit le 0 ou 1 obtenu en chaîne de caractères, pour pouvoir ensuite construire une chaîne binaire complète.pixel & 1 récupère le bit le moins significatif du pixel.
    #Cherche le délimiteur de 32 zéros → c’est la fin du message
    message_binaire = ''.join(bits)
    delimiteur = '0' * 32
    position_fin = message_binaire.find(delimiteur)
    
    if position_fin == -1:
        print(" Délimiteur non trouvé")
        message_binaire = message_binaire[:1000]
    else:
        print(f" Délimiteur trouvé à la position {position_fin} bits")
        message_binaire = message_binaire[:position_fin]
    
    message = ''
    for index in range(0, len(message_binaire), 8):
        octet = message_binaire[index:index+8]
        if len(octet) == 8:
            message += chr(int(octet, 2))
    
    print(f" Message décodé : {len(message)} caractères")
    return message

# TEST COMPLET : ENCODAGE ET DÉCODAGE

print("\n" + "="*70)
print("TEST COMPLET : ENCODAGE ET DÉCODAGE")
print("="*70)

# Encodage
image_paire = convertir_pixels_pairs(image_gris)
message_original = "Bonjour , voci le mot de passe : xxxZ137yyy !!!"
image_encodee = encoder_message_lsb1(image_paire, message_original)
cv2.imwrite("image_encodee.png", image_encodee)
print("\n✓ Image sauvegardée : image_encodee.png")

# Décodage
message_decode = decoder_message_lsb1(image_encodee)
print(f"Message décodé : '{message_decode}'")

# Comparaison
print("\n" + "="*70)
print("COMPARAISON FINALE")
print("="*70)
print(f"Message original : '{message_original}'")
print(f"Message décodé   : '{message_decode}'")
print(f"Longueur originale : {len(message_original)} caractères")
print(f"Longueur décodée   : {len(message_decode)} caractères")

if message_original == message_decode:
    print("\n SUCCÈS ! Les messages sont identiques !")
else:
    print("\n ERREUR ! Les messages sont différents !")

# Affichage des images et de la différence
difference = np.abs(image_gris.astype(int) - image_encodee.astype(int))
difference_affichage = np.clip(difference * 100, 0, 255).astype(np.uint8)

cv2.imshow("Image Originale", image_gris)
cv2.imshow("Image Encodée", image_encodee)
cv2.imshow("Différence (x100)", difference_affichage)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n✓✓✓ EXERCICES 3, 4 ET 5 TERMINÉS AVEC SUCCÈS !")
