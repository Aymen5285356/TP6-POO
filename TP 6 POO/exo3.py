def rechercher_contact():
    try:
     
        contacts = []
        with open('contacts.txt', 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    try:
                   
                        nom, prenom, telephone, email = ligne.split(',')
                        contacts.append({
                            'nom': nom.strip(),
                            'prenom': prenom.strip(),
                            'telephone': telephone.strip(),
                            'email': email.strip()
                        })
                    except ValueError:
                        print(f"Attention : Format incorrect pour la ligne : '{ligne}'")

        recherche = input("Entrez un nom ou un prénom à rechercher : ").strip().lower()

        resultats = []
        for contact in contacts:
            if (recherche == contact['nom'].lower() or
                    recherche == contact['prenom'].lower()):
                resultats.append(contact)

        if resultats:
            print(f"\n{len(resultats)} contact(s) trouvé(s) :\n")
            for i, contact in enumerate(resultats, 1):
                print(f"Contact {i} :")
                print(f"  Nom : {contact['nom']}")
                print(f"  Prénom : {contact['prenom']}")
                print(f"  Téléphone : {contact['telephone']}")
                print(f"  Email : {contact['email']}")
                print()
        else:
            print(f"Aucun contact trouvé pour '{recherche}'")

    except FileNotFoundError:
        print("Erreur : Le fichier 'contacts.txt' n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

rechercher_contact()
