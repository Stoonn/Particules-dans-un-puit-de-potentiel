import numpy as np
a = 4.39
hbar = 1
m = 1
V_0 = 6
itv = np.linspace(1e-6,V_0-1e-6,10000)

def k(e):
    return np.sqrt(2*m*(V_0-e))/hbar,
def q(e):
    return np.sqrt(2*m*e)/hbar

def e_n():
    valeurs = []
    parite = []
    Ep = [q(i)*np.tan(q(i)*a) - k(i) for i in itv]
    Ei = [q(i)/np.tan(q(i)*a) + k(i) for i in itv]
    for i in range(len(itv)-1):
        if Ep[i]*Ep[i+1] < 0:
            valeurs.append((abs(Ep[i])+abs(Ep[i+1]))/2)
            parite.append("pair")
        elif Ei[i]*Ei[i+1] < 0:
            valeurs.append((abs(Ei[i])+abs(Ei[i+1]))/2)
            parite.append("impair")
    return valeurs,parite
print(len(e_n()[1]),e_n())