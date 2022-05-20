import random

list_docteurs = [ ]
def enreg_docteur(nom, pnom, prenom, tel, matricule, special):
        horaire = "Disponible"
        docteur = [ ]
        docteur.append(nom)
        docteur.append(pnom)
        docteur.append(prenom)
        docteur.append(tel)
        docteur.append(matricule)
        docteur.append(special)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        docteur.append(horaire)
        
        if len(list_docteurs) > 0:
                mat = False
                for i in range(len(list_docteurs)):
                        if matricule == list_docteurs[i][4]:
                                mat = True
                if mat == True:
                        print ("Désolé, le numéro matricule entré appartient déjà à un docteur!")
                else:
                        list_docteurs.append(docteur)
                        print ("Le docteur \"", nom, pnom, prenom, "\" a été enregistré avec succès!")   
        else:
                list_docteurs.append(docteur)
                print ("Le docteur \"", nom, pnom, prenom, "\" a été enregistré avec succès!")


list_patients = [ ]
def enreg_patient(nom, pnom, prenom, tel, poids, taille, genre, age):
        patient = [ ]
        patient.append(nom)
        patient.append(pnom)
        patient.append(prenom)
        patient.append(tel)
        patient.append(poids)
        patient.append(taille)
        while genre.lower() != "masc" and genre.lower() != "fem":
            genre = input("Le genre entré est invalide! Veuillez entrer \"Masc\" ou \"Fem\" svp:")
        patient.append(genre)
        try:
                while age < 0 or age > 150:
                    age = int(input("Age incorrect! Veuillez réessayer:"))
                patient.append(age)
        except ValueError:
                print ("Vous avez entré une valeur invalide!")
        if len(list_patients) > 0:
            for i in range (len(list_patients)):
                num_dossier = random.randint(10000000, 100000000)
                while num_dossier == list_patients[i][8]:
                    num_dossier = random.randint(10000000, 100000000)
        else:
            num_dossier = random.randint(10000000, 100000000)
        patient.append(num_dossier)
        list_patients.append(patient)
        if genre.lower() == "masc":
                print ("Le patient \"", nom, pnom, prenom, "\" a été enregistré avec succès!")
        else:
                print ("La patiente \"", nom, pnom, prenom, "\" a été enregistrée avec succès!")


def chercher_nom_patient(nom, pnom, prenom):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        noms_patients = [ ]
        for i in range(len(list_patients)):
            noms = list_patients[i][0]+list_patients[i][1]+list_patients[i][2]
            noms_patients.append(noms.lower())
    
        nouveau_nom = nom+pnom+prenom
        resultats = [ ]
        for i in range(len(list_patients)):
            if nouveau_nom.lower() == noms_patients[i]:
                resultats.append(list_patients[i])
        if resultats == [ ]:
            print ("Aucun patient ne porte ce nom dans notre liste!")
        else:
            for i in range(len(resultats)):
                print(" Nom: ", resultats[i][0], \
                      "\n Post-nom: ", resultats[i][1], \
                      "\n Prénom: ", resultats[i][2], \
                      "\n Telephonne: ", resultats[i][3], \
                      "\n Poids: ", resultats[i][4], " Kg", \
                      "\n Taille: ", resultats[i][5], " m.", \
                      "\n Genre: ", resultats[i][6]+".", \
                      "\n Age: ", resultats[i][7], " ans", \
                      "\n Dossier n° ", resultats[i][8], "\n")


