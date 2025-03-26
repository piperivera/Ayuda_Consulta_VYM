import tkinter as tk
from tkinter import messagebox


def generar_consulta():
   
    valores = entrada_texto.get("1.0", tk.END).strip().split("\n")
    

    lista_resultados.delete(0, tk.END)
    
   
    consulta = " OR ".join([f'name LIKE "%{valor.strip()}%"' for valor in valores if valor.strip()])
    
   
    if consulta:
        lista_resultados.insert(tk.END, consulta)
    else:
        lista_resultados.insert(tk.END, "No se ingresaron valores válidos.")


ventana = tk.Tk()
ventana.title("Generador ")
ventana.geometry("600x500")


etiqueta = tk.Label(ventana, text="Ingresa uno por línea:")
etiqueta.pack(pady=10)


entrada_texto = tk.Text(ventana, height=10, width=40)
entrada_texto.pack(pady=10)


boton_generar = tk.Button(ventana, text="Generar Consulta", command=generar_consulta)
boton_generar.pack(pady=10)

lista_resultados = tk.Listbox(ventana, width=50)
lista_resultados.pack(pady=10)


ventana.mainloop()
