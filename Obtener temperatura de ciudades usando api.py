import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import matplotlib.pyplot as plt
import requests
import json

#funcion para validar casillas marcadas

def funcion_click():

    #listas que se usarán para graficar
    ciudades =[]
    temperaturas = []

    valor = 0 
    if (opcion_1.get()):
        api_key ="8d5e9b515d8bd6a5764c80662fe02848"
        ciudad_key ="3522507"
        url ="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (ciudad_key, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temperatura_Oaxaca = data["main"]["temp"]
        print("\nTemperatura actual de oaxaca:" , temperatura_Oaxaca)
        ciudades.append("Oaxaca")
        temperaturas.append(temperatura_Oaxaca)
        valor+=1
        
    if (opcion_2.get()):
       
        api_key ="8d5e9b515d8bd6a5764c80662fe02848"
        ciudad_key ="3531013"
        url ="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (ciudad_key, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temperatura_chiapas = data["main"]["temp"]
        print("\nTemperatura actual de chiapas de corzo:" , temperatura_chiapas)
        ciudades.append("Chiapa de Corzo")
        temperaturas.append(temperatura_chiapas)
        valor+=1

    if (opcion_3.get()):
        api_key ="8d5e9b515d8bd6a5764c80662fe02848"
        ciudad_key ="3815415"
        url ="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (ciudad_key, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temperatura_tlaxcala = data["main"]["temp"]
        print("\nTemperatura actual de tlaxcala:" , temperatura_tlaxcala)
        ciudades.append("Tlaxcala")
        temperaturas.append(temperatura_tlaxcala)
        valor+=1

        
    if (opcion_4.get()):
        api_key ="8d5e9b515d8bd6a5764c80662fe02848"
        ciudad_key ="3522551"
        url ="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (ciudad_key, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temperatura_laredo = data["main"]["temp"]
        print("\nTemperatura actual de nuevo laredo:" , temperatura_laredo)
        ciudades.append("Nuevo Laredo")
        temperaturas.append(temperatura_laredo)
        valor+=1
        
    if (opcion_5.get()):
        api_key ="8d5e9b515d8bd6a5764c80662fe02848"
        ciudad_key ="3516396"
        url ="http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (ciudad_key, api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        temperatura_tamasopo = data["main"]["temp"]
        print("\nTemperatura actual de tamasopo :" , temperatura_tamasopo)
        ciudades.append("Tamasopo")
        temperaturas.append(temperatura_tamasopo)
        valor+=1
        
    if (valor<2):
        print(valor)
        messagebox.showwarning(title="¡ADVERTENCIA!", message="Tiene que seleccionar por lo mínimo dos ciudades.")
    else:
        #GRAFICAR si se seleccionan dos o más
        plt.figure(figsize=(7,5))
        plt.title('Temperaturas de las ciudades seleccionadas',size=16,pad=25)

        plt.bar(ciudades,temperaturas, color=['r','b','g','c','m','y','k'])
        plt.ylabel("Temperatura actual", size=14)
        plt.xlabel("Ciudad", size=14)
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)

        plt.grid(False)
        plt.show()

    
    print(temperaturas)
    print(ciudades)


        
#diseño de ventana
ventana = tk.Tk()
ventana.title("ELIGE ")
ventana.geometry('500x500')

#label
etiqueta = ttk.Label(ventana, text= "Elige dos ciudades", font ="Helvetica 15")
etiqueta.pack()

#checkbutton
opcion_1 = tk.IntVar()
casilla_1 = tk.Checkbutton(ventana, text="OAXACA", variable=opcion_1)
casilla_1.deselect()
casilla_1.pack()
#checkbutton
opcion_2 = tk.IntVar()
casilla_2 = tk.Checkbutton(ventana, text="CHIAPAS DE CORZO", variable=opcion_2)
casilla_2.deselect()
casilla_2.pack()
#checkbutton
opcion_3 = tk.IntVar()
casilla_3 = tk.Checkbutton(ventana, text="TLAXCALA", variable=opcion_3)
casilla_3.deselect()
casilla_3.pack()
#checkbutton
opcion_4 = tk.IntVar()
casilla_4 = tk.Checkbutton(ventana, text="NUEVO LAREDO", variable=opcion_4)
casilla_4.deselect()
casilla_4.pack()
#checkbutton
opcion_5 = tk.IntVar()
casilla_5 = tk.Checkbutton(ventana, text="TAMASOPO", variable=opcion_5 )
casilla_5.deselect()
casilla_5.pack()

# boton
btn = ttk.Button(ventana, text="BUSCAR CLIMA", command=funcion_click)
btn.pack()

#activar ventana
ventana.mainloop()


