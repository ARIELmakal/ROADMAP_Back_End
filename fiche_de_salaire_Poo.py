class Personne:
    def __init__(self, nom:str, assiduite, travail, comportement):
        self.nom = nom
        if self.nom == "":  self.SePresenter()
        self.assiduite = assiduite
        if self.assiduite == 0: self.Assidu()
        self.travail = travail
        if self.travail == 0:   self.Effort()
        self.comportement = comportement
        if self.comportement == 0:  self.Behavior()
#Methode Présentation
    def SePresenter(self):
        self.nom = input("Nom de la personne: ")
#Cote Attribué à chaque employé

    #Assiduité aux travail
    def Assidu(self):
        self.assiduite =float(input(">> Cote assiduté : "))

        #Cas où la côte entrée est superieure à 3 ou inférieure à 0
        while self.assiduite >3 or self.assiduite < 0:
            print("La cote inscrite n'est pas valide (Cote comprise entre 1 - 3)\n")
            self.assiduite = float(input(">> Cote assiduté : "))

    #Effort ou le travail fourni
    def Effort(self):
        self.travail = float(input(">> Cote travail : "))

        #Cas où la côte entrée est superieure à 4 ou inférieure à 0
        while self.travail >4 or self.travail < 0:
            print("La cote inscrite n'est pas valide (Cote comprise entre 1 - 4)\n")
            self.travail = float(input(">> Cote travail : "))

    #Comportement dans ton travail
    def Behavior(self):
        self.comportement = float(input(">> Cote comportement : "))

        #Cas où la côte entrée est superieure à 3 ou inférieure à 0
        while self.comportement >3 or self.comportement < 0:
            print("La cote inscrite n'est pas valide (Cote comprise entre 1 - 3)\n")
            self.assiduite = float(input(">> Cote comportement : "))

#Salaire 
    def Salaire(self):
        salaire_heure = 200
        salaire_total = salaire_heure + self.travail + self.assiduite + self.comportement
        print(f"{self.nom} : {salaire_total} $")


list_personne = [Personne("Ariel",3,4,3),Personne("",0,0,0),Personne("",0,0,0)]
for personne in list_personne:
    personne.Salaire()