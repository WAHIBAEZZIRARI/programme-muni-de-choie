def main():
    Client = {}
    Compte = {}
    ClientCompte = {}

    while True:
        print("\nMenu:")
        print("1. Ajouter un client")
        print("2. Supprimer un client")
        print("3. Modifier le mot de passe")
        print("4. Déposer de l'argent")
        print("5. Retirer de l'argent")
        print("6. Générer le numéro de compte")
        print("7. Écrire dans un fichier CSV")
        print("8. Manipuler liste, tuple, set")
        print("0. Quitter")

        choix = input("Choisissez une option (0-8): ")

        if choix == '1':
            numCl = input("Entrez le numéro du nouveau client: ")
            MPC = input("Entrez son code secret: ")
            numC = input("Entrez le numéro de son compte: ")
            SoldeC = float(input("Entrez le solde initial de son compte: "))
            ajouter_client(numCl, MPC, numC, SoldeC, Client, Compte, ClientCompte)

        elif choix == '2':
            numC = input("Entrez le numéro du compte à supprimer: ")
            supprimer_client(numC, Client, Compte, ClientCompte)

        elif choix == '3':
            client = input("Entrez le numéro du client: ")
            nouveau_mot_de_passe = input("Entrez le nouveau mot de passe: ")
            modifier_mot_de_passe(client, nouveau_mot_de_passe, Client)

        elif choix == '4':
            client = input("Entrez le numéro du client: ")
            montant = float(input("Entrez la somme à déposer: "))
            deposer_argent(client, montant, Compte, ClientCompte)

        elif choix == '5':
            client = input("Entrez le numéro du client: ")
            montant = float(input("Entrez la somme à retirer: "))
            retirer_argent(client, montant, Compte, ClientCompte)

        elif choix == '6':
            numCl = input("Entrez le numéro du client: ")
            print(f"Numéro de compte généré: {generer_num_compte(numCl)}")

        elif choix == '7':
            ecrire_fichier_csv(Client)

        elif choix == '8':
            liste, t, s = manipuler_sts(ClientCompte)
            print(f"Liste : {liste}")
            print(f"Tuple : {t}")
            print(f"Set : {s}")

        elif choix == '0':
            print("Merci d'avoir utilisé notre application. Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    main()