def chercher_num_dossier(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
            print(" Nom: ", list_patients[cle][0], \
                      "\n Post-nom: ", list_patients[cle][1], \
                      "\n Prénom: ", list_patients[cle][2], \
                      "\n Telephonne: ", list_patients[cle][3], \
                      "\n Poids: ", list_patients[cle][4], " Kg", \
                      "\n Taille: ", list_patients[cle][5], " m.", \
                      "\n Genre: ", list_patients[cle][6]+".", \
                      "\n Age: ", list_patients[cle][7], " ans", \
                      "\n Dossier n° ", list_patients[cle][8], "\n")


def aff_patients():
    if len(list_patients) == 0:
        print ("La liste des patients est toute vide!")
    else:
        for i in range(len(list_patients)):
            print (" Nom: ", list_patients[i][0], \
                      "\n Post-nom: ", list_patients[i][1], \
                      "\n Prénom: ", list_patients[i][2], \
                      "\n Telephonne: ", list_patients[i][3], \
                      "\n Poids: ", list_patients[i][4], " Kg", \
                      "\n Taille: ", list_patients[i][5], " m.", \
                      "\n Genre: ", list_patients[i][6]+".", \
                      "\n Age: ", list_patients[i][7], " ans", \
                   "\n Dossier n° ", list_patients[i][8], "\n")

def aff_docteurs():
    if len(list_docteurs) == 0:
        print ("La liste des docteurs est toute vide!")
    else:
        for i in range(len(list_docteurs)):
            print (" Nom: ", list_docteurs[i][0], \
                      "\n Post-nom: ", list_docteurs[i][1], \
                      "\n Prénom: ", list_docteurs[i][2], \
                      "\n Telephonne: ", list_docteurs[i][3], \
                      "\n Numero matricule: ", list_docteurs[i][4], \
                      "\n Specialisation: ", list_docteurs[i][5], "\n")


def enreg_plainte(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
            plainte = input("Entrez une nouvelle plainte pour "+ list_patients[cle][2] +" "+list_patients[cle][0]+" :")
            list_patients[cle].append(plainte)
            print ("La nouvelle plainte de ", list_patients[cle][2], list_patients[cle][0], " a été enregistrée avec succès!")


def enreg_horaire(matricule, dossier):
    if len(list_docteurs) == 0:
        print ("La liste des docteurs est vide!")
    else:
        cle = -1
        for i in range(len(list_docteurs)):
            if matricule == list_docteurs[i][4]:
                cle = i
        if cle == -1:
                print ("Aucun medecin ne porte ce matricle!")
        else:
                if len(list_patients) == 0:
                        print ("La liste des patients est vide!")
                else:
                        cle2 = -1
                        for i in range(len(list_patients)):
                            if dossier == list_patients[i][8]:
                                cle2 = i
                        if cle2 == -1:
                            print ("Ce numero de dossier n'est pas attribué!")
                        else:
                            if len(list_patients[cle2]) <= 9:
                                print("Il n'y a aucune plainte disponible pour ", list_patients[cle2][2], list_patients[cle2][0])
                            else:
                                try:
                                    for i in range(9, len(list_patients[cle2])):
                                            print ("Plainte ",i-8, ": ", list_patients[cle2][i])
                                    c1 = int(input("Entrez le numero d'une plainte à ajouter"))
                                    while c1 >= len(list_patients[cle2])-8 or c1 <= 0:
                                            c1 = int(input("Numero invalide! Entrez le numero d'une plainte à ajouter"))
                                except ValueError:
                                     print ("Vous avez entré une valeur invalide!")
                                     main()
                                            
                                c2 = input("Tapez en toute lettre un jour de la semaine (du lundi au samedi) auquel sera attachée la plainte:")
                                while c2.lower() != "lundi" and c2.lower() != "mardi" and c2.lower() != "mercredi" and \
                                c2.lower() != "jeudi" and c2.lower() != "vendredi" and c2.lower() != "samedi":
                                        c2 = input("Erreur! Veuillez réesayer svp (entre lundi et samedi uniquement! exemple: mercredi)")
                                        
                                if c2.lower() == "lundi":
                                        if list_docteurs[cle][6] == "Disponible":
                                                list_docteurs[cle][6] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le lundi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][6] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")
                                                        
                                elif c2.lower() == "mardi":
                                        if list_docteurs[cle][7] == "Disponible":
                                                list_docteurs[cle][7] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le mardi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][7] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")

                                elif c2.lower() == "mercredi":
                                        if list_docteurs[cle][8] == "Disponible":
                                                list_docteurs[cle][8] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le mercredi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][8] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")

                                elif c2.lower() == "jeudi":
                                        if list_docteurs[cle][9] == "Disponible":
                                                list_docteurs[cle][9] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le jeudi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][9] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")

                                elif c2.lower() == "vendredi":
                                        if list_docteurs[cle][10] == "Disponible":
                                                list_docteurs[cle][10] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le vendredi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][10] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")

                                elif c2.lower() == "samedi":
                                        if list_docteurs[cle][11] == "Disponible":
                                                list_docteurs[cle][11] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                        else:
                                                c3 = input("Le docteur "+list_docteurs[cle][2]+" "+ list_docteurs[cle][0]+ " n'est pas disponible le samedi. Voulez-vous ecraser l'ancien programme?")
                                                while c3.lower() != "oui" and c3.lower() != "non":
                                                        c3 = input("Repondez par \"oui\" ou \"non\" svp!:")
                                                if c3.lower() == "oui":
                                                        list_docteurs[cle][11] = "Dossier n° "+str(list_patients[cle2][8])+": "+list_patients[cle2][c1+8]
                                                        print("La plainte n° ",c1, " de ", list_patients[cle2][2], list_patients[cle2][0], " a été prise en compte")
                                                else:
                                                        print("Merci! La plainte en cours n'a pas été ecrasée.")



