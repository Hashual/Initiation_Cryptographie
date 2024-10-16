import hashlib
import string
import csv
import os

# Liste complète des caractères autorisés (lettres, chiffres et caractères spéciaux)
invisibles = [" ", "\t", "\n", " "]
letters = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list(string.punctuation)
full_list = letters + digits + special_characters
LENGHT_LIST = len(full_list)

def deletInvisibleChar(tag: str) -> str:
    for element in invisibles:
        tag = tag.replace(element, "")
    return tag

def Primitive_hash(master_password : str,tag: str, password_lenght : int) -> str:
    BYTES_PER_HEX_PAIR = 2
    HEX_BASE = 16
    password = ""

    concatenate = master_password + tag
    characters = deletInvisibleChar(concatenate)
    if characters != concatenate:
        print("Des caractères invisibles ont été supprimés")
    
    
    # Calculer le hash SHA-256
    hash_function = hashlib.sha256()
    hash_function.update(characters.encode('utf-8'))
    hash_hex = hash_function.hexdigest()  # Le hash en hexadécimal (64 caractères)

    # Convertir le hash hexadécimal en une chaîne de 8 caractères
    for element in range(0, password_lenght * BYTES_PER_HEX_PAIR, BYTES_PER_HEX_PAIR):  # On prend 2 caractères hex à chaque fois (pour 1 octet)
        # Prendre chaque byte du hash, le convertir en entier et l'utiliser pour indexer full_list
        part = hash_hex[element:element+BYTES_PER_HEX_PAIR]
        index = int(part, HEX_BASE) % LENGHT_LIST  # Utiliser modulo pour rester dans la taille de la liste
        password += full_list[index]  # Ajouter le caractère correspondant

    return password

def Read_master_password_csv(fichier_csv):
    if os.path.exists(fichier_csv):
        with open(fichier_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['mot_de_passe_maitre']  # Retourner le mot de passe maître trouvé
    return None


def Write_master_password_csv(fichier_csv, master_password):
    with open(fichier_csv, mode='w', newline='') as csvfile:
        fieldnames = ['mot_de_passe_maitre', 'tag', 'date_modification']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'mot_de_passe_maitre': master_password, 'tag': '', 'date_modification': '2024-10-15'})

def Ask_master_password_csv():
    while True:
        new_password = input("Entrez un nouveau mot de passe maître (pas d'espaces) : ").strip()
        if ' ' in new_password:
            print("Le mot de passe maître ne peut pas contenir d'espaces.")
        else:
            return new_password
        
def Master_password_generator(index : int , nb_passage : int) -> str:
    master_password = ""
    length_list = len(full_list)
    nb_characters = 10  # Nombre de caractères du mot de passe

    # Boucle pour générer les 10 caractères basés sur l'index
    for i in range(nb_characters):
        # On trouve quel caractère correspond en fonction de l'index
        character_index = index % length_list
        master_password = full_list[character_index] + master_password
        # On divise l'index pour passer au caractère suivant
        index //= length_list

    return master_password


def Brut_force_password():
    compteur = 0
    nb_passage = 0
    while True:
        temp= Master_password_generator(compteur, nb_passage)
        compteur += 1

        if compteur % LENGHT_LIST == 0:
            nb_passage += 1

        if Primitive_hash(temp, "Unilim", 3) == "911":
            break
        else:
            print("Le mot de passe maître sans domaine de colision est : ",temp, "avec",compteur,"essais")
    print("Le mot de passe maître avec un domaine de colision est : ", temp)
    return temp

