from Hachage import *

if __name__ == "__main__":
    print("MENU :")
    print("1. Générer un mot de passe")
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

    else :
        print("Choix invalide")