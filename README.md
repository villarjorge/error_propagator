# error_propagator
Propagador de errores con python. Este projecto utiliza sympy para crear automáticamente las fórmulas de propagación de error de una ecuación dada. Genera imágenes de las fórmulas en la carpeta "imagenes" y permite copiar el código LaTex que representan las fórmulas. Además, permite calcular el error numérico utilizando las fórmulas de error.

## Ejemplo

Para la fórmula $x^z + y$ las variables $x, y$ tienen error. Podemos introducirlas así en el programa:

[!image](https://github.com/villarjorge/error_propagator/blob/main/primera%20ventana.png)

Lo que nos lleva a:

[!image](https://github.com/villarjorge/error_propagator/blob/main/segunda%20ventana.png)

Y las fórmulas que podemos copiar son: $\sqrt{{\Delta}y^{2} + \frac{x^{2 z} z^{2} {\Delta}x^{2}}{x^{2}}}$ y $\left|{{\Delta}y}\right| + \left|{\frac{x^{z} z {\Delta}x}{x}}\right|$
