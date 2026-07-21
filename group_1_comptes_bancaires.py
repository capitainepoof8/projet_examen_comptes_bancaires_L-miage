# non et premon goupe 1:
# menbre 1 : Soro Nontie Emmanuel
# menbre 2 : Esmel Priscille Ange


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
            return compte
    return None


def saisir_numero_compte_existant(comptes,message):
    numero = input(message)
    while not numero.isdigit() or trouver_compte(comptes, int(numero)) is None:
        print("ce compte n'existe pas")
        numero = input(message)
    return int(numero)

def saisir_montant_positif(message):
    # demande un montant tant qu'il n'est pas strictement positif
    montant_valide = False
    while not montant_valide:
        enter = input(message)
        try:
            montant = float(enter)
            if montant > 0:
                montant_valide = True
            else:
                print("Erreur : le montant doit être supérieur à 0")
        except ValueError:
            print("enter un nombre valide")
    return montant

def afficher_comptes(comptes):
    print("========================= les comptes chez nous ==============================")
    for compte in comptes:
        print(compte["numero"], compte["titulaire"], compte["solde"],"cfa")
 
def consulter_solde():
    for compte in comptes:
        print("====================== votre solde", compte["titulaire"]," ==========================")

# verifie le solde du compte
def solde_valide():
    solde_valide = False
    solde = None
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
    return solde


def consulter_solde(comptes):
    #demende d'un compte existants puis ont  affichons le solde
    numero = saisir_numero_compte_existant(comptes, "numero du compte : ")
    compte = trouver_compte(comptes,numero)
    print("\n======================================*************  bonjour  ************=============================================")
    print("================  compte utilisateur :", compte["titulaire"],", votre solde est de :", compte["solde"], "cfa===============================")

def plus_numero():
    # cherche le plus grand numero de compte existant
    plus_grand = 0
    for compte in comptes:
        if compte["numero"] > plus_grand:
            plus_grand = compte["numero"]
    return plus_grand


def nouveau_compte(titulaire, solde):
    nouveau_numero = plus_numero() + 1
    nouveau_compte = {"numero": nouveau_numero,"titulaire": titulaire, "solde": solde}
    comptes.append(nouveau_compte)
    print("felicitation pour votre compte créé : numero", nouveau_compte["numero"], titulaire ,solde,"cfa")
    

def creer_un_compte(comptes):
    titulaire = input("non du client: ")
    # si lutisisateur fais entrer sans renseigner de valeurs dans la console
    while titulaire.strip()=="":
        print("erreur!!!!, vous devez renseigner une nom")
        titulaire = input("non du client: ")
    solde = solde_valide()
    nouveau_compte(titulaire, solde)


def depot(comptes):
    # ont recupere le compte si valide ont credite (depose de largent ) le compte
    numero = saisir_numero_compte_existant(comptes, "numero du compte a credite : ")
    montant = saisir_montant_positif("montant a deposer : ")
    compte = trouver_compte(comptes, numero)
    compte["solde"] = compte["solde"] + montant
    print("depot effectué.",)
    print("votre nouveau solde est de :",compte["titulaire"], ":", compte["solde"], "cfa")


def retrais(comptes):
    #ont recupere les le compte  a debiter puis ont valide le retrais 

    numero = saisir_numero_compte_existant(comptes, "numero du compte a debiter : ")
    montant = saisir_montant_positif("montant a retirer : ")
    compte = trouver_compte(comptes, numero)
    if montant > compte["solde"]:
        print("Erreur : solde insuffisant. solde actuel :", compte["solde"], "cfa")
    else:
        compte["solde"] = compte["solde"] - montant
        print("=====================================================================================")
        print("retrait effectué. nouveau solde de", compte["titulaire"])
        print(compte["solde"], "cfa")
    
# fais  j'esserais de simplifier le plus pour que tu comprennne 
#mais simplement c'est pour la 6 option qui dit un transfere entre des compte de la meme entreprise

def transfer(comptes):
    # recupere le compte bebiteur et crediteur 
    numero_source = saisir_numero_compte_existant(comptes, "numero du compte source : ")
    numero_destination = saisir_numero_compte_existant(comptes, "numero du compte destination : ")
    
    # ont verifie si si l'utilusateur entre les meme compte si oui ont luis dit c'st pas possible
    
    while numero_destination == numero_source:
        print("Erreur : la destination doit etre differente de la source.")
        numero_destination = saisir_numero_compte_existant(comptes, "numero du compte destination : ")
    montant = saisir_montant_positif("montant a transferer : ")
    
# si compte existe alors ont doit verifier si il peut etre debiter  si oui ont accepete l'operation

    source = trouver_compte(comptes, numero_source)
    destination = trouver_compte(comptes, numero_destination)

    if montant > source["solde"]:
        print("Erreur : solde insuffisant sur le compte de", source["titulaire"])
    else:
        source["solde"] = source["solde"] - montant
        destination["solde"] = destination["solde"] + montant
        print("==================================================================")
        print("transfert effectué :", montant, "cfa de", source["titulaire"], "vers", destination["titulaire"])
        print("nouveau solde de", source["titulaire"], ":", source["solde"], "cfa")
        print("nouveau solde de", destination["titulaire"], ":", destination["solde"], "cfa")

# executeur main   a pour but de nous permetre de naviguer a travers nos option: choix
def main():
    print("====================****** Bienvenue à l'Agence CESAG BANK *******========================")
    quitter = False
    while not quitter:
        menu()
        choix = saisir_choix_menu()
        if choix == 1 :
            afficher_comptes(comptes)
        elif choix == 2:
            consulter_solde(comptes)
        elif choix==3:
            creer_un_compte(comptes)
        elif choix==4:
            depot(comptes)
        elif choix==5:
            retrais(comptes)
        elif choix==6:
            transfer(comptes)
        elif choix ==7:
            print("===============Merci d'avoir utilisé CESAG BANK================")
            print("=========================À bientôt======================")
            quitter = True

# ce ci  n'est pas obligatoire mais permet executer l'ensemble facilement (au cas ou tu pourra lance directement une fois telecharger sans rentrer dans ton editeur de code)
if __name__ == "__main__":
    main()
