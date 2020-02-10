from functools import reduce

from Cours import Cours
from Etudiant import Etudiant
from Note import Note

#Utils pour la version fonctionelle
tete_ = lambda liste: liste[0]
reste_ = lambda liste: liste[1:]

def somme_liste(liste):
    return (lambda liste: tete_(liste) + somme_liste(reste_(liste)) if liste else 0)(liste)

def taille_liste(liste):
    return (lambda liste: 1 + taille_liste(reste_(liste)) if liste else 0)(liste)

class BD:
    def __init__(self, liste_etudiants=[], liste_cours=[], liste_notes=[]):
        """
        :param liste_etudiants: Liste vide par defaut, sinon cette liste contient des etudiants
        :param liste_cours: Liste vide par defaut, sinon cette liste contient des cours
        :param liste_notes: Liste vide par defaut, sinon cette liste contient des notes
        """
        self.liste_etudiants = liste_etudiants
        self.liste_cours = liste_cours
        self.liste_notes = liste_notes

    def ajouter_etudiant(self, etudiant):
        """
        :param etudiant: Ajoute cet etudiant a la BD, dans la liste des etudiants
        :return: rien
        """
        self.liste_etudiants.append(etudiant)

    def supprimer_etudiant(self, etudiant):
        """
        :param etudiant: Supprime cet etudiant de la liste des etudiants de la BD
        :return: rien
        """
        self.liste_etudiants.remove(etudiant)

    def editer_etudiant(self, etudiant, nouveau_prenom_etudiant=None, nouveau_nom_etudiant=None, nouveau_niveau_etudiant=None):
        """
        Modifie un etudiant, l'ajoute a la BD, et le retourne
        :param etudiant: etudiant a modifier
        :param nouveau_prenom_etudiant: Nouveau prenom, si c'est None, le nouveau prenom est l'ancien
        :param nouveau_nom_etudiant: Nouveau nom, si c'est None, le nouveau nom est l'ancien
        :param nouveau_niveau_etudiant: Nouveau niveau, si c'est None, le nouveau niveau est l'ancien
        :return: le nouvel etudiant
        """
        self.supprimer_etudiant(etudiant)
        if nouveau_prenom_etudiant is not None:
            etudiant.prenom_etudiant = nouveau_prenom_etudiant
        if nouveau_nom_etudiant is not None:
            etudiant.nom_etudiant = nouveau_nom_etudiant
        if nouveau_niveau_etudiant is not None:
            etudiant.niveau_etudiant = nouveau_niveau_etudiant
        self.ajouter_etudiant(etudiant)
        return etudiant

    def ajouter_cours(self, cours):
        """
        :param cours: Ajoute ce cours a la BD, dans la liste des cours
        :return: Rien
        """
        self.liste_cours.append(cours)

    def supprimer_cours(self, cours):
        """
        :param cours: Supprime ce cours de la liste des cours de la BD
        :return: rien
        """
        self.liste_cours.remove(cours)

    def editer_cours(self, cours, nouveau_intitule_cours=None, nouveau_niveau_cours=None):
        """
        :param cours: Cours a modifier
        :param nouveau_intitule_cours: Le nouveau intitule, si c'est None, l'ancien n'est pas remplace
        :param nouveau_niveau_cours: Le nouveau niveau, si c'est None, l'ancien n'est pas remplace
        :return: le nouveau cours
        """
        self.supprimer_cours(cours)
        if nouveau_intitule_cours is not None:
            cours.intitule_cours = nouveau_intitule_cours
        if nouveau_niveau_cours is not None:
            cours.niveau_cours = nouveau_niveau_cours
        self.ajouter_cours(cours)
        return cours

    def ajouter_note(self, note):
        """
        :param note: Ajoute cette note a la BD, dans la liste des notes
        :return: Rien
        """
        self.liste_notes.append(note)

    def supprimer_note(self, note):
        """
        :param note:  Supprime cette note de la liste des notes de la BD
        :return: Rien
        """
        self.liste_notes.remove(note)

    def editer_note(self, note, nouvelle_note=None):
        """
        :param note: Note a modifier
        :param nouvelle_note: valeur de la nouvelle note, si c'est None, l'ancienne n'est pas remplacee
        :return: La nouvelle note
        """
        self.supprimer_note(note)
        if nouvelle_note is not None:
            note.note = nouvelle_note
        self.ajouter_note(note)
        return note

    ##################################
    # Version imperative:
    ##################################

    def moyenne_cours_imperatif(self, cours):
        # Algorithme imperatif classique, en utilisant sum() et len() de Python.
        """
        :param cours: La moyenne des notes de ce cours sera calculee en imperatif classique.
        :return: La moyenne des notes du cours en parametre
        """
        notes_cours = self.notes_cours_imperatif(cours)
        return sum(notes_cours) / len(notes_cours)

    def moyenne_etudiant_imperatif(self, etudiant):
        # Algorithme imperatif classique, en utilisant sum() et len() de Python.
        """
        :param etudiant: La moyenne des notes de cet etudiant sera calculee en imperatif classique.
        :return: La moyenne des notes de l'etudiant en parametre
        """
        notes_etudiant = self.notes_etudiant_imperatif(etudiant)
        return sum(notes_etudiant) / len(notes_etudiant)

    def notes_cours_imperatif(self, cours):
        # Algorithme imperatif classique
        """
         :param cours: Les notes correspondants a ce cours seront retournes
         :return: La liste des notes correspondants au cours en parametre
        """
        notes_resultat = []
        for note in self.liste_notes:
            if note.code_cours == cours.code_cours:
                notes_resultat.append(note.note)
        return notes_resultat

    def notes_etudiant_imperatif(self, etudiant):
        # Algorithme imperatif classique
        """
         :param etudiant: Les notes correspondants a cet etudiant seront retournes
         :return: La liste des notes correspondants a l'etudiant en parametre
        """
        notes_resultat = []
        for note in self.liste_notes:
            if note.numero_etudiant == etudiant.numero_etudiant:
                notes_resultat.append(note.note)
        return notes_resultat

    #####################################
    # Version fonctionelle:
    #####################################
    #Les utils utilises ici sont definis au dessus de la definition de la class BD

    def moyenne_cours_fonctionnel(self, cours):
        """
        :param cours: La moyenne des notes de ce cours sera calculee.
        :return: La moyenne des notes du cours en parametre
        """
        return (lambda cours: somme_liste(self.notes_cours_fonctionnel(self.liste_notes, cours))
                             / taille_liste(self.notes_cours_fonctionnel(self.liste_notes, cours)))(cours)

    def moyenne_etudiant_fonctionnel(self, etudiant):
        """
        :param etudiant: La moyenne des notes de cet etudiant sera calculee.
        :return: La moyenne des notes de l'etudiant en parametre
        """
        return (lambda etudiant: somme_liste(self.notes_etudiant_fonctionnel(self.liste_notes, etudiant))
                              / taille_liste(self.notes_etudiant_fonctionnel(self.liste_notes, etudiant)))(etudiant)

    def notes_cours_fonctionnel(self, liste_notes, cours):
        """
        :param liste_notes: la liste des notes de la BD
        :param cours: Les notes correspondants a ce cours seront retournes
        :return: La liste des notes correspondants au cours en parametre
        """
        return (lambda liste_notes, cours: liste_notes if liste_notes == []
                    else [tete_(liste_notes).note] + self.notes_cours_fonctionnel(reste_(liste_notes), cours) if tete_(liste_notes).code_cours == cours.code_cours
                    else self.notes_cours_fonctionnel(reste_(liste_notes), cours)
                )(liste_notes, cours)

    def notes_etudiant_fonctionnel(self, liste_notes, etudiant):
        """
        :param liste_notes: la liste des notes de la BD
        :param etudiant: Les notes correspondants a cet etudiant seront retournes
        :return: La liste des notes correspondants a l'etudiant en parametre
        """
        return (lambda liste_notes, etudiant: liste_notes if liste_notes == []
                    else [tete_(liste_notes).note] + self.notes_etudiant_fonctionnel(reste_(liste_notes), etudiant) if tete_(liste_notes).numero_etudiant == etudiant.numero_etudiant
                    else self.notes_etudiant_fonctionnel(reste_(liste_notes), etudiant)
                )(liste_notes, etudiant)

    ##################################
    # Version filter-map-reduce
    ##################################

    def moyenne_cours_filter_map_reduce(self, cours):
        # reduce
        # filter et map sont appliquees dans notes_cours_filter_map_reduce()
        """
        :param cours: La moyenne des notes de ce cours sera calculee en utilisant le paradigme filter-map-reduce
        :return: La moyenne des notes du cours en parametre
        """
        valeurs_notes = self.notes_cours_filter_map_reduce(cours)
        moyenne = reduce(lambda x, y: x + y, valeurs_notes) / len(valeurs_notes)
        return moyenne

    def moyenne_etudiant_filter_map_reduce(self, etudiant):
        #reduce
        #filter et map sont appliquees dans notes_etudiant_filter_map_reduce()
        """
        :param etudiant: La moyenne des notes de cet etudiant sera calculee en utilisant le paradigme filter-map-reduce
        :return: La moyenne des notes de l'etudiant en parametre
        """
        valeurs_notes = self.notes_etudiant_filter_map_reduce(etudiant)
        moyenne = reduce(lambda x, y: x + y, valeurs_notes) / len(valeurs_notes)
        return moyenne

    def notes_cours_filter_map_reduce(self, cours):
        #filter puis map
        """
        :param cours: Les notes correspondants a ce cours seront retournes en utilisant le paradigme filter-map-reduce
        :return: La liste des notes correspondants au cours en parametre
        """
        notes = list(filter(lambda note: note.code_cours == cours.code_cours, self.liste_notes))
        valeurs_notes = list(map(lambda note: note.note, notes))
        return valeurs_notes

    def notes_etudiant_filter_map_reduce(self, etudiant):
        # filter puis map
        """
        :param etudiant: Les notes correspondants a cet etudiant seront retournes en utilisant le paradigme filter-map-reduce
        :return: La liste des notes correspondants a l'etudiant en parametre
        """
        notes = list(filter(lambda note: note.numero_etudiant == etudiant.numero_etudiant, self.liste_notes))
        valeurs_notes = list(map(lambda note: note.note, notes))
        return valeurs_notes