def disponibilite_medecin(matricule):
        if len(list_docteurs) == 0:
                print ("La liste des docteurs est vide!")
        else:
            cle = -1
            for i in range(len(list_docteurs)):
                if matricule == list_docteurs[i][4]:
                    cle = i
            if cle == -1:
                print ("Aucun medecin ne porte ce matricle!")
            else:
                print ("Docteur ", list_docteurs[cle][2], list_docteurs[cle][0], ":")
                jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
                for i in range(len(jours)):
                    print(jours[i],": ", list_docteurs[cle][i+6])
                choix = input("Tapez 1 pour ajouter un rendez-vous, ou 0 pour retourner au menu principal:")
                while choix != "1" and choix != "0":
                    choix = input("Veuillez taper 1 ou 0 svp")
                
                if choix == "1":
                    try:
                        enreg_horaire(matricule, int(input("Entrez le numero du dossier du patient à prendre en charge:")))
                    except ValueError:
                         print("Vous avez entré une valeur inavlide!")
                else:
                    print("Merci")



def aff_plaintes(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
                if len(list_patients[cle]) <= 9:
                        print("Il n'y a aucune plainte disponible pour ", list_patients[cle][2], list_patients[cle][0])
                else:
                        print (list_patients[cle][2], list_patients[cle][0], ":")
                        for i in range(9, len(list_patients[cle])):
                                print ("Plainte ",i-8, ": ", list_patients[cle][i])


def afficher_IMC(dossier):
    if len(list_patients) == 0:
        print ("La liste des patients est vide!")
    else:
        cle = -1
        for i in range(len(list_patients)):
            if dossier == list_patients[i][8]:
                cle = i
        if cle == -1:
            print ("Ce numero de dossier n'est pas attribué!")
        else:
            imc = list_patients[cle][4]/list_patients[cle][5]
            if imc < 18.5:
                    print(list_patients[cle][2], list_patients[cle][0], ": Insuffisance pondérale (maigreur)")
            elif imc >= 18.5 and imc < 25:
                    print(list_patients[cle][2], list_patients[cle][0], ": Corpulence normale")
            elif imc >= 25 and imc < 30:
                    print(list_patients[cle][2], list_patients[cle][0], ": Surpoids")
            elif imc >= 30 and imc < 35:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité modérée")
            elif imc >= 35 and imc < 40:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité sévère")
            else:
                    print(list_patients[cle][2], list_patients[cle][0], ": Obésité morbide ou massive")


def main():
    c = input(" 1 pour enregistrer un docteur \n 2 pour enregistrer un patient \n \
3 pour rechercher un ou plusieurs patient(s) a partir d'un nom \n \
4 pour atteindre un patient gràce à son numero du dossier \n \
5 pour afficher tous les patients enregistrés \n \
6 pour afficher tous les docteurs enregistrés \n \
7 pour enregistrer une plainte \n \
8 pour personnaliser l'horaire d'un medecin \n \
9 pour vérifier la disponibilité d'un medecin \n \
10 pour afficher la liste des plaintes d'un patient \n \
11 pour afficher l'IMC (indice de masse corporelle) \n \
et 0 pour quitter. \
\n\n  >>> Choisissez une action à faire: ")
    if c == "1":
        enreg_docteur(input("Entrez le nom:"), input("Entrez le post-nom:"), \
        input("Entrez le prenom:"), input("Entrez le numero de téléphone:"), \
        input("Entrez le numero matricule:"), input("Entrez une specialisation:"))
        main()
    elif c == "2":
        try:
            enreg_patient(input("Entrez le nom:"), input("Entrez le post-nom:"), \
            input("Entrez le prenom:"), input("Entrez le numero de téléphone:"), \
            float(input("Entrez le poids (Juste la valeur numerique en Kg):")), \
            float(input("Entrez la taille (Juste la valeur numerique en mettre):")), \
            input("Entrez le genre (Masc ou Fem):"),  int(input("Entrez l'age (Juste la valeur numerique):")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "3":
        chercher_nom_patient(input("Entrez le nom:"), input("Entrez le post-nom:"), \
        input("Entrez le prenom:"))
        main()
    elif c == "4":
        try:
             chercher_num_dossier(int(input("Entrez le numero du dossier à atteindre:")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "5":
        aff_patients()
        main()
    elif c == "6":
        aff_docteurs()
        main()
    elif c == "7":
        try:
            enreg_plainte(int(input("Entrez le numero du dossier du patient:")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "8":
        try:
            enreg_horaire(input("Entrez le matricule du medecin"),\
            int(input("Entrez le numero du dossier du patient à prendre en charge:")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "9":
        disponibilite_medecin(input("Entrez le matricule du medecin"))
        main()
    elif c == "10":
        try:
            aff_plaintes(int(input("Entrez le numero du dossier du patient:")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "11":
        try:
            afficher_IMC(int(input("Entrez le numero du dossier à atteindre:")))
        except ValueError:
             print("Vous avez entré une valeur invalide!")
        main()
    elif c == "0":
        print("Merci à vous d'avoir consulté ce logiciel.")
    else:
        print ("Choix invalide!")
        main()


main()
