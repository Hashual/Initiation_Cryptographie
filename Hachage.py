import hashlib
import string
import csv
import os


letters = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list(string.punctuation)
full_list = letters + digits + special_characters
LENGHT_LIST = len(full_list)

def deletInvisibleChar(tag: str) -> str:
    # Prend une chaîne de caractères en entrée
    # Supprimer les caractères invisibles de la chaîne de caractères
    # Retourner la chaîne de caractères sans les caractères invisibles

    invisibles = [" ", "\t", "\n", " "]
    for element in invisibles:
        tag = tag.replace(element, "")
    return tag

def Primitive_hash(master_password : str,tag: str, password_lenght : int) -> str:
    # Prend un mot de passe maître, un tag et une longueur de mot de passe en entrée
    # Concatène le mot de passe maître et le tag
    # Supprime les caractères invisibles de la chaîne de caractères concaténée
    # Calcule le hachage SHA-256 de la chaîne de caractères concaténée
    # Convertit le hachage en une chaîne de caractères de longueur password_lenght
    # Retourne la chaîne de caractères de longueur password_lenght

    BYTES_PER_HEX_PAIR = 2
    HEX_BASE = 16
    password = ""

    concatenate = master_password + tag
    characters = deletInvisibleChar(concatenate)
    if characters != concatenate:
        print("Des caractères invisibles ont été supprimés")
    
    hash_function = hashlib.sha256()
    hash_function.update(characters.encode('utf-8'))
    hash_hex = hash_function.hexdigest()

    for element in range(0, password_lenght * BYTES_PER_HEX_PAIR, BYTES_PER_HEX_PAIR):
        part = hash_hex[element:element+BYTES_PER_HEX_PAIR]
        index = int(part, HEX_BASE) % LENGHT_LIST
        password += full_list[index]

    return password

def Read_master_password_csv(csv_file):
    # Prend un fichier CSV en entrée
    # Si le fichier existe, ouvre le fichier en mode lecture sinon retourne None
    # Lit le fichier CSV
    # Retourne le mot de passe maître trouvé ou None si aucun mot de passe maître n'est trouvé

    if os.path.exists(csv_file):
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['mot_de_passe_maitre']
    return None


def Write_master_password_csv(csv_file, master_password):
    # Prend un fichier CSV et un mot de passe maître en entrée
    # Ouvre le fichier en mode écriture
    # Écrit le mot de passe maître dans le fichier CSV

    with open(csv_file, mode='w', newline='') as csvfile:
        fieldnames = ['mot_de_passe_maitre', 'tag', 'date_modification']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'mot_de_passe_maitre': master_password, 'tag': '', 'date_modification': '2024-10-15'})

def Ask_master_password_csv():
    # Demande à l'utilisateur de saisir un nouveau mot de passe maître
    # Supprime les caractères invisibles du mot de passe maître
    # Retourne le mot de passe maître normalisé

    while True:
        new_password = input("Entrez un nouveau mot de passe maître (pas d'espaces) : ").strip()
        normalised_password = deletInvisibleChar(new_password)
        if new_password != normalised_password:
            print("Tous les caractères invisibles ont été supprimés.")
            print("Le mot de passe maître normalisé est  : ", normalised_password)
        else:
            return normalised_password
        
def Master_password_generator(index : int) -> str:
    # Prend un index en entrée
    # Génère un mot de passe maître de 10 caractères
    # Retourne le mot de passe maître

    master_password = ""
    length_list = len(full_list)
    nb_characters = 10

    for i in range(nb_characters):
        character_index = index % length_list
        master_password = master_password + full_list[character_index]
        index //= length_list

    return master_password

def Brut_force_password_one_tag_lenght1():
    # Pratque une attaque par force brute pour trouver un mot de passe maître avec un tag et une longueur de mot de 1
    # Retourne le mot de passe maître trouvé

    counter = 0
    while True:
        temp= Master_password_generator(counter)
        counter += 1
        if Primitive_hash(temp, "Unilim", 1) == "9" :
            break
        else :
            print("Nombre d'essais : ",counter)
        
    print("Le mot de passe maître avec un domaine de colision est : ", temp, " avec un index de ", counter)
    return temp


def Brut_force_password_three_tag_lenght1():
    # Pratque une attaque par force brute pour trouver un mot de passe maître avec trois tags et une longueur de 1
    # Retourne le mot de passe maître trouvé

    counter = 0
    while True:
        temp= Master_password_generator(counter)
        counter += 1
        if Primitive_hash(temp, "Unilim", 1) == "9" and Primitive_hash(temp, "Netflix", 1) == "P" and Primitive_hash(temp, "Amazon",1) == "h":
            break
        else :
            print("Nombre d'essais : ",counter)
        
    print("Le mot de passe maître avec un domaine de colision est : ", temp, " avec un index de ", counter)
    return temp

def Brut_force_password_three_tag_lenght2():
    # Praticque une attaque par force brute pour trouver un mot de passe maître avec trois tags et une longueur de 2
    # La valeure de counter est initialisée à 590_000_000 qui est une valeure proche du domaine de collision pour réduire le temps de calcul
    # Retourne le mot de passe maître trouvé

    counter = 590_000_000
    while True:
        temp= Master_password_generator(counter)
        counter += 1
        if Primitive_hash(temp, "Unilim", 2) == "9F" and Primitive_hash(temp, "Netflix", 2) == "Pl" and Primitive_hash(temp, "Amazon",2) == "hL":
            break
        elif counter % 1_000_000 == 0:
            print("Nombre d'essais : ",counter)
    print("Le mot de passe maître avec un domaine de colision est : ", temp, " avec un index de ", counter)
    return temp

