class Note:
    def __init__(self, numero_etudiant, code_cours, note):
        """
            :param numero_etudiant: Numero de l'etudiant
            :param code_cours: Code du cours correspondant
            :param note: valeur de la note
        """
        self.numero_etudiant = numero_etudiant
        self.code_cours = code_cours
        self.note = note

    def __str__(self):
        return "Note de l'etudiant numero %d, en cours code %s : %d" % (self.numero_etudiant, self.code_cours, self.note)
