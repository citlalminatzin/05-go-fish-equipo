[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jw8MUQHd)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23030704)
# Práctica 5: Modelos de Similitud Geométrica

**El Problema del Campeonato de Pesca De Róbalo**

Imaginemos que la competencia premia al pez más pesado, pero la única herramienta con la que contamos para determinar el peso de los peces es una cinta métrica. Como en las versiones anteriores del campeonato asistieron miles de participantes queremos poder predecir el peso de un pescado en término de algunas dimensiones fáciles de medir. A pesar de que el peso de un pescado se ve afectado por variables como la forma del pescado, la densidad del pescado, la edad del pescado, entre otras, haremos un modelo que dependa solo de variables medibles por nuestra cinta métrica. Algunos de los supuestos que usaremos en nuestro modelo son que:

• La especie está fija y todos los pescados serán robalos. (En general esto sí sucede en los campeonatos).

• La densidad de los pescados es constante. (Esto es poco realista pero nos servirá para un primer modelo).

• Las variables como la estación del año, el sexo, la edad, etc. no afectan al peso del róbalo.

• Los róbalos son geométricamente similares.

Ahora, recordando que la densidad (ρ) es igual a la masa entre el volumen, podemos calcular el peso (W) de un pescado multiplicando su volumen por su densidad:

$W =V ⋅ ρ$

Ahora, bajo nuestro supuesto de densidad constante y de similitud geométrica tenemos que

$W \propto V$

$W \propto l ^3$

A continuación pondremos a prueba nuestro primer modelo.

Nota:

• La masa corresponde a la cantidad de materia que compone un objeto determinado.

• El peso, en cambio, corresponde a la fuerza resultante de la acción que ejerce la gravedad de la Tierra (en nuestro caso).

## Integrantes

- Herrera Barrera Joyce
- Pulido Pérez José Antonio
- Rodríguez Rodríguez Diego


## Uso e instalación

Para ejecutar el código, necesitaremos:

- `matplotlib`: Lo necesitaremos para agregar y vizualizar las gráficas.
-  `numpy`: Lo necesitaemos para, entre otras cosas, calcular el coeficiente de correlación de Pearson.  

Primero, ejecuta modelos.py, en éste encontrarás funciones como:
 calc_error, modelo_geom, modelo_circ, cal_k_constante, cal_k_circ. Estas funciones nos servirán para construir y evaluar los modelos de similitud geométrica entre la longitud y el peso de los peces.
Hay funciones para estimar la constante K del modelo W = K L^3,
calcular pesos de la competencia, medir la correlación de Pearson y calcular error
entre predicción y datos reales.

Despues, ejecuta main.py, ahí podrás encontrar el código de los resultados esperados, (las gráficas).

## Ejercicio 1
Para poder ajustar nuestro modelo necesitamos datos sobre el peso $(W)$ y la longitud $(l)$ de algunos pescados. Los únicos datos sobrevivientes de los campeonatos anteriores se encuentran en la siguiente tabla: 

![Tabla de Datos](media/tabla.png)

En realidad, lo que medimos cuando "pesamos" en kg es la masa, y no el peso, de lo que estemos midiendo. 

Graficamos los datos de esta tabla de acuerdo a la relación:

$W \propto l ^3$

![Gráfica de relación $W y l^3$](media/grafica1.png)




## Ejercicio 2

Utiliza los datos anteriores y el método de tu preferencia para estimar un buen valor de $K$ para nuestro modelo de similaridad geométrica $W = Kl^3$. Grafica la estimación contra los datos. 

¿Qúe tan bueno es el ajuste? ¿Hay algún efecto que nuestro modelo no capture?


![Gráfica del Modelo $W = Kl^3$](media/grafica_modelo1.png)

*Modelo ajustado: $W = 1.45 \times 10^{-5} \cdot l^3$*
*Coeficiente de correlación $(r): 0.9907$*

En la imagen podemos notar que el ajuste es una muy buena aproximación. El ajuste toca dos puntos de la gráfica

## Ejercicio 3

# Coeficiente de correlación de Pearson

Ahora añadiremos una dimensión extra a nuestra tabla anterior. Supongamos que además de los datos anteriores también tenemos disponible la circunferencia máxima de cada pez.
|Cicunferencia Máxima|24.77|21.29|27.94|21.59|31.75|22.86|
|-----|----|-----|-----|-----|----|----|

Realice el ajuste del nuevo modelo en términos de la circunferencia ¿Cómo queda la fórmula explicita del modelo?¿Qué tan bueno es el ajuste?

El nuevo modelo:

## $W=k l C_m^2$
.

![Gráfica del Modelo $W = KL C^2$](media/grafica_modelo2.png)



## Conclusión

(Por favor modifica esta línea bro, es la última que tienes que modificar bro, por favor bro) Es buena práctica concluir tus prácticas. ¿Qué te llevas? ¿Sientes que fue relevante para ti? ¿Se te complicó algún aspecto? ¿Hubo algún resultado que contradijera tu intuición? 

---

[^1]: 1
