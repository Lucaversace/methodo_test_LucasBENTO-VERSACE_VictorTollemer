class Echo:
    def __init__(self, langue, temps_journee):
        self.temps_journee = temps_journee
        self.langue = langue

    def bien_dit(self):
        return self.langue.feliciter()

    def saluer(self):
        return self.langue.saluer(self.temps_journee)

    def au_revoir(self):
        return self.langue.dire_au_revoir()

    def refleter(self, texte):
        miroir = texte[::-1]
        return self.saluer() + miroir + (self.bien_dit() if miroir == texte else "") + self.au_revoir()
