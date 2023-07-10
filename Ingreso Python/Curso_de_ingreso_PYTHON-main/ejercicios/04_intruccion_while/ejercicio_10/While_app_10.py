import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

        # numero_ingresado
        # suma_negativos = 0
        # suma_positivos = 0
        # cantidad_positivos = 0
        # cantidad_negativos = 0
        # cantidad_ceros = 0
        
        # def confirm(mensaje):
        #     respuesta = input(mensaje + " (s/n): ")
        #     return respuesta.lower() == "s"

        # continuar = True
        # while continuar:
        #     numero_ingresado = prompt(numero_ingresado)
        #     numero_ingresado = int(numero_ingresado)
            
        #     es_negativo = numero_ingresado < 0
        #     es_positivo = numero_ingresado > 0
            
        #     if es_negativo:
        #         suma_negativos += numero_ingresado
        #         cantidad_negativos += 1
        #         continuar = confirm("¿Deseas continuar?")