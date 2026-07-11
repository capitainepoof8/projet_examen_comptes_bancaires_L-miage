#debut code le 9 juin /2026
# creation de la structure de donner et des fonction principal
#modification 10 juin /2026
#avance sur les fonctions
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

# execute test : python group_1_comptes_bancaires.py
#================================ INPORTANT =================================
#si tu fais des modification du code tu a juste a faire :
# git init
# git add .
# git commit -m "nom de la modification"
# git branch -M main
# git push -u origin main

comptes = [
{"numero": 1, "titulaire": "Awa Ndiaye", "solde": 150000},
{"numero": 2, "titulaire": "Moussa Diop", "solde": 75000},
{"numero": 3, "titulaire": "Fatou Sarr", "solde": 320000},
]



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
    
# si tu veut modifier tien compte des indications puis  laisse des commentaire  pour que je sache tes modification   
    #fonction recuper du cour 
def saisir_choix_menu():
    # demande le choix tant qu'il n'est pas entre 1 et 7
    choix = input("Votre choix : ")
    while not choix.isdigit() or int(choix) < 1 or int(choix) > 7:
        print("Erreur : entrez un nombre entre 1 et 7.")
        choix = input("Votre choix : ")
    return int(choix)

def trouver_compte( comptes,numero):
    for compte in comptes:
        if compte ["numero"] == numero:
            return comptes
    return None


 def saisir_numero_compte_existant(compte, message):
     #demande un numero de compte tant qu'il ne correspond a aucun compte existant
  while True:
    numero_comptes=int (input(message))
    
    for compte in comptes:
        if compte ["numero"] == numero_comptes:
            print("compte valide")
            return numero_comptes
    print("compte introuvable, reessayez")

numero_comptes_existant= saisir_numero_compte_existant(comptes, "entrer le numero de compte : ")

 
 def saisir_montant_positif(message):
      #demande un montant tant qu'il n'est pas un nombre strictement positif
    while True:
           montant=float(input(message))
           if not (montant > 0):
               print("le montant doit etre supperieure a 0. recommencez.")
               continue
           return montant 

montant_positif= saisir_montant_posif("entrer un montant : ")


def afficher_comptes(comptes):
    print("=========================les differents comptes==============================")
    for compte in comptes:
        print(compte["numero"], compte["titulaire"], compte["solde"],"cfa")
 
def consulter_solde():
    for compte in comptes:
        print("======================votre solde", compte["titulaire"],"==========================")

# verifie le solde du compte
def solde_valide():
    solde_valide = False
    while not solde_valide:
        enter = input(" votre solde initial (en cfa) : ")
        try:
            solde = float(enter)
            if solde>=0:
                solde_valide = True
            else : 
                print("Erreur !!! votre solde ne peut etre inferieur a 0 ")
        except ValueError:
            print("enter un nombre valide")
def plus_numero():
    for compte in comptes:
        if comptes["numero"]>plus_numero:
            plus_numero =compte["numero"]             
def nouveau_compte():
    nouveau_compte = {"numero":plus_numero+1,"titulaire":titulaire,"solde":solde}
    comptes.append(nouveau_compte)
    print("bravo, compte créé : numero", nouveau_compte["numero"],titulaire,solde,"cfa")


def creer_un_compte():
    titulaire = input("non du client: ")
    # si lutisisateur fais entrer sans renseigner de valeurs
    while titulaire.strip()=="":
        print("erreur!!!!, vous devez renseigner une nom")
        titulaire = input("non du client: ")
    solde_valide()
    plus_numero
    nouveau_compte()
        
# def depot():

# def retrais():

 
# def transfer():


#def main():
def main():
    print("====================Bienvenue à l'Agence CESAG BANK========================")
    quitter = False
    while not quitter:
        menu()
        choix = saisir_choix_menu(menu)
        
    if choix == 1 :
        afficher_comptes(comptes)
    elif choix == 2:
        consulter_solde()
    elif choix==3:
        creer_un_compte()
    elif choix==4:
        depot()
    elif choix==5:
        retrais()
    elif choix==6:
        transfer()
    elif choix ==7:
        print("===============Merci d'avoir utilisé CESAG BANK================")
        print("=========================À bientôt======================")
