#debut code le 9 juin /2026
# creation de la structure de donner et des fonction principal
#debut code le 9 juin /2026
#=============stcture code =========================

# base de donnee
# -----------------------la fonctions menu
# -----------------------la fonction de choix
# -----------------------la fonction de 

#===== AGENCE CESAG BANK =====
# 1. Afficher tous les comptes
# 2. Consulter le solde d'un compte
# 3. Creer un nouveau compte
# 4. Effectuer un depot
# 5. Effectuer un retrait
# 6. Effectuer un transfert entre deux comptes
# 7. Quitter
#==============================
# Votre choix :


comptes = [
{"numero": 1, "titulaire": "Awa Ndiaye", "solde": 150000},
{"numero": 2, "titulaire": "Moussa Diop", "solde": 75000},
{"numero": 3, "titulaire": "Fatou Sarr", "solde": 320000},
]
# si tu veut modifier tien compte des indications puis  laisse des commentaire  pour que je sache tes modification   
    #fonction recuper du cour 
def saisir_choix_menu():
    # demande le choix tant qu'il n'est pas entre 1 et 7
    choix = input("Votre choix : ")
    while not choix.isdigit() or int(choix) < 1 or int(choix) > 7:
        print("Erreur : entrez un nombre entre 1 et 7.")
        choix = input("Votre choix : ")
    return int(choix)

# def trouver_compte():
 
# def saisir_numero_compte_existant():
 
# def saisir_montant_positif():

# def afficher_comptes():
 
# def consulter_solde():

# def creer_compte():
 
# def deposer():

# def retirer():

 
# def transferer():

def menu():
    print("\n===== AGENCE CESAG BANK =====")
    print("1. Afficher tous les comptes")
    print("2. Consulter le solde d'un compte")
    print("3. Créer un nouveau compte")
    print("4. Effectuer un dépôt")
    print("5. Effectuer un retrait")
    print("6. Effectuer un transfert entre deux comptes")
    print("7. Quitter")
    print("==============================")
# def main():
# ici ont devra cree des chois avec en condition qui retourne les diferent fonction