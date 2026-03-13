#!/usr/bin/env python
"""
models.py

Aquí se encuntran las funciones reutilizables para construir y evaluar los
modelos de similitud geométrica entre la longitud y el peso de los peces.
Hay funciones para estimar la constante K del modelo W = K L^3,
calcular pesos de la competencia, medir la correlación de Pearson y calcular error
entre predicción y datos reales.
"""
import numpy as np

def cal_k_constante(longitudes, pesos):
    """Calculamos la constante K del modelo W = K L^3."""
    longitudes = np.array(longitudes)
    pesos = np.array(pesos)

    k_valores = pesos / (longitudes ** 3)
    return np.mean(k_valores)


def modelo_geom(longitudes: list[float], K: float) -> list[float]:
    """
    Modelo de similitud geométrica.
    longitudes= lista de longitudes de peces (en cm)
    K es la constante del modelo
    Regresa la lista de pesos de la competencia usando W = K L^3
    """
    pesos_competencia = []

    for L in longitudes:
        W = K * (L ** 3)
        pesos_competencia.append(W)

    return pesos_competencia


def cal_k_circ(longitudes, circunferencias, pesos):
    """Calcula K para el modelo W = K L C^2."""
    k_vals = []

    for L, C, W in zip(longitudes, circunferencias, pesos):
        k_vals.append(W / (L * (C ** 2)))

    return np.mean(k_vals)


def modelo_circ(longitudes, circunferencias, K):
    """Predice pesos usando W = K L C^2."""
    pesos = []

    for L, C in zip(longitudes, circunferencias):
        pesos.append(K * L * (C ** 2))

    return pesos


def pearson(x: list[float], y: list[float]):
    """Calcula el coeficiente de correlación de Pearson."""
    x = np.array(x)
    y = np.array(y)

    return np.corrcoef(x, y)[0, 1]


def calc_error(pred: list[float], truth: list[float]):
    """Calcula el error cuadrático medio entre predicción y datos reales."""
    pred = np.array(pred)
    truth = np.array(truth)

    return np.mean((pred - truth) ** 2)
