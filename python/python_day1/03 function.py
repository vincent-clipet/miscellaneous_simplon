#############
# FUNCTIONS #
#############

def est_pair(nb):
    return nb_utilisateur % 2 == 0



#######
# RUN #
#######

nb_utilisateur = int(input("Entrez un nombre entier : "))

if est_pair(nb_utilisateur):
    print("le nombre est pair")
else:
    print("Le nombre est impair")

