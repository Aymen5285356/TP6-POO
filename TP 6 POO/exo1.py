def calculer_somme_fichier():
    try:
      
        with open('nombres.txt', 'r') as fichier:
            somme = 0
            nombres_lus = 0

            for ligne in fichier:
               
                ligne = ligne.strip()
                if ligne:  
                    try:
                        nombre = float(ligne)
                        somme += nombre
                        nombres_lus += 1
                    except ValueError:
                        print(f"Attention : '{ligne}' n'est pas un nombre valide")

            with open('somme.txt', 'w') as fichier_somme:
                fichier_somme.write(f"La somme des {nombres_lus} nombres est : {somme}")

            print(f"Somme calculée avec succès. Résultat écrit dans 'somme.txt'")

    except FileNotFoundError:
        print("Erreur : Le fichier 'nombres.txt' n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

calculer_somme_fichier()
