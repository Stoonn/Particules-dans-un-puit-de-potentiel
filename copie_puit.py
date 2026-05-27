import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.figure import Figure


class InterfaceGraphique(tk.Tk):

    def style_ax(self):
        self.ax.tick_params(colors='#00ff6e')
        self.ax.xaxis.label.set_color('#00ff6e')
        self.ax.yaxis.label.set_color('#00ff6e')
        for sp in self.ax.spines.values():
            sp.set_color('#00ff6e')

    def quit_fullscreen(self, event):
        self.attributes("-fullscreen", False)

    def __init__(self, n_max):
        tk.Tk.__init__(self)

        # variables de départs
        self.mode_puits = 'fini'   
        self.mode_affichage = 'onde'  
        self.FONT_MONO = "Courier New"
        self.m = 1
        self.hbar = 1
        self.V_0 = 1
        self.WF = ["#00ff6e", "#00ffe0", "#ffb830", "#ff6b6b",
                   "#c77dff", "#4da6ff", "#ff9f1c", "#80ffdb"]
        # theme graphique
        style_scale = ttk.Style()
        style_scale.theme_use('clam')
        style_scale.configure("Phos.Horizontal.TScale",
                        background='#080b0f',
                        troughcolor='#1e4028',
                        sliderthickness=16,
                        sliderrelief="flat",
                        borderwidth=0)

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

        self.control_frame = tk.Frame(self, bg="#0c1018",
                                      relief="sunken", bd=1)
        self.control_frame.grid(row=1, column=0, sticky='nsew')
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.panel_frame = tk.Frame(self, bg="#080b0f",
                                    relief="sunken", bd=1)
        self.panel_frame.grid(row=1, column=1, sticky='nsew')
        self.panel_frame.grid_columnconfigure(0, weight=1)
        self.panel_frame.grid_rowconfigure(0, weight=1)
        self.headcontrol_frame = tk.Frame(self, bg="#080b0f",
                                          relief="sunken", bd=1)
        self.headcontrol_frame.grid(row=0, column=0, sticky='nsew')
        self.headcontrol_frame.grid_columnconfigure(0, weight=1)
        self.headpanel_frame = tk.Frame(self, bg="#0c1018",
                                        relief="sunken", bd=1)
        self.headpanel_frame.grid(row=0, column=1, sticky='nsew')
        self.headpanel_frame.grid_columnconfigure(0, weight=1)
        self.headpanel_frame.grid_rowconfigure(1, weight=1)
        self.Frame_largeur = tk.Frame(self.control_frame, bg='#080b0f',
                                      relief="sunken", bd=1, pady=15)
        self.Frame_largeur.grid(row=0, column=0, sticky='ew')
        self.Frame_largeur.grid_columnconfigure(0, weight=1)
        self.Frame_hauteur = tk.Frame(self.control_frame, bg='#080b0f',
                                      relief="sunken", bd=1, pady=15)
        self.Frame_hauteur.grid(row=1, column=0, sticky='ew')
        self.Frame_hauteur.grid_columnconfigure(0, weight=1)
        self.Frame_affichage = tk.Frame(self.control_frame, bg='#080b0f',
                                        relief="sunken", bd=1, pady=15)
        self.Frame_affichage.grid(row=2, column=0, sticky='ew')
        self.Frame_affichage.grid_columnconfigure(0, weight=1)
        self.Frame_bouton = tk.Frame(self.Frame_affichage, bg='#080b0f',
                                        relief="flat", pady=15)
        self.Frame_bouton.grid(row=1, column=0, sticky='ew')
        self.Frame_bouton.grid_columnconfigure(0, weight=1)
        self.Frame_bouton.grid_columnconfigure(1, weight=1)


        # les labels des différentes frames
        label_headcontrol1 = tk.Label(self.headcontrol_frame,
                                     text='PANNEAU DE CONTROLE',
                                     font=(self.FONT_MONO, 11, "bold"),
                                     fg='#7ecf93', bg='#080b0f', pady=20)
        label_headcontrol1.grid(row=1, column=0, sticky='')
        label_headcontrol2 = tk.Label(self.headcontrol_frame,
                                     text='PROJET NUMERIQUE DMP400',
                                     font=(self.FONT_MONO, 11, "bold"),
                                     fg='#7ecf93', bg='#080b0f')
        label_headcontrol2.grid(row=0, column=0, sticky='nw')

        label_headpanel = tk.Label(self.headpanel_frame,
                                   text='AFFICHAGE GRAPHIQUE',
                                   font=(self.FONT_MONO, 11, "bold"),
                                   fg='#7ecf93', bg='#080b0f')
        label_headpanel.grid(row=0, column=0)
        label_headpanel2 = tk.Label(self.headpanel_frame,
                                   text='MODELISATION DU PUIT DE POTENTIEL QUANTIQUE',
                                   font=(self.FONT_MONO, 11, "bold"),
                                   fg='#7ecf93', bg='#080b0f')
        label_headpanel2.grid(row=1, column=0, sticky ='')



        # figure matplotlib
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)

        # insertion dans subplot
        self.fig = Figure(facecolor='#080b0f')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#0f2d15')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.panel_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0,
                                        sticky='nsew', padx=50, pady=50)
        self.canvas.get_tk_widget().configure(bg="#080b0f", highlightthickness=0)
        # Label qui affiche la valeur largeur
        self.largeur_label = tk.Label(self.Frame_largeur,
                                      text=f'LARGEUR a : 1',
                                      font=(self.FONT_MONO, 11, "bold"),
                                      fg='#7ecf93', bg='#080b0f')
        self.largeur_label.grid(row=2, column=0, sticky='', pady=20)

        largeur_label2 = tk.Label(self.Frame_largeur,
                                  text='\u25B6 PARAMETRE a (demi largeur du puit)',
                                  font=(self.FONT_MONO, 11, "bold"),
                                  fg='#7ecf93', bg='#080b0f')
        largeur_label2.grid(row=0, column=0, sticky='nw')

        # variables qui controle les checkbutton
        self.bout_fini = tk.Button(self.Frame_bouton, text='FINI',
                            command=self.mode_fini,
                            bg='#0c1018', fg='#c8ffd4',
                            font=(self.FONT_MONO, 11, 'bold'),
                            relief='raised', width=15)
        self.bout_fini.grid(row=0, column=0, sticky='', pady=25)

        self.bout_infini = tk.Button(self.Frame_bouton, text='INFINI',
                              command=self.mode_infini,
                              bg='#0c1018', fg='#c8ffd4',
                              font=(self.FONT_MONO, 11, 'bold'),
                              relief='raised', width=15)
        self.bout_infini.grid(row=0, column=1, sticky='', pady=25)
        self.bout_onde = tk.Button(self.Frame_bouton, text='ONDE',
                            command=self.mode_onde,
                            bg='#0c1018', fg='#c8ffd4',
                            font=(self.FONT_MONO, 11, 'bold'),
                            relief='raised', width=15)
        self.bout_onde.grid(row=1, column=0, sticky='', pady=25)

        self.bout_proba = tk.Button(self.Frame_bouton, text='PROBA',
                             command=self.mode_proba,
                             bg='#0c1018', fg='#c8ffd4',
                             font=(self.FONT_MONO, 11, 'bold'),
                             relief='raised', width=15)
        self.bout_proba.grid(row=1, column=1, sticky='', pady=25)

        # label qui affiche la hauteur du puit
        self.hauteur_label = tk.Label(self.Frame_hauteur,
                                      text=f'POTENTIEL V : 1',
                                      font=(self.FONT_MONO, 11, "bold"),
                                      fg='#7ecf93', bg='#080b0f')
        self.hauteur_label.grid(row=1, column=0, sticky='', pady=20)

        largeur_label2 = tk.Label(self.Frame_hauteur,
                                  text='\u25B6 PARAMETRE V (hauteur du puit)',
                                  font=(self.FONT_MONO, 11, "bold"),
                                  fg='#7ecf93', bg='#080b0f')
        largeur_label2.grid(row=0, column=0, sticky='nw')

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
        self.Largeur_puit.grid(row=3, column=0, sticky='')

        # Bouton a check permettant d'activer et désactiver le potentiel infini
        self.affichage_label = tk.Label(self.Frame_affichage,
                                        text='\u25B6 MODE D\'AFFICHAGE',
                                        font=(self.FONT_MONO, 11, "bold"),
                                        fg='#7ecf93', bg='#080b0f')
        self.affichage_label.grid(row=0, column=0, sticky='nw')

        # fonction pour afficher le graphe
        self.puit_fini()
    
    # fonction d'onde pour le puit infini
    def puit_infini(self):

        self.ax.clear()
        self.style_ax()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.set_facecolor('#0f2d15')
        self.ax.axvline(int(L), color='#00ff6e', linestyle='--')
        self.ax.axvline(-int(L), color='#00ff6e', linestyle='--')
        self.ax.axvspan(-int(L)*2, -int(L), facecolor='#00ff6e', alpha=0.2)
        self.ax.axvspan(int(L), int(L)*2, facecolor='#00ff6e', alpha=0.2)
        self.ax.grid(True, color='#00ff6e', linewidth=0.5, alpha=0.2)
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
        self.style_ax()
        coefficients = self.coeff()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.set_facecolor('#0f2d15')
        self.ax.axvline(int(L), color='#00ff6e', linestyle='--')
        self.ax.axvline(-int(L), color='#00ff6e', linestyle='--')
        self.ax.axvspan(-int(L)*2, -int(L), facecolor='#00ff6e', alpha=0.2)
        self.ax.axvspan(int(L), int(L)*2, facecolor='#00ff6e', alpha=0.2)
        self.ax.grid(True, color='#00ff6e', linewidth=0.5, alpha=0.2)
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
        self.style_ax()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.set_facecolor('#0f2d15')
        self.ax.axvline(int(L), color='#00ff6e', linestyle='--')
        self.ax.axvline(-int(L), color='#00ff6e', linestyle='--')
        self.ax.axvspan(-int(L)*2, -int(L), facecolor='#00ff6e', alpha=0.2)
        self.ax.axvspan(int(L), int(L)*2, facecolor='#00ff6e', alpha=0.2)
        self.ax.grid(True, color='#00ff6e', linewidth=0.5, alpha=0.2)
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
        self.style_ax()
        L = self.Largeur_puit.get()
        x = np.linspace(-int(L) * 2, int(L) * 2, 2000)
        self.ax.axvline(int(L), color='grey', linestyle='--')
        self.ax.axvline(-int(L), color='grey', linestyle='--')
        self.ax.set_facecolor('#0f2d15')
        self.ax.axvspan(-int(L), int(L), facecolor='#0a1f0e', alpha=0.3)
        self.ax.grid(True, color='black', linewidth=0.5, alpha=0.3)
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
    def mode_fini(self):
        self.mode_puits = 'fini'
        if self.mode_affichage == 'proba':
            self.proba()
        else:
            self.puit_fini()

    def mode_infini(self):
        self.mode_puits = 'infini'
        if self.mode_affichage == 'proba':
            self.proba_infini()
        else:
            self.puit_infini()

    def mode_onde(self):
        self.mode_affichage = 'onde'
        if self.mode_puits == 'infini':
            self.puit_infini()
        else:
            self.puit_fini()

    def mode_proba(self):
        self.mode_affichage = 'proba'
        if self.mode_puits == 'infini':
            self.proba_infini()
        else:
            self.proba()
    # quand on touche aux boutons
    def refresh(self, *args):
        self.largeur_label.config(text=f'LARGEUR a : {int(self.Largeur_puit.get())}',
                                  font=(self.FONT_MONO, 11, "bold"),
                                  fg='#7ecf93', bg='#080b0f')   # actualises les labels pour les scales
        if self.mode_puits == 'infini':
            if self.mode_affichage == 'proba':
                self.proba_infini()
            else:
                self.puit_infini()
        else:
            self.hauteur_label.config(text=f'POTENTIEL V : {int(self.Hauteur_puit.get())}',
                                      font=(self.FONT_MONO, 11, "bold"),
                                      fg='#7ecf93', bg='#080b0f')

            if self.mode_affichage == 'proba':
                self.proba()
            else:
                self.puit_fini()


Interface = InterfaceGraphique(6)
Interface.mainloop()
