import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (f)Poste Quebracho Fino de 2.2 mts
    (v)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        largo_del_terreno = self.txt_largo.get()
        ancho_del_terreno = self.txt_ancho.get()
        
        largo_del_terreno = float(largo_del_terreno)
        ancho_del_terreno = float(ancho_del_terreno)
        
        metros_cuadrados = ancho_del_terreno * largo_del_terreno
        perimetro = (ancho_del_terreno + largo_del_terreno) * 2
        
        cantidad_esquinas = 4
        cantidad_postes_gruesos = perimetro // 250 + cantidad_esquinas
        cantidad_postes_finos = perimetro // 12
        cantidad_varillas = perimetro // 2
        cantidad_alambre = perimetro * 7
        
        alert("mensaje", f"la cantidad de metros cuadrados es: {metros_cuadrados:.0f}\nla cantidad de postes gruesos es: {cantidad_postes_gruesos:.0f}\n la cantidad de postes finos es: {cantidad_postes_finos:.0f}\n la cantidad de varillas es: {cantidad_varillas:.0f}\n la cantidad de alambre es: {cantidad_alambre:.0f}")
        
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()