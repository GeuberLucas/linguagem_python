class Ingresso:
    valor_ingresso: None
    valor_ad = None
    valor_ad1 = None

    def setvalor(self, v_ingresso):
        self.valor_ingresso = v_ingresso

    def setvalorad(self, valor_ad_vip):
        self.valor_ad = valor_ad_vip

    def setvalorad1(self, valor_ad_camarote):
        self.valor_ad1 = valor_ad_camarote


class VIP(Ingresso):
    valor_vip = None

    def setvip(self):
        self.valor_vip = self.valor_ad + self.valor_ingresso

    def getvip(self):
        return self.valor_vip


class Normal(Ingresso):
    valor_normal = None

    def setnormal(self):
        self.valor_normal = self.valor_ingresso

    def getnormal(self):
        return print('Valor Normal (R$' + str(self.valor_normal) + ')')


class Meia(Ingresso):
    valor_meia = None

    def setmeia(self):
        self.valor_meia = self.valor_ingresso / 2


class CamaroteInferior(VIP):
    localizacao = None
    valor_inf = None

    def setloceval(self, localizacao):
        self.localizacao = localizacao
        self.valor_inf = self.valor_vip


class CamaroteSuperior(VIP):
    loc_sup = None
    valor_sup = None

    def setsup(self, localizacao):
        self.loc_sup = localizacao
        self.valor_sup = self.valor_vip + self.valor_ad1


class Superclasse(Ingresso, Normal, Meia, CamaroteInferior, CamaroteSuperior):

    def nusa(self):
        print('bom evento')
