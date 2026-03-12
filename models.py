#!/usr/bin/env python
"""
models.py

(Por favor modifica o elimina este comentario) 
Es recomendable que escribas unas cuantas líneas
explicando el propósito de cada código. Te propongo
que utilices este archivo para que escribas las
funciones principales que vayas a reutilizar en
tus otras prácticas
"""
import numpy as np
import matplotlib.pyplot as plt

def cal_k_constante(longitudes, pesos):
    k_valores = pesos / (longitudes**3)
    return np.mean(k_valores)

def relacion_lineal_modpearson(x, y):
    relac_lineal = np.corrcoef(x, y)[0,1]
    return relac_lineal

def modelo_geom(longitudes: list[float]) -> list[float]:
    pesos_predichos = []

    for L in longitudes:
        W = K_optimo * (L**3)
        pesos_predichos.append(W)

    return pesos_predichos

longitud = np.array([36.81, 31.77, 43.82, 36.82, 32.07, 45.07, 35.89])
peso_campeonato = np.array([0.78, 0.47, 1.16, 0.74, 0.44, 1.40, 0.64])

K_optimo = cal_k_constante(longitud, peso_campeonato)

peso_predicho = modelo_geom(longitud)

r = relacion_lineal_modpearson(longitud**3, peso_campeonato)

plt.figure(figsize=(8,5))
plt.scatter(longitud, peso_campeonato, color='navy', label='Datos del campeonato')

l_espacio = np.linspace(min(longitud), max(longitud), 100)
plt.plot(l_espacio, K_optimo * (l_espacio**3), color='mediumpurple', label='Modelo usado $W = Kl^3$')

plt.xlabel('Longitud (cm)')
plt.ylabel('Peso (kg)')
plt.title('Primer Modelo de Similitud Geométrica ajustado')

plt.legend()
plt.grid(True)
plt.show()

    """
    longitudes: list[float] representa la lista de longitudes (en cm) de los peces se usa para calcular los pesos de los mismos. 

    """
    ... # Puedes eliminar esta línea

def modelo_circ(longitudes: list[float]) -> list[float]:
    """
    longitudes: list[float] ¿Qué significa longitudes? 
    (Por favor elimina la pregunta y reemplazala con su respuesta)
    ...
    """
    ... # Puedes eliminar esta línea

def pearson(x:list[float], y: list[float]):
    """Calcula el coeficiente de pearson"""
    ...

def calc_error(pred:list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""

def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()

