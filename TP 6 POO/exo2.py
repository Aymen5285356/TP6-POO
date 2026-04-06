# Exercice 2 - Extraction des majeurs

def extraire_majeurs():
    try:
        majeurs = []

        with open('personnes.txt', 'r') as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:  # Ignorer les lignes vides
                    try:
                        # Séparer le nom et l'âge
                        nom, age_str = ligne.split(',')
                        age = int(age_str.strip())
                        nom = nom.strip()

                        if age >= 18:
                            majeurs.append(nom)
                    except ValueError:
                        print(f"Attention : Format incorrect pour la ligne : '{ligne}'")

        # Écrire les majeurs dans un nouveau fichier
        with open('majeurs.txt', 'w') as fichier_majeurs:
            for nom in majeurs:
                fichier_majeurs.write(nom + '\n')

        print(f"{len(majeurs)} personne(s) majeure(s) trouvée(s). Résultat dans 'majeurs.txt'")

    except FileNotFoundError:
        print("Erreur : Le fichier 'personnes.txt' n'existe pas.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")


# Exécution
extraire_majeurs()