import numpy as np
a = 4.39
hbar = 1
m = 1
V_0 = 6
itv = np.linspace(1e-6, V_0-1e-6, 10000)


def k(e):
    return np.sqrt(2*m*(V_0-e))/hbar


def q(e):
    return np.sqrt(2*m*e)/hbar


def e_n():
    valeurs = []
    parite = []
    Ep = [q(i) * np.tan(q(i) * a) - k(i) for i in itv]
    Ei = [q(i) / np.tan(q(i) * a) + k(i) for i in itv]
    for i in range(len(itv)-1):
        if Ep[i]*Ep[i+1] < 0:
            if abs(Ep[i]-Ep[i+1]) > 10:
                continue
            else:
                valeurs.append(float(round(itv[i], 3)))
                parite.append("pair")
        elif Ei[i]*Ei[i+1] < 0:
            if abs(Ei[i] - Ei[i+1]) > 10:
                continue
            else:
                valeurs.append(float(round(itv[i], 3)))
                parite.append("impair")
    return list(zip(valeurs, parite))


print(e_n())
print(np.cos(q(e_n()[2][0])*a))

# calculs des coefficients des fonctions d'ondes dans les différentes zones


def coeff(x):
    B1 = []
    B2 = []
    B3 = []
    for i in x:
        E = i[0]
        qi = q(E)
        ki = k(E)
        if i[1] == "pair":
            norm = float(np.sqrt(a + np.sin(2*qi*a)/(2*qi) + np.cos(qi*a)**2 / ki))
            B = round(1.0 / norm, 4)
            A = float(round(B * np.exp(ki*a) * np.cos(qi*a), 4))
            B1.append(A)
            B2.append(B)
            B3.append(A)
        else:
            norm = float(np.sqrt(a - np.sin(2*qi*a)/(2*qi) + np.sin(qi*a)**2 / ki))
            B = round(1.0 / norm, 4)
            A = float(round(B * np.exp(ki*a) * np.sin(qi*a), 4))
            B1.append(-A)
            B2.append(B)
            B3.append(A)
    return list(zip(B1, B2, B3))


print(coeff(e_n()))
