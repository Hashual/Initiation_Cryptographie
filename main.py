from Hachage import *

if __name__ == "__main__":
    csv_file = "./LOIZEAU_TP_3_et_4/masterPassword.csv"
    
    master_password = Read_master_password_csv(csv_file)
    if master_password is None:
        print("Aucun mot de passe maître trouvé.")
        master_password = Ask_master_password_csv()
        Write_master_password_csv(csv_file, master_password)

    print("\nMENU :")
    print("1. Générer un mot de passe")
    print("2. Changer le mot de passe maître")
    print("3. Brut force password")
    print("4. Quitter")
    choice = input()
    if choice == "1":
        print("Entrez le tag : ")
        chain = input() 
        while True :
            print("Entrez la taille du mot de passe entre 1 et 12 : ")
            password_lenght = input()
            if password_lenght == "" :
                password_lenght = 8
                print("La taille du mot de passe par défaut est de 8")
                break
            elif int(password_lenght) < 1 or int(password_lenght) > 12:
                print("La taille du mot de passe doit être comprise entre 1 et 12")
            else :
                break
        print("Le mot de passe généré est : ", Primitive_hash(master_password,chain, int(password_lenght)))
    
    elif choice == "2":
            master_password = Ask_master_password_csv()
            Write_master_password_csv(csv_file, master_password)
            print("Le mot de passe maître a été changé.")
    


    elif choice == "3":
        Brut_force_password()
    
    elif choice == "4":
        print("Au revoir")
        
    
    else:
        print("Choix invalide.")