class Etudiant:
    def __init__(self, numero_etudiant, prenom_etudiant, nom_etudiant, niveau_etudiant):
        """
            :param numero_etudiant: numero de l'etudiant (identificateur)
            :param prenom_etudiant: prenom de l'etudiant
            :param nom_etudiant: nom de l'etudiant
            :param niveau_etudiant: niveau de l'etudiant ('A', 'B' ou 'C')
        """
        self.numero_etudiant = numero_etudiant
        self.prenom_etudiant = prenom_etudiant
        self.nom_etudiant = nom_etudiant
        self.niveau_etudiant = niveau_etudiant

    def __str__(self):
        return "%s %s, numero %d, niveau %s" %(self.prenom_etudiant, self.nom_etudiant, self.numero_etudiant, self.niveau_etudiant)

