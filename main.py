#!/usr/bin/env python

import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ, cal_k_constante, cal_k_circ
import numpy as np

def plot_ejercicio1(longitudes, pesos):

    L3 = np.array(longitudes)**3

    plt.scatter(L3, pesos, color="turquoise")

    plt.xlabel("Longitud l [cm]")
    plt.ylabel("Peso W [kg]")
    plt.title("Relación entre W y L^3")

    plt.grid(True)

    plt.savefig("media/grafica1.png")
    plt.show()
    plt.close()

def make_plot(longitudes, pesos, K):

    plt.scatter(longitudes, pesos, color="navy", label="Datos reales")

    l_espacio = np.linspace(min(longitudes), max(longitudes), 100)

    plt.plot(l_espacio, K*(l_espacio**3),
             color="mediumpurple",
             label="Modelo W = KL^3")

    plt.xlabel("Longitud l [cm]")
    plt.ylabel("Peso W [kg]")
    plt.title("Modelo de similitud geométrica")
    plt.legend()
    plt.grid(True)

    plt.savefig("media/grafica_modeloe1.png")
    plt.show()
    plt.close()
    
def make_plot_circ(longitudes, circunferencias, pesos, K):
    """Gráfica del modelo W = K L C^2 usando C promedio."""

    plt.scatter(longitudes, pesos,
                color="darkmagenta",
                label="Datos reales")

    l_espacio = np.linspace(min(longitudes), max(longitudes), 100)
    C_prom = np.mean(circunferencias)

    plt.plot(l_espacio,
             K * l_espacio * (C_prom ** 2),
             color="cornflowerblue",
             label="Modelo W = K L C^2")

    plt.xlabel("Longitud l [cm]")
    plt.ylabel("Peso W [kg]")
    plt.title("Modelo con Circunferencia")
    plt.legend()
    plt.grid(True)

    plt.savefig("media/grafica_modelo2.png")
    plt.show()
    plt.close()

def main():

    longitudes = [36.81, 31.77, 43.82, 36.82, 32.07, 45.07, 35.89]
    pesos = [0.78, 0.47, 1.16, 0.74, 0.44, 1.40, 0.64]
    circunferencias = [24.77, 21.29, 27.94, 24.77, 21.59, 31.75, 22.86]

    plot_ejercicio1(longitudes, pesos) 

    K = cal_k_constante(longitudes, pesos)
    make_plot(longitudes, pesos, K)
    pred = modelo_geom(longitudes, K)
    error = calc_error(pred, pesos)

    print("Modelo W = K L^3")
    print("Constante K:", K)
    print("Error del modelo:", error)

    K_circ = cal_k_circ(longitudes, circunferencias, pesos)
    pred_circ = modelo_circ(longitudes, circunferencias, K_circ)
    error_circ = calc_error(pred_circ, pesos)

    make_plot_circ(longitudes, circunferencias, pesos, K_circ)

    print("\nModelo W = K L C^2")
    print("Constante K:", K_circ)
    print("Error del modelo:", error_circ)

if __name__ == "__main__":
    main()
