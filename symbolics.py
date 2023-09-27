"""
En este archivo se encuentran las funciones encargadas de las operaciones con simbolos necesáreas para
obtener las fórmulas de errores, así como parsear esas formulas a latex
"""
import sympy as smp

def tomar_input():
    #print("Introduce el simbolo de la variable de la que quieres calcular el error: ")
    #variable_target_simbolica = smp.symbols(input())

    print("Introduce los simbolos de las variables que tengan error con las que quieres trabajar (Separadas por comas): ")
    variables_con_error = input().split(",")
    variables_con_error_simbolicas = smp.symbols(variables_con_error)

    errores = [r"{\Delta}"+f"{v}" for v in variables_con_error]
    errores_simbolicos = smp.symbols(errores)

    print("Introduce los simbolos de las restantes variables: ")
    variables_sin_error = input().split(",")
    variables_sin_error_simbolicas = smp.symbols(variables_sin_error)

    print("Introduce el lado derecho de la ecuación en cuestión: ")
    ecuacion = input()
    ecuacion_simbolica = smp.sympify(ecuacion)

    #return variable_target_simbolica, variables_con_error_simbolicas, errores_simbolicos, variables_sin_error_simbolicas, ecuacion_simbolica
    return variables_con_error_simbolicas, errores_simbolicos, variables_sin_error_simbolicas, ecuacion_simbolica

def procesar_input(variables_con_error, variables_sin_error, ecuacion):
    variables_con_error = variables_con_error.split(",")
    variables_sin_error = variables_sin_error.split(",")

    variables_con_error_simbolicas = smp.symbols(variables_con_error)# Por algun motivo si estas variables tienen real=True, se rompe

    errores = [r"{\Delta}"+f"{v}" for v in variables_con_error]
    errores_simbolicos = smp.symbols(errores, real=True)

    variables_sin_error_simbolicas = smp.symbols(variables_sin_error, real=True)

    ecuacion_simbolica = smp.sympify(ecuacion)
    return ecuacion_simbolica, variables_con_error_simbolicas, errores_simbolicos, variables_sin_error_simbolicas

def diferenciar(ecuacion_simbolica, variables_con_error_simbolicas, errores_simbolicos):
    #print(ecuacion_simbolica, variables_con_error_simbolicas, errores_simbolicos)
    propagacion_error_gauss_simbolico = smp.sympify(0)

    for variable, error in zip(variables_con_error_simbolicas, errores_simbolicos):
        propagacion_error_gauss_simbolico += (smp.diff(ecuacion_simbolica, variable)*error)**2 #(ecuacion_simbolica.diff(variable)*error)**2

    propagacion_error_gauss_simbolico = smp.sqrt(propagacion_error_gauss_simbolico)
    propagacion_error_gauss_simbolico.simplify()

    propagacion_error_sobreest_simbolico = smp.sympify(0)

    for variable, error in zip(variables_con_error_simbolicas, errores_simbolicos):
        propagacion_error_sobreest_simbolico += smp.Abs(ecuacion_simbolica.diff(variable)*error)

    propagacion_error_sobreest_simbolico.simplify()
    return propagacion_error_gauss_simbolico, propagacion_error_sobreest_simbolico

def formula_a_latex(formula) -> str:
    return smp.latex(formula)

def formula_a_lambda(variables, formula):
    return smp.lambdify(variables, formula)

def paso_simbolico(variables_con_error, variables_sin_error, ecuacion):
    # Engloba todos los pasos simbolicos. 
    # Devuelve las strings de latex de las fórmulas de errores, las lambdas de las fórmulas de errores y las strings de variables de las fórmulas de errores 
    ecuacion_y_variables_simbolicas = procesar_input(variables_con_error, variables_sin_error, ecuacion)
    formulas_de_errores = diferenciar(*ecuacion_y_variables_simbolicas[:3]) # :3 & >:3

    variables_flattened = [i for l in ecuacion_y_variables_simbolicas[1:] for i in l]
    
    return [smp.latex(f) for f in formulas_de_errores], [smp.lambdify(variables_flattened, f) for f in formulas_de_errores], [str(v).replace(r"{\Delta}", "Δ") for v in variables_flattened] # smp.python(v)