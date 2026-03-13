#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ, cal_k_constante
import numpy as np

def plot_ejercicio1(longitudes, pesos):

    L3 = np.array(longitudes)**3

    plt.scatter(L3, pesos, color="turquoise")

    plt.xlabel("L^3")
    plt.ylabel("Peso (kg)")
    plt.title("Relación entre W y L^3")

    plt.grid(True)

    plt.savefig("grafica1.png")
    plt.show()
    plt.close()

def make_plot(longitudes, pesos, K):

    plt.scatter(longitudes, pesos, color="navy", label="Datos reales")

    l_espacio = np.linspace(min(longitudes), max(longitudes), 100)

    plt.plot(l_espacio, K*(l_espacio**3),
             color="mediumpurple",
             label="Modelo W = KL^3")

    plt.xlabel("Longitud (cm)")
    plt.ylabel("Peso (kg)")
    plt.title("Modelo de similitud geométrica")
    plt.legend()
    plt.grid(True)

    plt.savefig("grafica_modelo1.png")
    plt.show()
    plt.close()

def main():

    longitudes = [36.81, 31.77, 43.82, 36.82, 32.07, 45.07, 35.89]
    pesos = [0.78, 0.47, 1.16, 0.74, 0.44, 1.40, 0.64]

    plot_ejercicio1(longitudes, pesos) 
    K = cal_k_constante(longitudes, pesos)
    make_plot(longitudes, pesos, K)
    pred = modelo_geom(longitudes, K)
    error = calc_error(pred, pesos)

    print("Constante K:", K)
    print("Error del modelo:", error)
    """
    (Si no modificas esta cadena de texto lloro)
    Aquí va el código, recuerda reutilizar el 
    código que ya escribiste en otros archivos
    """

if __name__ == "__main__":
    main()
