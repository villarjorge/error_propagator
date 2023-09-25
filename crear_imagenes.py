"""
Creación de las imagenes
"""
import matplotlib.pyplot as plt

def formula_a_imagen(given_string: str, name="temp"):
    given_string = "$" + given_string + "$"

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])

    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height

    plt.text(0.5*(left+right), 0.5*(bottom+top), given_string,
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=20, color='red',
                    transform=ax.transAxes)
    ax.set_axis_off()
    plt.savefig("imagenes/" + name + ".jpg")
    plt.close()