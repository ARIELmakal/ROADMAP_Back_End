'''
Ce code calcule le salaire qui sera attribué à chaque employé en prend en compte ces trois facteurs:
    - La côte d_assiduité.
    - Le temps fournit au bureau ou dans l_atelier.
    - Le comportement des employés.
    Nombre d_heures est de 10h et ils sont payer 20$/h

'''

print("\n\t\tFICHE DE PAIEMENT: \n")

#Création des listes stockant les noms et les salaires  des employes
liste_employés = []
list_salaire = []

#Variable stockant le nombre des personnes qui doivent être payés.
personnels = int(input("Combien de personnes doivent recevoir leur payes ?\n"))

#Cas où le nombre de personnes est égal à 0: La question sera réposé
while personnels == 0 :
    print("Nombre invalide !")
    personnels = int(input("Combien de personnes doivent recevoir leur paye ?\n"))


#Nous allons à partir de cette boucle récuperer tous les noms des employés en les mettant dans une liste
for names in range (0,personnels):
    names = input("\nComment s'appelle cette personne ?\n")
    liste_employés.append(names)


    #Dans cette partie du code nous allons récuperer les côtes pour fixer un salaire
    print(f"\n\t\tNous allons maintenant fixer le salaire de {names} par rapport aux facteurs suivants:\nL'assiduité est coté sur 3pts\nLe travail fournit est coté sur 4pts\nLe comportement est coté sur 3pts.\n\n")

    #Cette variable stockera la côte assiduite attribuer des employés
    question_assiduite = float(input("Assiduité= "))

    #Cas où la côte entrée est superieure à 3 et inférieure à 0 
    while question_assiduite > 3 or question_assiduite < 0:
        print("La côte introduite n'est pas valide")
        question_assiduite = float(input("Assiduité= "))
        


    #Cette variable stockera la côte du travail fournit attribuer aux employés
    question_travail_fournit = float(input("Travail fournit= "))

    #Cas où la côte entrée est superieure à 4 et inférieure à 0
    while question_travail_fournit > 4 or question_travail_fournit < 0:
        print("La côte introduite n'est pas valide")
        question_travail_fournit = float(input("Travail fournit= "))



    #Cette variable stockera la côte du comportement attribuer aux employés
    question_comportement = float(input("Comportement = "))

    #Cette boucle prend compte le fait que l'utilisateur ne saisisse que ce qui est demandé : un nombre entre 0-3
    while question_comportement > 3 or question_comportement < 0:
        print("La cote inserée  n'est pas valide !")
        question_comportement = float(input("Comportement= "))


    #Cette variable associe les côtes récues pour determiner le surplus
    surplus = question_comportement + question_assiduite + question_travail_fournit

    #Affichage de la côte après sommation 
    print(f"{names} a obtenu un surplus de {surplus}$\n")

    # Cette variable sert à calculer le salaire en prenant en compte 10 heures de travail que nous multiplieront par 20$
    salaire_heure = 10 * 20

    # Cette variable stockera le salaire total après calculs
    salaire_total = salaire_heure + surplus

    #Nous allons à partir de cette boucle récuperer tous les salaires des employés en les mettant dans une liste
    for salaire in range (0,personnels-1): #Ici j'ai mis -1 parce qu'il prend le nombre de personne qui doivent être payer et il répète le salaire d'une personne deux fois 
        list_salaire.append(salaire_total)
        
    #Affichage du salaire
    print(f"{names} aura: {salaire_total}$")

#Affichage de la liste enregistrée
print(f"Voici les employés: {liste_employés}")
print(f"Voici leurs salaires: {list_salaire} (en dollard ) \n")