#Un peu de tests....
if __name__ == '__main__':
    bd = BD()

    etudiant1 = Etudiant(1, "Jean", "Dupont", 'A')
    etudiant2 = Etudiant(2, "Jacques", "Durant", 'A')

    bd.ajouter_etudiant(etudiant1)
    bd.ajouter_etudiant(etudiant2)

    cours1 = Cours('100', 'Paradigmes de programmation', 'A')
    cours2 = Cours('101', 'ACCOV', 'A')
    cours3 = Cours('102', 'Structures de donnees', 'A')

    bd.ajouter_cours(cours1)
    bd.ajouter_cours(cours2)
    bd.ajouter_cours(cours3)

    bd.ajouter_note(Note(1, '100', 10))
    bd.ajouter_note(Note(1, '101', 11))
    bd.ajouter_note(Note(1, '102', 12))

    bd.ajouter_note(Note(2, '100', 13))
    bd.ajouter_note(Note(2, '101', 14))
    bd.ajouter_note(Note(2, '102', 15))

    print(bd.editer_cours(cours=cours1, nouveau_niveau_cours='B'))

    print('---imperatif---')

    print(bd.notes_cours_imperatif(cours1))
    print(bd.notes_cours_imperatif(cours2))
    print(bd.notes_cours_imperatif(cours3))

    print(bd.moyenne_cours_imperatif(cours1))
    print(bd.moyenne_cours_imperatif(cours2))
    print(bd.moyenne_cours_imperatif(cours3))

    print(bd.notes_etudiant_imperatif(etudiant1))
    print(bd.notes_etudiant_imperatif(etudiant2))

    print(bd.moyenne_etudiant_imperatif(etudiant1))
    print(bd.moyenne_etudiant_imperatif(etudiant2))

    print('---filter map reduce---')
    print(bd.notes_cours_filter_map_reduce(cours1))
    print(bd.notes_cours_filter_map_reduce(cours2))
    print(bd.notes_cours_filter_map_reduce(cours3))

    print(bd.moyenne_cours_filter_map_reduce(cours1))
    print(bd.moyenne_cours_filter_map_reduce(cours2))
    print(bd.moyenne_cours_filter_map_reduce(cours3))

    print(bd.notes_etudiant_filter_map_reduce(etudiant1))
    print(bd.notes_etudiant_filter_map_reduce(etudiant2))

    print(bd.moyenne_etudiant_filter_map_reduce(etudiant1))
    print(bd.moyenne_etudiant_filter_map_reduce(etudiant2))


    print('---fonctionnel---')
    print(bd.notes_cours_fonctionnel(bd.liste_notes, cours1))
    print(bd.notes_cours_fonctionnel(bd.liste_notes, cours2))
    print(bd.notes_cours_fonctionnel(bd.liste_notes, cours3))

    print(bd.moyenne_cours_fonctionnel(cours1))
    print(bd.moyenne_cours_fonctionnel(cours2))
    print(bd.moyenne_cours_fonctionnel(cours3))

    print(bd.notes_etudiant_fonctionnel(bd.liste_notes, etudiant1))
    print(bd.notes_etudiant_fonctionnel(bd.liste_notes, etudiant2))

    print(bd.moyenne_etudiant_fonctionnel(etudiant1))
    print(bd.moyenne_etudiant_fonctionnel(etudiant2))
