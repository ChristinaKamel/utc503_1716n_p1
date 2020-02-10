class Cours:
    def __init__(self, code_cours, intitule_cours, niveau_cours):
        """
        :param code_cours: Code du cours (identificateur)
        :param intitule_cours: Nom du cours
        :param niveau_cours: Niveau du cours ('A', 'B', 'C')
        """
        self.code_cours = code_cours
        self.intitule_cours = intitule_cours
        self.niveau_cours = niveau_cours

    def __str__(self):
        return "%s %s: niveau %s" %(self.code_cours, self.intitule_cours, self.niveau_cours)