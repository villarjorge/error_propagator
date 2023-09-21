"""
Creacion de las ventanas. Ventana de input lleva a una ventana de resultado y calculo numérico
"""

import tkinter as tk
from symbolics import paso_simbolico
from crear_imagenes import formula_a_imagen

def crear_ventana_input():
    # Parte donde inicializamos todo
    ventana_input = tk.Tk() 
    ventana_input.title("Ventana de introducción para el propagador de errores")

    marco_inputs = tk.LabelFrame(ventana_input, text="Introducción de las variables y las fórmulas", padx=10, pady=10)

    etiqueta_variables_con_error = tk.Label(marco_inputs, text="Introduce los simbolos de las variables que tengan error con las que quieres trabajar (Separadas por comas):")
    etiqueta_variables_sin_error = tk.Label(marco_inputs, text="Introduce los simbolos de las restantes variables:")
    etiqueta_formula = tk.Label(marco_inputs, text="Introduce el lado derecho de la ecuación en cuestión:")

    entrada_variables_con_error = tk.Entry(marco_inputs, width=35, borderwidth=5)
    entrada_variables_sin_error = tk.Entry(marco_inputs, width=35, borderwidth=5)
    entrada_formula = tk.Entry(marco_inputs, width=35, borderwidth=5)

    marco_botones = tk.LabelFrame(ventana_input)

    boton_ayuda = tk.Button(marco_botones, text="Ayuda", command=crear_ventana_ayuda)
    boton_calcular = tk.Button(
        marco_botones, 
        text="Calcular", 
        command=lambda: crear_ventana_calculo(
            entrada_variables_con_error.get(), entrada_variables_sin_error.get(), entrada_formula.get()
        )
    )
    # Parte donde colocamos todo
    marco_inputs.pack()

    etiqueta_variables_con_error.grid(row=0, column=0)
    entrada_variables_con_error.grid(row=0, column=1)

    etiqueta_variables_sin_error.grid(row=1, column=0)
    entrada_variables_sin_error.grid(row=1, column=1)

    etiqueta_formula.grid(row=2, column=0)
    entrada_formula.grid(row=2, column=1)

    marco_botones.pack()

    boton_ayuda.grid(row=0, column=0)
    boton_calcular.grid(row=0, column=1)

    ventana_input.mainloop()

def get_error(f, entries) -> str():
    values = [float(e.get()) for e in entries]
    return str(f(*values))

def crear_ventana_ayuda():
    ventana_ayuda = tk.Toplevel()
    ventana_ayuda.title("Ayuda")

    texto = """
    Utiliza 'E' para el número e, ^ para exponentes, expresa explicitamente que quieres multiplicar con '*', 
    utiliza sin(x) en vez de sen(x) y utiliza paréntesis si utilizas funciones como seno y coseno.

    Aplicación realizada por Jorge San José Villar en Septiembre del 2023
    """

    etiqueta_mensaje_de_ayuda = tk.Label(ventana_ayuda, text=texto)

    etiqueta_mensaje_de_ayuda.pack()

    ventana_ayuda.focus()
    ventana_ayuda.mainloop()

def crear_ventana_calculo(variables_con_error:str, variables_sin_error:str, formula:str):
    # En el futuro estaría bien añadir la fórmula como imagen embevida en esta ventana
    strings_latex, lambdas, variables = paso_simbolico(variables_con_error, variables_sin_error, formula)

    ventana_calculo = tk.Toplevel()
    ventana_calculo.title("Fórmula de error y cálculos")

    formula_a_imagen(strings_latex[0], "gauss")
    formula_a_imagen(strings_latex[1], "sobreest")

    tk.Label(ventana_calculo, text="Fórmulas generadas correctamente como imagénes en 'imágenes'").pack()

    marco_botones_copiar = tk.LabelFrame(ventana_calculo, text="Pulsa para copiar codigos latex")
    
    # https://stackoverflow.com/questions/579687/how-do-i-copy-a-string-to-the-clipboard
    boton_copiar_gauss = tk.Button(
        marco_botones_copiar, 
        text="Error gaussiano", 
        command=lambda: (ventana_calculo.clipboard_clear(), ventana_calculo.clipboard_append(strings_latex[0]))
    )
    boton_copiar_sobreest = tk.Button(
        marco_botones_copiar,
        text="Sobreestimación del error",
        command=lambda: (ventana_calculo.clipboard_clear(), ventana_calculo.clipboard_append(strings_latex[1]))
    )

    # parte donde colocamos todo
    marco_botones_copiar.pack()
    boton_copiar_gauss.grid(row=0, column=0)
    boton_copiar_sobreest.grid(row=0, column=1)

    # Parte programatica
    marco_entradas_variables = tk.LabelFrame(ventana_calculo, text="Obtener error numérico")

    entries = list()

    for index, v in enumerate(variables):
        m = tk.LabelFrame(marco_entradas_variables)

        tk.Label(m, text=f"{v}:").grid(row=0, column=0)

        e = tk.Entry(m)
        entries.append(e)
        e.grid(row=0, column=1)

        m.grid(row=index//3, column=index%3)
        
    marco_entradas_variables.pack()

    marco_calculo = tk.LabelFrame(ventana_calculo)

    label_error_gauss = tk.Label(marco_calculo, text="El error gausiano es: ")
    boton_calcular_gauss = tk.Button(
        marco_calculo, 
        text="Calcular error gaussiano", 
        command=lambda: label_error_gauss.config(text="El error gausiano es: " + get_error(lambdas[0], entries))
    )

    boton_calcular_gauss.grid(row=0, column=0)
    label_error_gauss.grid(row=0, column=1)


    label_error_sobreest = tk.Label(marco_calculo, text="La sobreestimación del error es: ")
    boton_calcular_sobreest = tk.Button(
        marco_calculo, 
        text="Calcular error sobreestimado", 
        command=lambda: label_error_sobreest.config(text="La sobreestimación del error es: " + get_error(lambdas[1], entries))
    )

    boton_calcular_sobreest.grid(row=1, column=0)
    label_error_sobreest.grid(row=1, column=1)

    marco_calculo.pack()

    ventana_calculo.focus()
    ventana_calculo.mainloop()

if __name__ == "__main__":
    crear_ventana_input()