from Hachage import *

if __name__ == "__main__":
    fichier_csv = "masterPassword.csv"
    
    mot_de_passe_maitre = lire_mdp_maitre_csv(fichier_csv)
    if mot_de_passe_maitre is None:
        print("Aucun mot de passe maître trouvé.")
        mot_de_passe_maitre = demander_nouveau_mdp_maitre()
        ecrire_mdp_maitre_csv(fichier_csv, mot_de_passe_maitre)

    print("\nMENU :")
    print("1. Générer un mot de passe")
    print("2. Changer le mot de passe maître")
    print("3. Quitter")
    choice = input()
    if choice == "1":
        print("Entrez la première chaine de caractères : ")
        chain1 = input()
        print("Entrez la deuxième chaine de caractères : ")
        chain2 = input() 
        while True :
            print("Entrez la taille du mot de passe entre 8 et 12 : ")
            passwordLenght = input()
            if passwordLenght == "" :
                passwordLenght = 8
                print("La taille du mot de passe par défaut est de 8")
                break
            elif int(passwordLenght) < 8 or int(passwordLenght) > 12:
                print("La taille du mot de passe doit être comprise entre 8 et 12")
            else :
                break
        print("Le mot de passe généré est : ", hachagePrimitif(chain1, chain2, int(passwordLenght)))
    
    elif choice == "2":
            mot_de_passe_maitre = demander_nouveau_mdp_maitre()
            ecrire_mdp_maitre_csv(fichier_csv, mot_de_passe_maitre)
            print("Le mot de passe maître a été changé.")
    
    elif choice == "3":
        print("Sortie...")
        
    
    else:
        print("Choix invalide.")