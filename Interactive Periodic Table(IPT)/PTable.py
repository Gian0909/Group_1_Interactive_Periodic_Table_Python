import tkinter as tk
from PIL import ImageTk, Image
from tkinter import *
from tkinter.messagebox import showerror
import mysql.connector


# Creates and Initiates class 'App'


class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.winfo_toplevel().title("Periodic Table of the Elements")
        self.topLabel = tk.Label(self, text="Interactive Periodic Table of Elements", font=("Sans serif", 18, "bold"),
                                 bg="#3f3f3f", fg="white")
        self.winfo_toplevel().iconbitmap('icons\myIcon.ico')
        self.configure(background="#3f3f3f")
        self.winfo_toplevel().resizable(False, False)
        # self.winfo_toplevel().geometry("900x700")
        self.topLabel.grid(row=0, column=0, columnspan=20)

        # Names of tk.Buttons in column 1
        self.fillerLine = tk.Label(self, text="", width=5, bg="#3f3f3f")
        self.fillerLine.grid(row=0, column=0)

        hydrogen_btn = [('H', 'Hydrogen',
                         'Atomic #1\nAtomic mass:1.0078 u\nMelting point:-259.16°C (13.99 K)\nBoiling point:-252.87°C (20.28 K)\nDiscovery date:1766 by:Cavendish H. \nState = Gas\nElement Group = Reactive nonmetals')]
        btn_row = 2
        btn_column = 1
        for b in hydrogen_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2a4165", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Li2Fr = [('Li', 'Lithium',
                  'Atomic #3\nAtomic mass:6.9410 u\nMelting point:180.54°C (453.69 K)\nBoiling point:1342°C (1615.15 K)\nDiscovery date:1817 by: Arfwedson J.A. \nState = Solid\nElement Group = Alkali Metals'),
                 ('Na', 'Sodium',
                  'Atomic # = 11\nAtomic mass:22.990 u\nMelting point:97.79°C (370.94 K)\nBoiling point:882.85°C (1156 K)\nDiscovery date:1807 by: Davy H. \nState = Solid\nElement Group = Alkali Metals'),
                 ('K', 'Potassium',
                  'Atomic # = 19\nAtomic mass:39.098 u\nMelting point:63.5°C (336.65 K)\nBoiling point:758.85°C (1032 K)\nDiscovery date:1807 by:Davy H. \nState = Solid\nElement Group = Alkali Metals'),
                 ('Rb', 'Rubidium',
                  'Atomic # = 37\nAtomic mass:85.468 u\nMelting point:39.48°C (312.63 K)\nBoiling point:688°C (961.15 K)\nDiscovery date:1861 by:Kirchhoff G., Bunsen, R. \nState = Solid\nElement Group = Alkali Metals'),
                 ('Cs', 'Caesium',
                  'Atomic # = 55\nAtomic mass:132.91 u\nMelting point:28.44°C (301.59 K)\nBoiling point:670.85°C (944 K)\nDiscovery date:1860 by:Kirchhoff G., Bunsen, R.\nState = Solid\nElement Group = Alkali Metals'),
                 ('Fr', 'Francium',
                  'Atomic # = 87\nAtomic mass:223 u\nMelting point:27°C (300.15 K)\nBoiling point:676.85°C (950 K)\nDiscovery date:1939 by:Perey, M.\nState = Solid\nElement Group = Alkali Metals')]
        # create all tk.Buttons with a loop
        btn_row = 3
        btn_column = 1
        for b in Li2Fr:
            tk.Button(self, text=b[0], width=5, height=2, bg="#244d57", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Be2Ra = [('Be', 'Beryllium',
                  'Atomic # = 4\nAtomic mass:9.0122 u\nMelting point: 1286.85°C (1560 K)\nBoiling point:2469°C (2742.15 K)\nDiscovery date:1797 by:Vauquelin L.N. \nState = Solid\nElement Group = Alkali Earth Metals'),
                 ('Mg', 'Magnesium',
                  'Atomic # = 12\nAtomic mass:24.305 u\nMelting point:650°C (923.15 K)\nBoiling point:1091°C (1364.15 K)\nDiscovery date:1755 by: Black J., Davy H. \nState = Solid\nElement Group = Alkali Earth Metals'),
                 ('Ca', 'Calcium',
                  'Atomic # = 20\nAtomic mass:40.078 u\nMelting point:842°C (1115.15 K)\nBoiling point:1483.85°C (1757 K)\nDiscovery date:1808 by:Davy H. \nState = Solid\nElement Group = Alkali Earth Metals'),
                 ('Sr', 'Strontium',
                  'Atomic # = 38\nAtomic mass:87.620 u\nMelting point:777°C (1050.15 K)\nBoiling point:1381.85°C (1655 K)\nDiscovery date:1790 by:Davy H.,Crawford A.,Cruickshank W. \nState = Solid\nElement Group = Alkali Earth Metals'),
                 ('Ba', 'Barium',
                  'Atomic # = 56\nAtomic mass:137.33 u\nMelting point:727°C (1000.15 K)\nBoiling point:1897°C (2170.15 K)\nDiscovery date:1808 by:Scheele C.W., Davy H.\nState = Solid\nElement Group = Alkali Earth Metals'),
                 ('Ra', 'Radium',
                  'Atomic # = 88\nAtomic mass:226 u\nMelting point:700°C (973.15 K)\nBoiling point:1737°C (2010.15 K)\nDiscovery date:1898 by:Curie M., Curie P. \nState = Solid\nElement Group = Alkali Earth Metals')]
        btn_row = 3
        btn_column = 2
        for b in Be2Ra:
            tk.Button(self, text=b[0], width=5, height=2, bg="#622e39", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        ScnY = [('Sc', 'Scandium',
                 'Atomic # = 21\nAtomic mass:44.956 u\nMelting point:1540.85°C (1814 K)\nBoiling point:2835.85°C (3109 K)\nDiscovery date:1879 by:Cleve P.T.,Nilson L.F. \nState = Solid\nElement Group = Transition Metals'),
                ('Y', 'Yttrium',
                 'Atomic # = 39\nAtomic mass:88.906 u\nMelting point:1526°C (1799.15 K)\nBoiling point:3337.85°C (3611 K)\nDiscovery date:1794 by:Gadolin J.\nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 3
        for b in ScnY:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Lanthanum_btn = [('La', 'Lanthanum',
                          'Atomic # = 57\nAtomic mass:138.91 u\nMelting point:920°C (1193.15 K)\nBoiling point:3463.85°C (3737 K)\nDiscovery date:1839 by:Mosander C.G. \nState = Solid\nElement Group = Lanthanides')]
        btn_row = 7
        btn_column = 3
        for b in Lanthanum_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#004a77", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Actinium_btn = [('Ac', 'Actinium',
                         'Atomic # = 89\nAtomic mass:227 u\nMelting point:1050°C (1323.15 K)\nBoiling point:3196.85°C (3470 K)\nDiscovery date:1899 by:Debierne A.L. \nState = Solid\nElement Group = Actinides')]
        btn_row = 8
        btn_column = 3
        for b in Actinium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#613b28", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        self.fillerLine = tk.Label(self, text="", width=5, bg="#3f3f3f")
        self.fillerLine.grid(row=0, column=4)

        Ti2Rf = [('Ti', 'Titanium',
                  'Atomic # = 22\nAtomic mass:47.867 u\nMelting point:1668°C (1941.15 K)\nBoiling point:3286.85°C (3560 K)\nDiscovery date:1791 by:Gregor W. \nState = Solid\nElement Group = Transition Metals'),
                 ('Zr', 'Zirconium',
                  'Atomic # = 40\nAtomic mass:50.942 u\nMelting point:1910°C (2183.15 K)\nBoiling point:3407°C (3680.15 K)\nDiscovery date:1801 by: del Río A.M. \nState = Solid\nElement Group = Transition Metals'),
                 ('Hf', 'Hafnium',
                  'Atomic # = 72\nAtomic mass:178.49 u\nMelting point:2227°C (2500.15 K)\nBoiling point:4601.85°C (4875 K)\nDiscovery date:1923 by:de Hevesy G.,Coster G.\nState = Solid\nElement Group = Transition Metals'),
                 ('Rf', 'Rutherfordium',
                  'Atomic # = 104\nAtomic mass:267 u\nMelting point:2100°C (2373.15 K)\nBoiling point: N/A\nDiscovery date:1964 by:Ghiorso A., et al.\nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 5
        for b in Ti2Rf:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 10:
                btn_row = 1
                btn_column += 1

        V2Ha = [('V', 'Vanadium',
                 'Atomic # = 23\nAtomic mass:50.942 u\nMelting point:1910°C (2183.15 K)\nBoiling point:3407°C (3680.15 K)\nDiscovery date:1801 by:del Río A.M. \nState = Solid\nElement Group = Transition Metals'),
                ('Nb', 'Niobium',
                 'Atomic # = 41\nAtomic mass:92.906 u\nMelting point:2468.85°C (2742 K)\nBoiling point:4927°C (5200.15 K)\nDiscovery date:1801 by:Hatchett C. \nState = Solid\nElement Group = Transition Metals'),
                ('Ta', 'Tantalum',
                 'Atomic # = 73\nAtomic mass:180.95 u\nMelting point:3019.85°C (3293 K)\nBoiling point:5456.85°C (5730 K)\nDiscovery date:1802 by:Ekeberg A.G. \nState = Solid\nElement Group = Transition Metals'),
                ('Db', 'Dubnium',
                 'Atomic # = 105\nAtomic mass:262 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1967 by:Ghiorso A. \nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 6
        for b in V2Ha:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 10:
                btn_row = 1
                btn_column += 1

        Cr2Sg = [('Cr', 'Chromium',
                  'Atomic # = 24\nAtomic mass:51.996 u\nMelting point:1907°C (2180.15 K)\nBoiling point:2671.85°C (2945 K)\nDiscovery date:1797 by:Vauquelin L.N. \nState = Solid\nElement Group = Transition Metals'),
                 ('Mo', 'Molybdenum',
                  'Atomic # = 42\nAtomic mass:95.950 u\nMelting point:2622.85°C (2896 K)\nBoiling point:4638.85°C (4912 K)\nDiscovery date:1778 by: Scheele C.W. \nState = Solid\nElement Group = Transition Metals'),
                 ('W', 'Tungsten',
                  'Atomic # = 74\nAtomic mass:183.84 u\nMelting point:3421.85°C (3695 K)\nBoiling point:5555°C (5828.15 K)\nDiscovery date:1783 by:Elhuyar J.J , Elhuyar F. \nState = Solid\nElement Group = Transition Metals'),
                 ('Sg', 'Seaborgium',
                  'Atomic # = 106\nAtomic mass:269 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1974 by:Lawrence Berkeley National Laboratory, Ghiorso A. \nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 7
        for b in Cr2Sg:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Mn2Bh = [('Mn', 'Manganese',
                  'Atomic # = 25\nAtomic mass:54.938 u\nMelting point:1246°C (1519.15 K)\nBoiling point:2061°C (2334.15 K)\nDiscovery date:1774 by: Kaim I.G., Scheele C.W., Gahn J.G \nState = Solid\nElement Group = Transition Metals'),
                 ('Tc', 'Technetium',
                  'Atomic # = 43\nAtomic mass:98 u\nMelting point:2203.85°C (2477 K)\nBoiling point:4264.85°C (4538 K)\nDiscovery date:1937 by:Perrier C., Segrè E. \nState = Solid\nElement Group = Transition Metals'),
                 ('Re', 'Rhenium',
                  'Atomic # = 75\nAtomic mass:186.21 u\nMelting point:3181.85°C (3455 K)\nBoiling point:5596.85°C (5870 K)\nDiscovery date:1925 by:Noddack I., Berg O., Noddack W.\nState = Solid\nElement Group = Transition Metals'),
                 ('Bh', 'Bohrium',
                  'Atomic # = 107\nAtomic mass:264 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1981 by:Armbruster P., Münzenberg G. \nState = Unknown\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 8
        for b in Mn2Bh:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Fe2Hs = [('Fe', 'Iron',
                  'Atomic # = 26\nAtomic mass:55.845 u\nMelting point:1538°C (1811.15 K)\nBoiling point:2862°C (3135.15 K)\nState = Solid\nElement Group = Transition Metals'),
                 ('Ru', 'Ruthenium',
                  'Atomic # = 44\nAtomic mass:101.07 u\nMelting point:2334°C (2607.15 K)\nBoiling point:4150°C (4423.15 K)\nDiscovery date:1844 by:Claus K.E. \nState = Solid\nElement Group = Transition Metals'),
                 ('Os', 'Osmium',
                  'Atomic # = 76\nAtomic mass:190.23 u\nMelting point:3033°C (3306.15 K)\nBoiling point:5026.85°C (5300 K)\nDiscovery date:1803 by:Tennant S. \nState = Solid\nElement Group = Transition Metals'),
                 ('Hs', 'Hassium',
                  'Atomic # = 108\nAtomic mass:269 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1984 by:Münzenberg G., Armbruster P. \nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 9
        for b in Fe2Hs:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Co2Mt = [('Co', 'Cobalt',
                  'Atomic # = 27\nAtomic mass:58.933 u\nMelting point:1495°C (1768.15 K)\nBoiling point:2869.85°C (3143 K)\nDiscovery date:1735 by:Brandt G. \nState = Solid\nElement Group = Transition Metals'),
                 ('Rh', 'Rhodium',
                  'Atomic # = 45\nAtomic mass:102.91 u\nMelting point:1962.85°C (2236 K)\nBoiling point:3696.85°C (3970 K)\nDiscovery date:1803 by:Wollaston W.H. \nState = Solid\nElement Group = Transition Metals'),
                 ('Ir', 'Iridium',
                  'Atomic # = 77\nAtomic mass:192.22 u\nMelting point:2446°C (2719.15 K)\nBoiling point:4428°C (4701.15 K)\nDiscovery date:1803 by:Tennant S. \nState = Solid\nElement Group = Transition Metals'),
                 ('Mt', 'Meitnerium',
                  'Atomic # = 109\nAtomic mass:278 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1982 by:Armbruster P., Münzenberg G.\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 5
        btn_column = 10
        for b in Co2Mt:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Ni2Pt = [('Ni', 'Nickel',
                  'Atomic # = 28\nAtomic mass:58.693 u\nMelting point:1455°C (1728.15 K)\nBoiling point:2730°C (3003.15 K)\nDiscovery date:1751 by:Cronstedt A.X. \nState = Solid\nElement Group = Transition Metals'),
                 ('Pd', 'Palladium',
                  'Atomic # = 46\nAtomic mass:106.42 u\nMelting point:1554.9°C (1828.05 K)\nBoiling point:2963°C (3236.15 K)\nDiscovery date:1803 by:Wollaston W.H. \nState = Solid\nElement Group = Transition Metals'),
                 ('Pt', 'Platinum',
                  'Atomic # = 78\nAtomic mass:195.08 u\nMelting point:1768.3°C (2041.45 K)\nBoiling point:3825°C (4098.15 K)\nDiscovery date:1735 by:de Ulloa A.\nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 11
        for b in Ni2Pt:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Darmstadtium_btn = [('Ds', 'Darmstadtium',
                             'Atomic # = 110\nAtomic mass:281 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1994 by:Hofmann S., Ninov V. \nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 11
        for b in Darmstadtium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Cu2Au = [('Cu', 'Copper',
                  'Atomic # = 29\nAtomic mass:63.546 u\nMelting point:1084.62°C (1357.77 K)\nBoiling point:2562°C (2835.15 K)\nState = Solid\nElement Group = Transition Metals'),
                 ('Ag', 'Silver',
                  'Atomic # = 47\nAtomic mass:107.87 u\nMelting point:961.78°C (1234.93 K)\nBoiling point:2162°C (2435.15 K)\nState = Solid\nElement Group = Transition Metals'),
                 ('Au', 'Gold',
                  'Atomic # = 79\nAtomic mass:196.97 u\nMelting point:1064.18°C (1337.33 K)\nBoiling point:2700°C (2973.15 K)\nState = Solid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 12
        for b in Cu2Au:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Roentgenium_btn = [('Rg', 'Roentgenium',
                            'Atomic # = 111\nAtomic mass:282 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1994 by:Hofmann S., Nino V. \nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 12
        for b in Roentgenium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Zn2Hg = [('Zn', 'Zinc',
                  'Atomic # = 30\nAtomic mass:65.380 u\nMelting point:419.53°C (692.68 K)\nBoiling point:907°C (1180.15 K)\nDiscovery date:1746 by:Andreas Sigismund Marggraf\nState = Solid\nElement Group = Transition Metals'),
                 ('Cd', 'Cadmium',
                  'Atomic # = 48\nAtomic mass:112.41 u\nMelting point:321.11°C (594.26 K)\nBoiling point:766.85°C (1040 K)\nDiscovery date:1817 by:Stromeyer F., Hermann K.S.L\nState = Solid\nElement Group = Transition Metals'),
                 ('Hg', 'Mercury',
                  'Atomic # = 80\nAtomic mass:200.59 u\nMelting point:-38.83°C (234.32 K)\nBoiling point:356.73°C (629.88 K)\nState = Liquid\nElement Group = Transition Metals')]
        btn_row = 5
        btn_column = 13
        for b in Zn2Hg:
            tk.Button(self, text=b[0], width=5, height=2, bg="#433c65", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Copernicium_btn = [('Cn', 'Copernicium',
                            'Atomic # = 112\nAtomic mass:285 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:1996 by:Ninov V., Hofmann S. \nState = Liquid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 13
        for b in Copernicium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Boron_btn = [('B', 'Boron',
                      'Atomic # = 5\nAtomic mass:10.811 u\nMelting point:2076°C (2349.15 K)\nBoiling point:4000°C (4273.15 K)\nDiscovery date:1808 by:Thénard L.J, Humphry D., et al.\nState = Solid\nElement Group = Metalloids')]
        btn_row = 3
        btn_column = 14
        for b in Boron_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#523e1b", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Al2Ti = [('Al', 'Aluminium',
                  'Atomic # = 13\nAtomic mass:26.982 u\nMelting point:660.32°C (933.47 K)\nBoiling point:2470°C (2743.15 K)\nDiscovery date:1825 by: Ørsted H.C. \nState = Solid\nElement Group = Post-transition Metals'),
                 ('Ga', 'Gallium',
                  'Atomic # = 31\nAtomic mass:69.723 u\nMelting point:29.76°C (302.91 K)\nBoiling point:2400°C (2673.15 K)\nDiscovery date:1875 by: de Boisbaudran PE.L. \nState = Solid\nElement Group = Post-transition Metals'),
                 ('In', 'Indium',
                  'Atomic # = 49\nAtomic mass:114.82 u\nMelting point:156.63°C (429.78 K)\nBoiling point:2072°C (2345.15 K)\nDiscovery date:1863 by:Reich F. \nState = Solid\nElement Group = Post-transition Metals'),
                 ('Tl', 'Thallium',
                  'Atomic # = 81\nAtomic mass:204.38 u\nMelting point:303.85°C (577 K)\nBoiling point:1472.85°C (1746 K)\nDiscovery date:1861 by:Crookes W. \nState = Solid\nElement Group = Post-transition Metals')]
        btn_row = 4
        btn_column = 14
        for b in Al2Ti:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2f4d47", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Nihonium_btn = [('Nh', 'Nihonium',
                         'Atomic # = 113\nAtomic mass:286 u\nMelting point: N/A\nBoiling point: N/A\nDiscovery date:2003 by:Riken\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 14
        for b in Nihonium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Carbon_btn = [('C', 'Carbon',
                       'Atomic # = 6\nAtomic mass:12.011 u\nMelting point:3550°C (3823.15 K)\nBoiling point: N/A\nState = Solid\nElement Group = Reactive Nonmetals')]
        btn_row = 3
        btn_column = 15
        for b in Carbon_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2a4165", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        SinGe = [('Si', 'Silicon',
                  'Atomic # = 14\nAtomic mass:28.086 u\nMelting point:1410°C (1683.15 K)\nBoiling point:2355°C (2628.15 K)\nDiscovery date:1823 by:Lavoisier J. ,Berzelius J.J\nState = Solid\nElement Group = Metalloids'),
                 ('Ge', 'Germanium',
                  'Atomic # = 32\nAtomic mass:72.640 u\nMelting point:938.25°C (1211.4 K)\nBoiling point:2833°C (3106.15 K)\nDiscovery date:1886 by:Winkler C. \nState = Solid\nElement Group = Metalloids')]
        btn_row = 4
        btn_column = 15
        for b in SinGe:
            tk.Button(self, text=b[0], width=5, height=2, bg="#523e1b", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        SnnPb = [('Sn', 'Tin',
                  'Atomic # = 50\nAtomic mass:118.71 u\nMelting point:231.93°C (505.08 K)\nBoiling point:2602°C (2875.15 K)\nState = Solid\nElement Group = Post-transition Metals'),
                 ('Pb', 'Lead',
                  'Atomic # = 82\nAtomic mass:207.20 u\nMelting point:327.5°C (600.65 K)\nBoiling point:1749°C (2022.15 K)\nState = Solid\nElement Group = Post-transition Metals')]
        btn_row = 6
        btn_column = 15
        for b in SnnPb:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2f4d47", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Flerovium_btn = [('Fl', 'Flerovium',
                          'Atomic # = 114\nAtomic mass:289 u\Melting point: N/A\nBoiling point: N/A\nDiscovery date:1998 by:Hofmann S., et al.\nState = Liquid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 15
        for b in Flerovium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        NnP = [('N', 'Nitrogen',
                'Atomic # = 7\nAtomic mass:14.007 u\nMelting point:-210.01°C (63.14 K)\nBoiling point:-195.79°C (77.36 K)\nDiscovery date:1772 by:Rutherford D. \nState = Gas\nElement Group = Reactive Nonmetals'),
               ('P', 'Phosphorus',
                'Atomic # = 15\nAtomic mass:30.974 u\nMelting point:44.1°C (317.25 K)\nBoiling point:280.5°C (553.65 K)\nDiscovery date:1669 by: Brand H. \nState = Solid\nElement Group = Reactive Nonmetals')]
        btn_row = 3
        btn_column = 16
        for b in NnP:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2a4165", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        AsnSb = [('As', 'Arsenic',
                  'Atomic # = 33\nAtomic mass:74.922 u\nMelting point:816.85°C (1090 K)\nBoiling point:613°C (886.15 K)\nDiscovery date:1250 by:Magnus A. \nState = Solid\nElement Group = Metalloids'),
                 ('Sb', 'Antimony',
                  'Atomic # = 51\nAtomic mass:121.76 u\nMelting point:630.63°C (903.78 K)\nBoiling point:1586.85°C (1860 K)\nState = Solid\nElement Group = Metalloids')]
        btn_row = 5
        btn_column = 16
        for b in AsnSb:
            tk.Button(self, text=b[0], width=5, height=2, bg="#523e1b", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Bismuth_btn = [('Bi', 'Bismuth',
                        'Atomic # = 83\nAtomic mass:208.98 u\nMelting point:271.41°C (544.56 K)\nBoiling point:1564°C (1837.15 K)\nDiscovery date:1753 by:Geoffroy C.F.\nState = Solid\nElement Group = Post-transition Metals')]
        btn_row = 7
        btn_column = 16
        for b in Bismuth_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2f4d47", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Moscovium_btn = [('Mc', 'Moscovium',
                          'Atomic # = 115\nAtomic mass:289 u\Melting point: N/A\nBoiling point: N/A\nDiscovery date:2003 by:Joint Institute for Nuclear Research\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 16
        for b in Moscovium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        O2Se = [('O', 'Oxygen',
                 'Atomic # = 8\nAtomic mass:15.999 u\nMelting point:-218.79°C (54.36 K)\nBoiling point:-182.96°C (90.19 K)\nDiscovery date:1774 by:Lavoisier A, Scheele C.W, Priestley, J.\nState = Gas\nElement Group = Reactive Nonmetals'),
                ('S', 'Sulfur',
                 'Atomic # = 16\nAtomic mass:32.065 u\nMelting point:112.8°C (385.95 K)\nBoiling point:444.6°C (717.75 K)\nState = Solid\nElement Group = Reactive Nonmetals'),
                ('Se', 'Selenium',
                 'Atomic # = 34\nAtomic mass:78.960 u\nMelting point:220.85°C (494 K)\nBoiling point:684.85°C (958 K)\nDiscovery date:1817 by:Berzelius J.J., Gahn J.G. \nState = Solid\nElement Group = Reactive Nonmetals')]
        btn_row = 3
        btn_column = 17
        for b in O2Se:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2a4165", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Tellurium_btn = [('Te', 'Tellurium',
                          'Atomic # = 52\nAtomic mass:127.60 u\nMelting point:449.51°C (722.66 K)\nBoiling point:987.85°C (1261 K)\nDiscovery date:1782 by:Von Reichenstein FJ.M., Klaproth M.H.\nState = Solid\nElement Group = Metalloids')]
        btn_row = 6
        btn_column = 17
        for b in Tellurium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#523e1b", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Polonium_btn = [('Po', 'Polonium',
                         'Atomic # = 84\nAtomic mass:209 u\nMelting point:253.85°C (527 K)\nBoiling point:962°C (1235.15 K)\nDiscovery date:1898 by:Curie M., Curie P.\nState = Solid\nElement Group = Post-transition Metals')]
        btn_row = 7
        btn_column = 17
        for b in Polonium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2f4d47", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        Livermorium_btn = [('Lv', 'Livermorium',
                            'Atomic # = 116\nAtomic mass:293 u\Melting point: N/A\nBoiling point: N/A\nDiscovery date:2000 by:Joint Institute for Nuclear Research\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 17
        for b in Livermorium_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        F2At = [('F', 'Fluorine',
                 'Atomic # = 9\nAtomic mass:18.998 u\nMelting point:-219.62°C (53.53 K)\nBoiling point:-188.11°C (85.04 K)\nDiscovery date:1886 by:Moissan H. \nState = Gas\nElement Group = Reactive Nonmetals'),
                ('Cl', 'Chlorine',
                 'Atomic # = 17\nAtomic mass:35.453 u\nMelting point:-101.5°C (171.65 K)\nBoiling point:-34.04°C (239.11 K)\nDiscovery date:1774 by:Scheele C.W \nState = Gas\nElement Group = Reactive Nonmetals'),
                ('Br', 'Bromine',
                 'Atomic # = 35\nAtomic mass:79.904 u\nMelting point:-7.2°C (265.95 K)\nBoiling point:58.8°C (331.95 K)\nDiscovery date:1826 by:Balard A.J., Löwig C.J. \nState = Liquid\nElement Group = Reactive Nonmetals'),
                ('I', 'Iodine',
                 'Atomic # = 53\nAtomic mass:126.90 u\nMelting point:113.7°C (386.85 K)\nBoiling point:184.3°C (457.45 K)\nDiscovery date:1811 by:Courtois B. \nState = Solid\nElement Group = Reactive Nonmetals'),
                ('At', 'Astatine',
                 'Atomic # = 85\nAtomic mass:210 u\nMelting point:301.85°C (575 K)\nBoiling point:336.85°C (610 K)\nDiscovery date:1940 by:Segrè E. \nState = Solid\nElement Group = Post-transition Metals')]
        btn_row = 3
        btn_column = 18
        for b in F2At:
            tk.Button(self, text=b[0], width=5, height=2, bg="#2a4165", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Tennessine_btn = [('Ts', 'Tennessine',
                           'Atomic # = 117\nAtomic mass:294 u\nMelting point: N/a\nBoiling point:610°C (883.15 K)\nDiscovery date:2010 by:Oganessian Y., et al.\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 18
        for b in Tennessine_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        self.fillerLine = tk.Label(self, text="", width=5, bg="#3f3f3f")
        self.fillerLine.grid(row=0, column=20)

        He2Rn = [('He', 'Helium',
                  'Atomic # = 2\nAtomic mass:4.0026 u\nMelting point:-272.2°C (0.95 K)\nBoiling point:-268.93°C (4.22 K)\nDiscovery date:1868 by:Pierre J., Per T.C, Ramsay W., et al.\nState = Gas\nElement Group = Noble Gases'),
                 ('Ne', 'Neon',
                  'Atomic # = 10\nAtomic mass:20.180 u\nMelting point:-248.59°C (24.56 K)\nBoiling point:-246.05°C (27.1 K)\nDiscovery date:1898 by:Ramsay W.,Travers M.\nState = Gas\nElement Group = Noble Gases'),
                 ('Ar', 'Argon',
                  'Atomic # = 18\nAtomic mass:39.948 u\nMelting point:-189.35°C (83.8 K)\nBoiling point:-185.85°C (87.3 K)\nDiscovery date:1894 by:Strutt J.W., 3rd Baron Rayleigh, et al.\nState = Gas\nElement Group = Noble Gases'),
                 ('Kr', 'Krypton',
                  'Atomic # = 36\nAtomic mass:83.798 u\nMelting point:-157.36°C (115.79 K)\nBoiling point:-153.41°C (119.74 K)\nDiscovery date:1898 by:Travers M., Ramsay W. \nState = Gas\nElement Group = Noble Gases'),
                 ('Xe', 'Xenon',
                  'Atomic # = 54\nAtomic mass:131.29 u\nMelting point:-111.75°C (161.4 K)\nBoiling point:-108.12°C (165.03 K)\nDiscovery date:1898 by:Ramsay W., Travers M. \nState = Gas\nElement Group = Noble Gases'),
                 ('Rn', 'Radon',
                  'Atomic # = 86\nAtomic mass:222 u\nMelting point:-71°C (202.15 K)\nBoiling point:-61.7°C (211.45 K)\nDiscovery date:1900 by:Dorn F.E. \nState = Gas\nElement Group = Noble Gases')]
        btn_row = 2
        btn_column = 19
        for b in He2Rn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#623842", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        Oganesson_btn = [('Og', 'Oganesson',
                          'Atomic # = 118\nAtomic mass:294 u\nMelting point: N/A\nBoiling point: N/\nDiscovery date:2002 by:Yuri Oganessian\nState = Solid\nElement Group = Unknown Properties')]
        btn_row = 8
        btn_column = 19
        for b in Oganesson_btn:
            tk.Button(self, text=b[0], width=5, height=2, bg="#46474c", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_row += 1
            if btn_row > 8:
                btn_row = 1
                btn_column += 1

        self.fillerLine = tk.Label(self, text="", height=2, bg="#3f3f3f")
        self.fillerLine.grid(row=10, column=0)

        Ce2Lu = [('Ce', 'Cerium',
                  'Atomic # = 58\nAtomic mass:140.12 u\nMelting point:795°C (1068.15 K)\nBoiling point:3257°C (3530.15 K)\nDiscovery date:1803 by: Klaproth M.H., Mosander C.G., et al.\nState = Solid\nElement Group = Lanthanides'),
                 ('Pr', 'Praseodymium',
                  'Atomic # = 59\nAtomic mass:140.91 u\nMelting point:930.85°C (1204 K)\nBoiling point:3520°C (3793.15 K)\nDiscovery date:1885\nState = Solid\nElement Group = Lanthanides'),
                 ('Nd', 'Neodymium',
                  'Atomic # = 60\nAtomic mass:144.24 u\nMelting point:1020.85°C (1294 K)\nBoiling point:3073.85°C (3347 K)\nDiscovery date:1885 by:von Welsbach C.A. \nState = Solid\nElement Group = Lanthanides'),
                 ('Pm', 'Promethium',
                  'Atomic # = 61\nAtomic mass:145 u\nMelting point:1041.85°C (1315 K)\nBoiling point:2999.85°C (3273 K)\nDiscovery date:1945 by:Marinsky J.A., Coryell C.D.,et al. \nState = Solid\nElement Group = Lanthanides'),
                 ('Sm', 'Samarium',
                  'Atomic # = 62\nAtomic mass:150.36 u\nMelting point:1072°C (1345.15 K)\nBoiling point:1793.85°C (2067 K)\nDiscovery date:1879 by:de Boisbaudran PE.L. \nState = Solid\nElement Group = Lanthanides'),
                 ('Eu', 'Europium',
                  'Atomic # = 63\nAtomic mass:151.96 u\nMelting point:826°C (1099.15 K)\nBoiling point:1529°C (1802.15 K)\nDiscovery date:1901 by:Boisbaudran PE.L., Demarçay EA.\nState = Solid\nElement Group = Lanthanides'),
                 ('Gd', 'Gadolinium',
                  'Atomic # = 64\nAtomic mass:157.25 u\nMelting point:1311.85°C (1585 K)\nBoiling point:3271.85°C (3545 K)\nDiscovery date:1880 by:Boisbaudran PE.L.,de Marignac J.C.G.\nState = Solid\nElement Group = Lanthanides'),
                 ('Tb', 'Terbium',
                  'Atomic # = 65\nAtomic mass:158.93 u\nMelting point:1355.85°C (1629 K)\nBoiling point:3230°C (3503.15 K)\nDiscovery date:1843 by:Mosander C.G\nState = Solid\nElement Group = Lanthanides'),
                 ('Dy', 'Dysprosium',
                  'Atomic # = 66\nAtomic mass:162.5 u\nMelting point:1412°C (1685.15 K)\nBoiling point:2566.85°C (2840 K)\nDiscovery date:1886 by:Boisbaudran PE.L.\nState = Solid\nElement Group = Lanthanides'),
                 ('Ho', 'Holmium',
                  'Atomic # = 67\nAtomic mass:164.93 u\nMelting point:1474°C (1747.15 K)\nBoiling point:2694.85°C (2968 K)\nDiscovery date:1878 by:Delafontaine M., Cleve P.T., Soret JL.\nState = Solid\nElement Group = Lanthanides'),
                 ('Er', 'Erbium',
                  'Atomic # = 68\nAtomic mass:167.26 u\nMelting point:1528.85°C (1802 K)\nBoiling point:2868°C (3141.15 K)\nDiscovery date:1843 by:Mosander C.G. \nState = Solid\nElement Group = Lanthanides'),
                 ('Tm', 'Thulium',
                  'Atomic # = 69\nAtomic mass:168.93 u\nMelting point:1544.85°C (1818 K)\nBoiling point:1950°C (2223.15 K)\nDiscovery date:1879 by:Cleve P.T. \nState = Solid\nElement Group = Lanthanides'),
                 ('Yb', 'Ytterbium',
                  'Atomic # = 70\nAtomic mass:173.04 u\nMelting point:819°C (1092.15 K)\nBoiling point:1195.85°C (1469 K)\nDiscovery date:1878 by:de Marignac J.C.G. \nState = Solid\nElement Group = Lanthanides'),
                 ('Lu', 'Lutetium',
                  'Atomic # = 71\nAtomic mass:174.97 u\nMelting point:1662.85°C (1936 K)\nBoiling point:3402°C (3675.15 K)\nDiscovery date:1907 by:James C. , Urbain G.\nState = Solid\nElement Group = Lanthanides')]
        btn_row = 11
        btn_column = 5
        for b in Ce2Lu:
            tk.Button(self, text=b[0], width=5, height=2, bg="#004a77", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_column += 1
            if btn_column > 18:
                btn_column = 1
                btn_row += 1

        Th2Lr = [('Th', 'Thorium',
                  'Atomic # = 90\nAtomic mass:232.04 u\nMelting point:1750°C (2023.15 K)\nBoiling point:4786.85°C (5060 K)\nDiscovery date:1828 by:Berzelius J.J.\nState = Solid\nElement Group = Actinides'),
                 ('Pa', 'Protactinium',
                  'Atomic # = 91\nAtomic mass:231.04 u\nMelting point:1568°C (1841.15 K)\nBoiling point:4000°C (4273.15 K)\nDiscovery date:1913 by:OGöhring O.H., Fajans K.\nState = Solid\nElement Group = Actinides'),
                 ('U', 'Uranium',
                  'Atomic # = 92\nAtomic mass:238.03 u\nMelting point:1132.2°C (1405.35 K)\nBoiling point:4131°C (4404.15 K)\nDiscovery date:1789 by:Klaproth M.H. \nState = Solid\nElement Group = Actinides'),
                 ('Np', 'Neptunium',
                  'Atomic # = 93\nAtomic mass:237.05 u\nMelting point:644°C (917.15 K)\nBoiling point:3901.85°C (4175 K)\nDiscovery date:1940 by:McMillan E., Abelson P. \nState = Solid\nElement Group = Actinides'),
                 ('Pu', 'Plutonium',
                  'Atomic # = 94\nAtomic mass:244 u\nMelting point:639.4°C (912.55 K)\nBoiling point:3231.85°C (3505 K)\nDiscovery date:1940 by:McMillan E., Seaborg G.T., et al.\nState = Solid\nElement Group = Actinides'),
                 ('Am', 'Americium',
                  'Atomic # = 95\nAtomic mass:243 u\nMelting point:1175.85°C (1449 K)\nBoiling point:2606.85°C (2880 K)\nDiscovery date:1944 by:Seaborg G.T., Ghiorso A. , James R.A. \nState = Solid\nElement Group = Actinides'),
                 ('Cm', 'Curium',
                  'Atomic # = 96\nAtomic mass:247 u\nMelting point:1346.85°C (1620 K)\nBoiling point:3109.85°C (3383 K)\nDiscovery date:1944 by:Seaborg G.T., Ghiorso A., James R.A\nState = Solid\nElement Group = Actinides'),
                 ('Bk', 'Berkelium',
                  'Atomic # = 97\nAtomic mass:247 u\nMelting point:984.85°C (1258 K)\nBoiling point:2627°C (2900.15 K)\nDiscovery date:1949 by:Seaborg G.T., Ghiorso A.\nState = Solid\nElement Group = Actinides'),
                 ('Cf', 'Californium',
                  'Atomic # = 98\nAtomic mass:251 u\nMelting point:898.85°C (1172 K)\nBoiling point:1472°C (1745.15 K)\nDiscovery date:1950 by:Seaborg G.T., Ghiorso A.\nState = Solid\nElement Group = Actinides'),
                 ('Es', 'Einsteinium',
                  'Atomic # = 99\nAtomic mass:252 u\nMelting point:860°C (1133.15 K)\nBoiling point: N/A\nDiscovery date:1952 by:Seaborg G.T., Ghiorso A.\nState = Solid\nElement Group = Actinides'),
                 ('Fm', 'Fermium',
                  'Atomic # = 100\nAtomic mass:257 u\nMelting point:1526.85°C (1800 K)\nBoiling point: N/A\nDiscovery date:1953 by:Seaborg G.T., Ghiorso A.\nState = Solid\nElement Group = Actinides'),
                 ('Md', 'Mendelevium',
                  'Atomic # = 101\nAtomic mass:258 u\nMelting point:826.85°C (1100 K)\nBoiling point: N/A\nDiscovery date:1955 by:Seaborg G.T.\nState = Solid\nElement Group = Actinides'),
                 ('No', 'Nobelium',
                  'Atomic # = 102\nAtomic mass:259 u\nMelting point:826.85°C (1100 K)\nBoiling point: N/A\nDiscovery date:1958 by:Seaborg G.T., JINR\nState = Solid\nElement Group = Actinides'),
                 ('Lr', 'Lawrencium',
                  'Atomic # = 103\nAtomic mass:262 u\nMelting point:1627°C (1900.15 K)\nBoiling point: N/A\nDiscovery date:1961 by:Albert G., LBNL\nState = Solid\nElement Group = Actinides')
                 ]
        btn_row = 12
        btn_column = 5
        for b in Th2Lr:
            tk.Button(self, text=b[0], width=5, height=2, bg="#613b28", fg="white",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).grid(row=btn_row,
                                                                                            column=btn_column)
            btn_column += 1
            if btn_column > 18:
                btn_column = 1
                btn_row += 1

        self.fillerLine = tk.Label(self, text="", width=5, bg="#3f3f3f")
        self.fillerLine.grid(row=13, column=0)

        clear = [
            ('Clear', 'Interactive Periodic Table of Elements', 'Click the element you would like information about.')]
        for b in clear:
            tk.Button(self, text=b[0], width=6, height=3, bg="gray", fg="black", justify="center",
                      command=lambda text=b: self.name(text[1]) or self.info(text[2])).place(x=50, y=360)
            btn_row += 1
            if btn_row > 7:
                btn_row = 1
                btn_column += 1

        self.infoLine = tk.Label(self, text="Click the element you would like information about.", justify='left',
                                 font=("Sans serif", 9, "bold"), bg="gray", fg="white")
        self.infoLine.grid(row=1, column=4, columnspan=12, rowspan=4)

        def click():
            global be_img
            top = Toplevel()
            top.configure(background="#3f3f3f")
            top.title("About")
            top.geometry("950x500")
            top.iconbitmap('icons\myIcon.ico')
            top.resizable(False, False)
            TableInfo_lbl = Label(top, text="About", font=("Sans serif", 18, "bold"), bg="#3f3f3f", fg="White", padx=30).pack()
            Info_lbl = Label(top, text="\nThe periodic table of chemical elements, often called the periodic table, organizes all discoveredchemical elements.\n\nSo we created an Interactive Periodic Table or IPT where a user can interact with the application by clicking each tile\n\nor button and displaying each chemical element information or details found in each element.The Interactive Periodic\n\nTable is useful for modern students and scientists because it helps predict the types of chemical reactions that a\n\nparticular element is likely to participate in. And other feature isa lso added to create more\n\nfunction for the user benefit.", font=("Sans serif", 13, "bold"), borderwidth=20, bg="#3f3f3f", fg="white").pack()
            Names = Label(top, text="Member: \nDavid, Jerson Noehl D. \nGaite,Jhon Edward A. \nHortal, Gian Carlo I. \nPilapil, Brian Kenneth M. \nQuiroz, Charles Wayne M.", font=("Sans serif", 13, "bold"), fg="white", bg="#3f3f3f").place(x=0, y=320)
            exit_btn = Button(top, text="close", command=top.destroy,fg="white",bg="#3f3f3f", width=30).place(relx=0.39, rely=0.95)

        # About btn
        abt_btn = Button(self, text="About ", width=5, height=2, bg="gray", fg="black", command=click)
        abt_btn.place(x=865, y=385)

        def search_window():
            def search():
                global myresult
                Esymbol = e1.get()
                Ename = e2.get()
                atomicNums = e3.get()
                atomicMass = e4.get()
                Egroup = e5.get()

                mysqldb = mysql.connector.connect(host="localhost", user="root", password="Ilovemusic11",
                                                  database="p_element")
                mycursor = mysqldb.cursor()

                try:
                    mycursor.execute("SELECT * FROM elements where Esymbol = '" + Esymbol + "'")
                    myresult = mycursor.fetchall()

                    for x in myresult:
                        print(x)
                    e2.delete(0, END)
                    e2.insert(END, x[1])

                    e3.delete(0, END)
                    e3.insert(END, x[2])

                    e4.delete(0, END)
                    e4.insert(END, x[3])

                    e5.delete(0, END)
                    e5.insert(END, x[4])

                except Exception as e:
                    showerror("Error", "Element does not Exist!!!")
                    mysqldb.rollback()
                    mysqldb.close()

            root = Tk()
            root.title("Search Element")
            root.geometry("300x250")
            root.iconbitmap('icons\myIcon.ico')
            root.configure(bg='#3f3f3f')

            Label(root, text="Element Symbol").place(x=10, y=10)
            Button(root, text="Search", command=search, bg='white', fg='#3f3f3f', height=1, width=13).place(x=153, y=40)
            Label(root, text="Element Name").place(x=10, y=80)
            Label(root, text="Atomic Number").place(x=10, y=120)
            Label(root, text="Atomic Mass").place(x=10, y=160)
            Label(root, text="Group").place(x=10, y=200)

            e1 = Entry(root)
            e1.place(x=140, y=10)

            e2 = Entry(root)
            e2.place(x=140, y=80)

            e3 = Entry(root)
            e3.place(x=140, y=120)

            e4 = Entry(root)
            e4.place(x=140, y=160)

            e5 = Entry(root)
            e5.place(x=140, y=200)

            root.mainloop()

        # Search btn
        srch_btn = Button(self, text="Search ", width=6, height=3, bg="gray", fg="black", command=search_window)
        srch_btn.place(x=110, y=360)

    # Replaces Label at the top with the name of whichever element tk.Button was pressed
    def name(self, text):
        self.topLabel.config(text=text, background="#3f3f3f")

    # Displays information on the element of whichever element tk.Button was pressed
    def info(self, text):
        self.infoLine.config(text=text)