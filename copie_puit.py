import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.figure import Figure


class InterfaceGraphique(tk.Tk):

    def quit_fullscreen(self, event):
        self.attributes("-fullscreen", False)

    def __init__(self, n_max):
        tk.Tk.__init__(self)

        # variables de départs
        self.m = 1
        self.hbar = 1
        self.V_0 = 1
        # theme graphique
        style_scale = ttk.Style()
        style_scale.theme_use('clam')
        style_scale.configure("Phos.Horizontal.TScale",
                        background='#050709',
                        troughcolor='#2B0136',
                        sliderthickness=16,
                        sliderrelief="flat",
                        borderwidth=0)
        style_checkbutton = ttk.Style()
        style_checkbutton.theme_use('clam')
        style_checkbutton.configure("Phos.TCheckbutton",
                        background='#050709',
                        foreground='white',
                        font=('Arial', 10))

        # nombre max de niveau d'énergie voulu
        self.n_max = n_max

        # Configuration de la grille
        self.title('Simulation du puits quantique')
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", self.quit_fullscreen)

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)

        self.control_frame = tk.Frame(self, bg="red", bd=2, relief="solid")
        self.control_frame.grid(row=1, column=0, sticky='nsew')
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.panel_frame = tk.Frame(self, bg="pink", bd=2, relief="solid")
        self.panel_frame.grid(row=1, column=1, sticky='nsew')
        self.panel_frame.grid_columnconfigure(0, weight=1)
        self.panel_frame.grid_rowconfigure(0, weight=1)
        self.headcontrol_frame = tk.Frame(self, bg="green",
                                          bd=2, relief="solid")
        self.headcontrol_frame.grid(row=0, column=0, sticky='nsew')
        self.headpanel_frame = tk.Frame(self, bg="grey", bd=2, relief="solid")
        self.headpanel_frame.grid(row=0, column=1, sticky='nsew')
        self.Frame_largeur = tk.Frame(self.control_frame, bg='black', bd=2, relief="solid", pady=15)
        self.Frame_largeur.grid(row=0, column=0, sticky='ew')
        self.Frame_largeur.grid_columnconfigure(0, weight=1)
        self.Frame_hauteur = tk.Frame(self.control_frame, bg='blue', bd=2, relief="solid", pady=15)
        self.Frame_hauteur.grid(row=1, column=0, sticky='ew')
        self.Frame_hauteur.grid_columnconfigure(0, weight=1)
        self.Frame_affichage = tk.Frame(self.control_frame, bg='purple', bd=2, relief="solid", pady=15)
        self.Frame_affichage.grid(row=2, column=0, sticky='ew')
        self.Frame_affichage.grid_columnconfigure(0, weight=1)

        # les labels des différentes frames
        label_headcontrol = tk.Label(self.headcontrol_frame,
                                     text='Panneau de controle')
        label_headcontrol.grid(row=0, column=0)

        label_headpanel = tk.Label(self.headpanel_frame,
                                   text='affichage graphique')
        label_headpanel.grid(row=0, column=0)

        # figure matplotlib
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # insertion dans subplot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky='nsew')

        # Label qui affiche la valeur largeur
        self.largeur_label = tk.Label(self.Frame_largeur, text='1')
        self.largeur_label.grid(row=1, column=0, sticky='')

        largeur = tk.Label(self.Frame_largeur, text='largeur a :')
        largeur.grid(row=0, column=0, sticky='')

        # variables qui controle les checkbutton
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()

        # label qui affiche la hauteur du puit
        self.hauteur_label = tk.Label(self.Frame_hauteur, text='1')
        self.hauteur_label.grid(row=1, column=0, sticky='')

        self.hauteur_text = tk.Label(self.Frame_hauteur, text='potentiel v :')
        self.hauteur_text.grid(row=0, column=0, sticky='')

        # Bouton potentiel v
        self.Hauteur_puit = ttk.Scale(self.Frame_hauteur, from_=1, to=25,
                                      command=self.refresh, orient='horizontal',
                                      style="Phos.Horizontal.TScale")
        self.Hauteur_puit.grid(row=2, column=0, sticky='')

        # ici ce sera la largeur a du puit
        self.Largeur_puit = ttk.Scale(self.Frame_largeur, from_=1,
                                       to=25, command=self.refresh,
                                       orient='horizontal', style="Phos.Horizontal.TScale")
        self.Largeur_puit.set(1)
        self.Largeur_puit.grid(row=2, column=0, sticky='')

        # Bouton a check permettant d'activer et désactiver le potentiel infini
        self.var1 = tk.BooleanVar()
        self.infinibout = ttk.Checkbutton(self.Frame_affichage,
                                         text='potentiel infini',
                                         variable=self.var1,
                                         style="Phos.TCheckbutton",
                                         command=lambda: self.infini())
        self.infinibout.grid(row=0, column=0, sticky='')

        # Bouton permettant d'activer et désactiver la densité de proba
        self.var2 = tk.BooleanVar()
        self.probabout = ttk.Checkbutton(self.Frame_affichage,
                                        text='densité de proba',
                                        variable=self.var2,
                                        style="Phos.TCheckbutton",
                                        command=lambda: self.refresh())
        self.probabout.grid(row=1, column=0, sticky='')

        # fonction pour afficher le graphe
        self.puit_fini()

    # fonction permettant de passer d'un puit fini à infini
    # et faire disparaitre la spinbox de potenitel
    def infini(self):

        if self.var1.get():
            if self.var2.get():
                self.Hauteur_puit.destroy()
                self.hauteur_label = tk.Label(self.Frame_hauteur, text='\u221e')
                self.hauteur_label.grid(row=1, column=0, sticky='')
                self.proba_infini()
            else:
                self.Hauteur_puit.destroy()
                self.hauteur_label = tk.Label(self.Frame_hauteur, text='\u221e')
                self.hauteur_label.grid(row=1, column=0, sticky='')
                self.puit_infini()
        else:
            self.Hauteur_puit = ttk.Scale(self.Frame_hauteur, from_=1,
                                       to=25, command=self.refresh,
                                       orient='horizontal', style="Phos.Horizontal.TScale")
            self.Hauteur_puit.grid(row=2, column=0, sticky='')
            self.hauteur_text = tk.Label(self.Frame_hauteur,
                                         text='potentiel v :')
            self.hauteur_text.grid(row=0, column=0, sticky='')
            self.hauteur_label = tk.Label(self.Frame_hauteur, text='1')
            self.hauteur_label.grid(row=1, column=0, sticky='')
            if self.var2.get():
                self.proba()
            else:
                self.puit_fini()

    # fonction d'onde pour le puit infini
    def puit_infini(self):

        self.ax.clear()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.axvline(int(L), color='grey', linestyle='--')
        self.ax.axvline(-int(L), color='grey', linestyle='--')
        psy = np.zeros_like(x)
        absol = np.abs(x) <= int(L)
        for n in range(1, self.n_max+1):
            E = (n * np.pi) ** 2 / (8 * int(L) ** 2)
            if n % 2 == 0:
                psy[absol] = (1/(np.sqrt(int(L)))) * (np.sin(n * np.pi * x[absol] / (2 * int(L))))
            else:
                psy[absol] = (1/(np.sqrt(int(L)))) * (np.cos(n * np.pi * x[absol] / (2 * int(L))))
            self.ax.plot(x, psy + E)
        self.ax.set_ylim(0.2*(1 * np.pi) ** 2 / (8 * int(L) ** 2),
                         (self.n_max * np.pi) ** 2 / (8 * int(L) ** 2)*1.1)
        self.canvas.draw()

    # fonctions pour le puit fini
    def k(self, e):
        return np.sqrt(2*self.m*(self.V_0-e))/self.hbar

    def q(self, e):
        return np.sqrt(2*self.m*e)/self.hbar

    # dichotimie pour trouver les En
    def e_n(self):
        self.V_0 = max(1, int(self.Hauteur_puit.get()))  # minimum 1
        self.itv = np.linspace(1e-6, self.V_0-1e-6, 10000)
        L = self.Largeur_puit.get()
        valeurs = []
        parite = []
        Ep = [self.q(i) * np.tan(self.q(i) *
                                 int(L)) - self.k(i) for i in self.itv]
        Ei = [self.q(i) / np.tan(self.q(i) *
                                 int(L)) + self.k(i) for i in self.itv]
        for i in range(len(self.itv)-1):
            if Ep[i]*Ep[i+1] < 0:
                if abs(Ep[i]-Ep[i+1]) > 10:
                    continue
                else:
                    valeurs.append(float(round(self.itv[i], 3)))
                    parite.append("pair")
            elif Ei[i]*Ei[i+1] < 0:
                if abs(Ei[i] - Ei[i+1]) > 10:
                    continue
                else:
                    valeurs.append(float(round(self.itv[i], 3)))
                    parite.append("impair")
        return valeurs, parite

    # calculs des coeffs des fonctions d'ondes
    def coeff(self):
        B1 = []
        B2 = []
        B3 = []
        valeurs, parite = self.e_n()
        for i in range(len(parite)):
            a = int(self.Largeur_puit.get())
            Ei = valeurs[i]
            qi = self.q(Ei)
            ki = self.k(Ei)
            if parite[i] == "pair":
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

    # fonction du puit fini.
    def puit_fini(self):
        maxi = []
        mini = []
        self.ax.clear()
        coefficients = self.coeff()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.axvline(int(L), color='grey', linestyle='--')
        self.ax.axvline(-int(L), color='grey', linestyle='--')
        region1 = x < -int(L)
        region2 = np.abs(x) <= int(L)
        region3 = x > int(L)
        psy = np.zeros_like(x)
        valeurs, parite = self.e_n()

        for n in range(len(valeurs)):
            if parite[n] == 'pair':

                psy[region1] = coefficients[n][0]*(np.exp(self.k(valeurs[n]) * x[region1]))

                psy[region2] = coefficients[n][1]*np.cos(self.q(valeurs[n]) * x[region2])

                psy[region3] = coefficients[n][2]*(np.exp(self.k(valeurs[n]) * (-x[region3])))

            elif parite[n] == 'impair':

                psy[region1] = coefficients[n][0]*(np.exp(self.k(valeurs[n]) * x[region1]))

                psy[region2] = coefficients[n][1]*np.sin(self.q(valeurs[n]) * x[region2])

                psy[region3] = coefficients[n][2]*(np.exp(self.k(valeurs[n]) * (-x[region3])))

            self.ax.plot(x, psy + valeurs[n])
            self.ax.axhline(valeurs[n], 0.01, 0.99, color="black",
                            linewidth=0.7)
            maxi.append(np.max(psy[region2]))
            mini.append(np.min(psy[region1]))
        self.ax.set_ylim(0.9*(np.min(mini)+valeurs[0]),
                         1.1*(np.max(maxi)+valeurs[len(valeurs)-1]))
        self.canvas.draw()

    # Fonction qui donne la densité de probabilité
    # dans un puit fini

    def proba(self):
        maxi = []
        mini = []
        coefficients = self.coeff()
        self.ax.clear()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.axvline(int(L), color='grey', linestyle='--')
        self.ax.axvline(-int(L), color='grey', linestyle='--')
        region1 = x < -int(L)
        region2 = np.abs(x) <= int(L)
        region3 = x > int(L)
        psy = np.zeros_like(x)
        valeurs, parite = self.e_n()

        for n in range(len(valeurs)):
            if parite[n] == 'pair':

                psy[region1] = (coefficients[n][0]*np.exp(self.k(valeurs[n]) * x[region1]))**2

                psy[region2] = (coefficients[n][1]*np.cos(self.q(valeurs[n]) * x[region2]))**2

                psy[region3] = (coefficients[n][2]*np.exp(self.k(valeurs[n]) * (-x[region3])))**2

            elif parite[n] == 'impair':

                psy[region1] = (coefficients[n][0]*np.exp(self.k(valeurs[n]) * x[region1]))**2

                psy[region2] = (coefficients[n][1]*np.sin(self.q(valeurs[n]) * x[region2]))**2

                psy[region3] = (coefficients[n][2]*np.exp(self.k(valeurs[n]) * (-x[region3])))**2

            self.ax.plot(x, psy + valeurs[n])
            self.ax.fill_between(x, psy + valeurs[n], valeurs[n], alpha=0.2)
            self.ax.axhline(valeurs[n], 0.01, 0.99, color="black",
                            linewidth=0.7)
            maxi.append(np.max(psy[region2]))
            mini.append(np.min(psy[region1]))
        self.ax.set_ylim(0.9*(np.min(mini)+valeurs[0]),
                         1.1*(np.max(maxi)+valeurs[len(valeurs)-1]))
        self.canvas.draw()

    # fonction d'onde pour la proba en puit infini
    def proba_infini(self):

        self.ax.clear()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.axvline(int(L), color='grey', linestyle='--')
        self.ax.axvline(-int(L), color='grey', linestyle='--')
        psy = np.zeros_like(x)
        absol = np.abs(x) <= int(L)
        for n in range(1, self.n_max+1):
            E = (n * np.pi) ** 2 / (8 * int(L) ** 2)
            if n % 2 == 0:
                psy[absol] = ((1/(np.sqrt(int(L)))) * (np.sin(n * np.pi * x[absol] / (2 * int(L)))))**2
            else:
                psy[absol] = ((1/(np.sqrt(int(L)))) * (np.cos(n * np.pi * x[absol] / (2 * int(L)))))**2
            self.ax.plot(x, psy + E)
            self.ax.fill_between(x, psy + E, E, alpha=0.2)
        self.ax.set_ylim(0.2*(1 * np.pi) ** 2 / (8 * int(L) ** 2),
                         (self.n_max * np.pi) ** 2 / (8 * int(L) ** 2)*1.1)
        self.canvas.draw()

    # fonction pour update les xlim et les fonction d'onde
    # quand on touche aux boutons
    def refresh(self, *args):
        self.largeur_label.config(text=f'{int(self.Largeur_puit.get())}')   # actualises les labels pour les scales
        if self.var1.get():
            if self.var2.get():
                self.proba_infini()
            else:
                self.puit_infini()
        else:
            self.hauteur_label.config(text=f'{int(self.Hauteur_puit.get())}')
            if self.var2.get():
                self.proba()
            else:
                self.puit_fini()


Interface = InterfaceGraphique(6)
Interface.mainloop()
