import math


class Rigidity:
    c = 299792458
    elec = 1.6021E-19

    def __init__(self, m0u, Ekin, type, Q):
        self.m0u = m0u
        self.m0kg = self.m0u * 1.66054E-27
        self.EkinJ = self.getEkinV(Ekin, type) * 1.6E-13
        self.Erest = self.m0kg * (self.c ** 2)
        self.Etotal = self.EkinJ + self.Erest
        self.Q = Q
        self.q = Q * self.elec
        self.gamma = (self.EkinJ / self.Erest) + 1
        self.beta = math.sqrt(1 - ((1 / self.gamma) ** 2))
        self.v = self.beta * self.c

    def getEkinV(self, Ekin, type):
        if type == "MeV":
            return Ekin
        elif type == "AMeV":
            return Ekin * 238
        elif type == "MeV/u":
            return Ekin * 196.9665701
        elif type == "TeV":
            return Ekin * 1.0E+6
        elif type== "GeV":
            return Ekin * 1.0E+3

    def get(self):
        return (self.m0kg * self.gamma * self.v) / self.q


Uranium_Ion = Rigidity(238.050787, 90, "AMeV", 28).get()
Gold_Ion = Rigidity(196.9665701, 330, "MeV/u", 77).get()
Protons = Rigidity(1.00782503224, 7, "TeV", 1).get()
Electrons = Rigidity(5.5E-4, 10, "GeV", 1).get()

print(Uranium_Ion)
print(Gold_Ion)
print(Protons)
print(Electrons)
