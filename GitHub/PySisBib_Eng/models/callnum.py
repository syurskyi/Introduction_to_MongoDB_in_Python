class CallNum():

    def __init__(self, classif_cdd, composicao, ano, vol, exemp):
        self.classif_cdd = classif_cdd
        self.composicao = composicao
        self.ano = ano
        self.vol = vol
        self.exemp = exemp

    def __str__(self):
        return '{}{}{:02d}{:02d}{:02d}'.format(self.classif_cdd, self.composicao,
               self.ano, self.vol, self.exemp)
