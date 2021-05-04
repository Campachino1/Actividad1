import PySimpleGUI as sg      
import json
import csv

archivo1 = open("carbon-footprint-travel-mode.csv", "r")
footprint = csv.reader(archivo1, delimiter=',')
archivo2 = open("mismanaged-plastic-waste-by-region-2010.csv","r")
plasticwaste = csv.reader(archivo2, delimiter=',')



def procesar_csv (data):
    colum = next(data)
    datos_procesados = []
    for d in data:
        zip_iterator = zip(colum,d)
        dic = dict(zip_iterator)
        datos_procesados.append(dic)
    return datos_procesados

def guardar_JSON (data,ruta):
    archivo = open(ruta,"w")
    json.dump(data,archivo)
    archivo.close()

def popup_ruta ():
    None
button_footprint = sg.Button('Huella de Carbono de Transportes',k='footprint_button')
button_deaths_from_energy_production = sg.Button('Desechos Plasticos',k='plastic_button')
font_titulo = ["Sans-serif",30]
titulo = sg.Text("Datos para analizar!",font=font_titulo)
button_exit = sg.Button("Salir",k='exit')

layout = [[titulo],[button_footprint],[button_deaths_from_energy_production],[button_exit]]
columna1 = [[sg.Column(layout,element_justification='center',pad=(50,50))]]
window = sg.Window('Actividad 1 -Rossi- ',columna1,size=(500,300),element_justification='c',disable_close=True)


while True:
    event, values = window.read()
    if event in ("exit"):
        break
    elif event in ("footprint_button"): 
        text=sg.popup_get_text('Ingrese Nombre del Archivo CSV',title='Name')
        if text:
            guardar_JSON(procesar_csv(footprint),(text+".json"))
            sg.popup_ok("Procesado exitoso")      
    elif event in ("plastic_button"):
        text=sg.popup_get_text('Ingrese Nombre del Archivo CSV',title='Name')
        if text:
            guardar_JSON(procesar_csv(plasticwaste),(text+".json"))
            sg.popup_ok("Procesado exitoso")
window.close()

    
        
