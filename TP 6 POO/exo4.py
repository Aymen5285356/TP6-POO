import json

def lire_json():
    try:
        with open('utilisateurs.json', 'r', encoding='utf-8') as fichier:
            utilisateurs = json.load(fichier)
        return utilisateurs
    except FileNotFoundError:
        print("Erreur : Le fichier 'utilisateurs.json' n'existe pas.")
        return None
    except json.JSONDecodeError:
        print("Erreur : Le fichier JSON est mal formaté.")
        return None

def manipuler_donnees(utilisateurs):
    if not utilisateurs:
        return

    print("=" * 50)
    print("1. Nombre d'utilisateurs :", len(utilisateurs))

    print("\n2. Liste des utilisateurs :")
    for utilisateur in utilisateurs:
        print(f"   - {utilisateur['prenom']} {utilisateur['nom']}")

    if utilisateurs:
        plus_age = max(utilisateurs, key=lambda x: x['age'])
        print(
            f"\n3. Email de l'utilisateur le plus âgé ({plus_age['prenom']} {plus_age['nom']}, {plus_age['age']} ans) :")
        print(f"   {plus_age['email']}")

    actifs = [u for u in utilisateurs if u.get('actif', False)]
    print(f"\n4. Utilisateurs actifs ({len(actifs)}) :")
    for utilisateur in actifs:
        print(f"   - {utilisateur['prenom']} {utilisateur['nom']} : {utilisateur['email']}")

    print(f"\n5. Nombre d'utilisateurs actifs : {len(actifs)}")
    print("=" * 50)

def sauvegarder_modifications(utilisateurs):
    if not utilisateurs:
        return

    for utilisateur in utilisateurs:
        if utilisateur.get('prenom') == 'Claire' and utilisateur.get('nom') == 'Martin':
            utilisateur['actif'] = True
            print(f"\nStatut modifié pour {utilisateur['prenom']} {utilisateur['nom']} : actif = True")

    with open('utilisateurs_modifies.json', 'w', encoding='utf-8') as fichier:
        json.dump(utilisateurs, fichier, indent=4, ensure_ascii=False)

    print("Données sauvegardées dans 'utilisateurs_modifies.json'")

def main_exercice4():
    utilisateurs = lire_json()
    if utilisateurs:
        manipuler_donnees(utilisateurs)
        sauvegarder_modifications(utilisateurs)

def creer_fichier_test():
    utilisateurs_test = [
        {"nom": "Dupont", "prenom": "Jean", "age": 25, "email": "jean.dupont@email.com", "actif": True},
        {"nom": "Martin", "prenom": "Claire", "age": 30, "email": "claire.martin@email.com", "actif": False},
        {"nom": "Leroy", "prenom": "Pierre", "age": 22, "email": "pierre.leroy@email.com", "actif": True},
        {"nom": "Bernard", "prenom": "Sophie", "age": 35, "email": "sophie.bernard@email.com", "actif": False}
    ]

    with open('utilisateurs.json', 'w', encoding='utf-8') as fichier:
        json.dump(utilisateurs_test, fichier, indent=4, ensure_ascii=False)
    print("Fichier 'utilisateurs.json' créé pour le test.")


# Pour tester, décommentez la ligne suivante :
# creer_fichier_test()
main_exercice4()
