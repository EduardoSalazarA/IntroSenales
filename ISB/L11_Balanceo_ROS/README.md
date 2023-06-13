# Informe de Laboratorio: Importancia del Balanceo de Datos utilizando ROS

## Introducción
En este laboratorio, exploraremos la importancia del balanceo de datos en problemas de clasificación utilizando la técnica ROS (Random Over-Sampling). El objetivo es abordar el desequilibrio de clases en los conjuntos de datos y mejorar el rendimiento de los modelos de aprendizaje automático.

## Definición sobre las Inteligencias Artificiales
Las inteligencias artificiales (IA) son sistemas que intentan imitar la inteligencia humana para resolver problemas de manera automatizada. En el campo del aprendizaje automático, las IA utilizan algoritmos para analizar y aprender de los datos, siendo la clasificación una tarea común en la que se asignan etiquetas o categorías a los datos.

## Comentarios sobre el Código
En este laboratorio, se utilizó el siguiente código de ejemplo para realizar la regresión logística y aplicar el balanceo de datos utilizando ROS. A continuación, se destacan los cambios realizados en el código original para resaltar la importancia del balanceo de datos:

1. **Añadiendo nueva matriz**: Se agrego Variables al codigo para obtener las variables del ventilador y salida:

   ```python
   #visualizamos el dataset
   df= pd.read_csv(data)
   Variables = ['P_ventilador', 'V_out'] #C Rp Dif_vol V_in V_out P_ventilador PIP
   df.head()
2. **Inclusión de variables**: Se cambiaron los valores de x para mejorar la presición del modelo:

   ```python
   # definimos la matriz de caracteristicas
   x = d_filtrado.loc[:, Variables]
   y = d_filtrado['Error_aceptable']
3. **Comprobando los cambios**:El codigo se ejecuta como tal con el objetivo de apreciar un cambio en los valores de P ademas de buscar cambios notables:
   ```python
      # Se anñade una columna constante para el término de intercepción
      x_train_with_const = sm.add_constant(x_train)
      
      # Crear un modelo logístico con statsmodels
      logit_model = sm.Logit(y_train, x_train_with_const)
      
      # Ajustar el modelo
      result = logit_model.fit()
      
      # Obtener los coeficientes y los p-valores
      coefficients = result.params
      p_values = result.pvalues
      
      print("Coeficientes:")
      print(coefficients)
      print("\nP-valores:")
      print(p_values)

<p align="center"><img src="https://github.com/EduardoSalazarA/IntroSenales/blob/main/ISB/Imagenes/p_new.JPG">
</p>
<p align="center"><img src="https://github.com/EduardoSalazarA/IntroSenales/blob/main/ISB/Imagenes/Classification_Report.JPG">
</p>




## Conclusiones
### 1 Mejora del rendimiento del modelo: 
Al aplicar la técnica de balanceo de datos utilizando ROS, se logró reducir significativamente el valor de p a menos de 0.5 (paso a p=0.000646 desde p=0.5). Esto indica una mayor significancia estadística de los coeficientes del modelo y una mayor confianza en los resultados obtenidos.

### 2 Impacto en el rendimiento del modelo: 
El balanceo de datos utilizando ROS tiene un impacto positivo en el rendimiento del modelo de aprendizaje automático. Al equilibrar las clases del conjunto de datos, se reducen los sesgos y se mejora la capacidad predictiva del modelo. Esto se refleja en una mayor precisión y capacidad de generalización en la clasificación de nuevos datos.

### 3 Implicaciones y aplicaciones prácticas:
El balanceo de datos utilizando ROS tiene implicaciones importantes en problemas reales donde hay un desequilibrio de clases. En campos como la detección de fraudes, diagnóstico médico o análisis de anomalías, donde la clase minoritaria puede ser crucial, el uso de ROS puede ayudar a identificar y predecir casos positivos con mayor precisión.

### 4 Áreas de mejora e investigaciones futuras: 
Aunque ROS es una técnica efectiva para abordar el desequilibrio de clases, existen áreas de mejora y posibles investigaciones futuras. Algunas áreas a considerar incluyen la exploración de otras técnicas de balanceo de datos, como SMOTE (Synthetic Minority Over-sampling Technique), y la evaluación del impacto del balanceo de datos en diferentes algoritmos de aprendizaje automático. Además, se pueden investigar estrategias de selección de características para mejorar aún más el rendimiento del modelo.
