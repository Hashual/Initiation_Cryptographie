import hashlib
import string
import csv
import os

# Liste complète des caractères autorisés (lettres, chiffres et caractères spéciaux)
invisibles = [" ", "\t", "\n", " "]
letters = list(string.ascii_letters)
chiffres = list(string.digits)
caracteres_speciaux = list(string.punctuation)
liste_complete = letters + chiffres + caracteres_speciaux

def deletInvisibleChar(chain: str) -> str:
    for element in invisibles:
        chain = chain.replace(element, "")
    return chain

def hachagePrimitif(chain1: str, chain2: str, passwordLenght : int) -> str:
    BYTES_PER_HEX_PAIR = 2
    HEX_BASE = 16
    taille_liste = len(liste_complete)
    mot_de_passe = ""

    concatene = chain1 + chain2
    caracteres = deletInvisibleChar(concatene)
    if caracteres != concatene:
        print("Des caractères invisibles ont été supprimés")
    
    
    # Calculer le hash SHA-256
    fonctionHachage = hashlib.sha256()
    fonctionHachage.update(caracteres.encode('utf-8'))
    hash_hex = fonctionHachage.hexdigest()  # Le hash en hexadécimal (64 caractères)

    # Convertir le hash hexadécimal en une chaîne de 8 caractères
    for i in range(0, passwordLenght * BYTES_PER_HEX_PAIR, BYTES_PER_HEX_PAIR):  # On prend 2 caractères hex à chaque fois (pour 1 octet)
        # Prendre chaque byte du hash, le convertir en entier et l'utiliser pour indexer liste_complete
        morceau = hash_hex[i:i+BYTES_PER_HEX_PAIR]
        index = int(morceau, HEX_BASE) % taille_liste  # Utiliser modulo pour rester dans la taille de la liste
        mot_de_passe += liste_complete[index]  # Ajouter le caractère correspondant

    return mot_de_passe

def lire_mdp_maitre_csv(fichier_csv):
    if os.path.exists(fichier_csv):
        with open(fichier_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row['mot_de_passe_maitre']  # Retourner le mot de passe maître trouvé
    return None


def ecrire_mdp_maitre_csv(fichier_csv, mdp_maitre):
    with open(fichier_csv, mode='w', newline='') as csvfile:
        fieldnames = ['mot_de_passe_maitre', 'tag', 'date_modification']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'mot_de_passe_maitre': mdp_maitre, 'tag': '', 'date_modification': '2024-10-15'})

def demander_nouveau_mdp_maitre():
    while True:
        nouveau_mdp = input("Entrez un nouveau mot de passe maître (pas d'espaces) : ").strip()
        if ' ' in nouveau_mdp:
            print("Le mot de passe maître ne peut pas contenir d'espaces.")
        else:
            return nouveau_mdp

