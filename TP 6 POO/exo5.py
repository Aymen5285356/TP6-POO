# Exercice 5 - Gestion des notes avec exceptions

def calculer_moyenne_notes():
    notes_valides = []

    try:
        with open('notes.txt', 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()

            print("Lecture des notes des étudiants :\n")

            for numero_ligne, ligne in enumerate(lignes, 1):
                ligne = ligne.strip()
                if not ligne:  # Ignorer les lignes vides
                    continue

                try:
                    # Séparer le nom et la note
                    parties = ligne.split(',')
                    if len(parties) != 2:
                        raise ValueError("Format incorrect (attendu: Nom,Note)")

                    nom = parties[0].strip()
                    note_str = parties[1].strip()

                    # Convertir la note en nombre
                    try:
                        note = float(note_str)
                        if note < 0 or note > 20:
                            print(f"Attention : Note invalide ({note}) pour {nom} - doit être entre 0 et 20")
                            continue
                        notes_valides.append(note)
                        print(f"✓ {nom} : {note}")
                    except ValueError:
                        print(f"✗ Erreur ligne {numero_ligne} : '{note_str}' n'est pas un nombre valide pour {nom}")

                except ValueError as e:
                    print(f"✗ Erreur ligne {numero_ligne} : {e}")
                except Exception as e:
                    print(f"✗ Erreur inattendue ligne {numero_ligne} : {e}")

    except FileNotFoundError:
        print("Erreur : Le fichier 'notes.txt' n'existe pas.")
        return
    except PermissionError:
        print("Erreur : Permission refusée pour lire le fichier 'notes.txt'.")
        return
    except Exception as e:
        print(f"Erreur inattendue lors de l'ouverture du fichier : {e}")
        return

    # Afficher la moyenne des notes valides
    print("\n" + "=" * 40)
    if notes_valides:
        moyenne = sum(notes_valides) / len(notes_valides)
        print(f"Nombre de notes valides : {len(notes_valides)}")
        print(f"Moyenne des notes : {moyenne:.2f}/20")
    else:
        print("Aucune note valide trouvée pour calculer la moyenne.")
    print("=" * 40)


# Exécution
calculer_moyenne_notes()