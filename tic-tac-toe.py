def grille(grille):
    print("     0)  1)  2)")
    print("   -------------")
    print("0)", end='')
    for i in range(3):
        print(" | "+str(grille[i]), end='')
    print(" |")
    print("   -------------")
    print("1)", end='')
    for i in range(3):
        print(" | "+str(grille[i+3]), end='')
    print(" |")
    print("   -------------")
    print("2)", end='')
    for i in range(3):
        print(" | "+str(grille[i+6]), end='')
    print(" |")
    print("   -------------")
    # pour faire la grille et numéroter les cases  
 
 
def tour(grille, joueur):
    print("C'est le tour du joueur "+str(joueur))
    colonne=input("Entrez le numero de la colonne : ")
    ligne=input("Entrez le numero de la ligne : ")
    print("Vous avez joué la case ("+colonne+","+ligne+")")
    while grille[int(colonne)+int(ligne)*3]!=" ":
        grille(grille)
        print("Cette case est indisponible ! Saisissez une autre case svp ")
        colonne=input("Entrez le numero de la colonne : ")
        ligne=input("Entrez le numero de la ligne : ")
        print("Vous avez joué la case ("+colonne+","+ligne+")")
    # questions pour places les pions
 
    if joueur==1 :
        grille[int(colonne)+int(ligne)*3]="X"
    if joueur==2 :
        grille[int(colonne)+int(ligne)*3]="O"
    grille(grille)
    #place le bon pion
 
def gagnant(grille):
    if (grille[0]==grille[1]) and (grille[0]==grille[2]) and (grille[0]!=" "):
        return 1
    if (grille[3]==grille[4]) and (grille[3]==grille[5]) and (grille[3]!=" "):
        return 1
    if (grille[6]==grille[7]) and (grille[6]==grille[8]) and (grille[6]!=" "):
        return 1
    if (grille[0]==grille[3]) and (grille[0]==grille[6]) and (grille[0]!=" "):
        return 1
    if (grille[1]==grille[4]) and (grille[1]==grille[7]) and (grille[1]!=" "):
        return 1
    if (grille[2]==grille[5]) and (grille[2]==grille[8]) and (grille[2]!=" "):
        return 1
    if (grille[0]==grille[4]) and (grille[0]==grille[8]) and (grille[0]!=" "):
        return 1
    if (grille[2]==grille[4]) and (grille[2]==grille[6]) and (grille[2]!=" "):
        return 1
    #defini quand les 3 X ou O sont alligner donc gagnant
 
 
def match_nul(grille):
    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1
# si match nul ça recommence
 
joueur=1
print("Le joueur 1 possède les X. Le joueur 2 possède les O")
grille=[" "," "," "," "," "," "," "," "," "]
grille(grille)
gagne=0
while gagne==0:
    tour(grille,joueur)
    if gagnant(grille):
        print("Le joueur "+str(joueur)+" remporte la partie !! Bravo !!!!")
        gagne=1
    else:
        if match_nul(grille):
            print(" Match nul ! tentez la prochaine ...")
            gagne=1
    if joueur==1:
        joueur=2
    else:
        joueur=1