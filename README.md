# Propagador de errores
Propagador de errores con interfaz realizado con python (principalmente las bibliotecas Tkinter, sympy y matplotlib). Este projecto requiere la biblioteca Sympy, que se utiliza para crear automáticamente las fórmulas de propagación de error de una ecuación dada. Genera imágenes de las fórmulas en la carpeta "imagenes" y permite copiar el código LaTex que representan las fórmulas. Además, permite calcular el error numérico utilizando las fórmulas de error.

## Ejemplo

Para la fórmula $x^z + y$ las variables $x, y$ tienen error. Podemos introducirlas así en el programa:

![image](https://github.com/villarjorge/error_propagator/blob/main/primera%20ventana.png)

Lo que nos lleva a:

![!image](https://github.com/villarjorge/error_propagator/blob/main/segunda%20ventana.png)

Las fórmulas que podemos copiar son: $\sqrt{{\Delta}y^{2} + \frac{x^{2 z} z^{2} {\Delta}x^{2}}{x^{2}}}$ y $\left|{{\Delta}y}\right| + \left|{\frac{x^{z} z {\Delta}x}{x}}\right|$

Una vez introducidos valores numéricos podemos calcular los errores numéricos. 

## Tips de uso e instalación

Necesitas tener Python instalado en tu ordenador, así como la librería sympy. Para instalar sympy puedes probar el comando "pip install sympy" en una terminal. Si utilizas Anaconda, probablemente te vendrá sympy por defecto. 

Puedes descargar este repositorio como zip pulsando el botón verde de arriba en el que pone "Code". Si le pulsas a "Download Zip" comienza la descarga. Puedes extraer los archivos a su propia carpeta. Una vez hayas hecho esto, puedes hacer doble click sobre el archivo "Propagador_errores.bat" para iniciar el programa. 
