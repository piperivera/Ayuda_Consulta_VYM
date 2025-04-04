import tkinter as tk
from tkinter import ttk

# Función para copiar el contenido del Listbox al portapapeles
def copiar_listbox(listbox):
    valores = listbox.get(0, tk.END)
    texto = "\n".join(valores)
    ventana.clipboard_clear()
    ventana.clipboard_append(texto)
    ventana.update()  # Actualiza para que quede en el clipboard incluso si se cierra

# ----------- FUNCIONES DE CADA TAB -----------

def generar_consulta():
    valores = entrada_like.get("1.0", tk.END).strip().split("\n")
    lista_resultados_like.delete(0, tk.END)
    consulta = " OR ".join([f'name LIKE "%{valor.strip()}%"' for valor in valores if valor.strip()])
    if consulta:
        lista_resultados_like.insert(tk.END, consulta)
    else:
        lista_resultados_like.insert(tk.END, "No se ingresaron valores válidos.")

def limpiar_fechas():
    valores = entrada_fechas.get("1.0", tk.END).strip().split("\n")
    lista_resultados_fechas.delete(0, tk.END)
    for valor in valores:
        fecha = valor.strip().split(" ")[0]
        if fecha:
            lista_resultados_fechas.insert(tk.END, fecha)

def limpiar_nombres():
    valores = entrada_nombres.get("1.0", tk.END).strip().split("\n")
    lista_resultados_nombres.delete(0, tk.END)
    for valor in valores:
        nombre = valor.strip().split(".")[0]
        if nombre:
            lista_resultados_nombres.insert(tk.END, nombre)

# ----------- VENTANA PRINCIPAL -----------
ventana = tk.Tk()
ventana.title("Herramientas de Texto")
ventana.geometry("600x500")

# ----------- TABS -----------
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True)

# ----------- TAB 1: LIKE -----------
tab_like = ttk.Frame(notebook)
notebook.add(tab_like, text="Consulta LIKE")

etiqueta_like = tk.Label(tab_like, text="Ingresa uno por línea:")
etiqueta_like.pack(pady=10)

entrada_like = tk.Text(tab_like, height=10, width=40)
entrada_like.pack(pady=10)

boton_like = tk.Button(tab_like, text="Generar Consulta", command=generar_consulta)
boton_like.pack(pady=5)

lista_resultados_like = tk.Listbox(tab_like, width=50)
lista_resultados_like.pack(pady=5)

boton_copiar_like = tk.Button(tab_like, text="Copiar Todo", command=lambda: copiar_listbox(lista_resultados_like))
boton_copiar_like.pack(pady=5)

# ----------- TAB 2: Fechas -----------
tab_fechas = ttk.Frame(notebook)
notebook.add(tab_fechas, text="Fechas")

etiqueta_fechas = tk.Label(tab_fechas, text="Ingresa fechas con hora:")
etiqueta_fechas.pack(pady=10)

entrada_fechas = tk.Text(tab_fechas, height=10, width=40)
entrada_fechas.pack(pady=10)

boton_fechas = tk.Button(tab_fechas, text="Limpiar Fechas", command=limpiar_fechas)
boton_fechas.pack(pady=5)

lista_resultados_fechas = tk.Listbox(tab_fechas, width=50)
lista_resultados_fechas.pack(pady=5)

boton_copiar_fechas = tk.Button(tab_fechas, text="Copiar Todo", command=lambda: copiar_listbox(lista_resultados_fechas))
boton_copiar_fechas.pack(pady=5)

# ----------- TAB 3: Nombres -----------
tab_nombres = ttk.Frame(notebook)
notebook.add(tab_nombres, text="Nombres")

etiqueta_nombres = tk.Label(tab_nombres, text="Ingresa nombres con dominio:")
etiqueta_nombres.pack(pady=10)

entrada_nombres = tk.Text(tab_nombres, height=10, width=40)
entrada_nombres.pack(pady=10)

boton_nombres = tk.Button(tab_nombres, text="Limpiar Nombres", command=limpiar_nombres)
boton_nombres.pack(pady=5)

lista_resultados_nombres = tk.Listbox(tab_nombres, width=50)
lista_resultados_nombres.pack(pady=5)

boton_copiar_nombres = tk.Button(tab_nombres, text="Copiar Todo", command=lambda: copiar_listbox(lista_resultados_nombres))
boton_copiar_nombres.pack(pady=5)

# ----------- EJECUTAR VENTANA -----------
ventana.mainloop()
