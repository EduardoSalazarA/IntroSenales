# Procesamiento de Señales EEG

Este repositorio contiene el trabajo del laboratorio sobre procesamiento de señales electroencefalograficas (EEG) en el campo de la Ingeniería Biomédica. El objetivo principal de este estudio es analizar y extraer información relevante de la actividad eléctrica del cerebro utilizando técnicas de procesamiento de señales. A continuación, se presentan los principales aspectos abordados en este trabajo:

## Extraccion de la señal EEG
En esta sección, se extraen los datos del archivo de texto que devuelve el Open BCI al utilizar el ULTRACORTEX "MARK IV".![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/c678118c-7726-49d6-bffb-ee19fe70bc3f)

## Analisis en frecuencia
En el archivo de texto encontramos la frecuencia de muestreo de 125 Hz que se utilizo en el experimento. Procedemos a analizar la magnitud del espectro de la transformada rapida de Fourier. ![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/02318140-9440-47c4-b39a-08ef757f21ba)

## Filtrado de la señal EEG
En esta sección, se exploran diferentes técnicas de filtrado para eliminar el ruido presente en la señal EEG. Se implementan filtros pasabanda para mejorar la calidad de la señal y facilitar el análisis posterior.
![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/f99fa5a8-dc46-4200-a2fb-feb59b303d1d)

## Normalizacion de la señal
Realizamos la normalización lo cual asegura que las señales de diferentes registros de EEG sean comparables entre sí. Dado que los registros de EEG pueden variar en amplitud y rango dinámico debido a diferencias en la colocación de los electrodos, la impedancia de los electrodos y otros factores, normalizar la señal ayuda a eliminar estas diferencias y permite la comparación directa de las características de interés.![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/ead03940-2f2e-4e54-a061-70103ecedb7c)

## Extracción de la onda Alfa
Las ondas alfa son oscilaciones eléctricas que ocurren en el rango de frecuencia de 8 a 13 Hz y se asocian típicamente con un estado de relajación mental y alerta tranquila. La extracción de las ondas alfa en el EEG puede ser útil para medir y evaluar el nivel de relajación o calma en un individuo. ![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/4707a0c4-e411-41d6-bc31-8d1d8395e9b7)

## Extraccion de la onda Beta
Las ondas beta están relacionadas con la actividad mental activa, especialmente en tareas que requieren concentración, atención y procesamiento cognitivo. La extracción y el análisis de las ondas beta pueden ayudar a evaluar la carga cognitiva y la activación mental durante tareas como resolución de problemas, toma de decisiones y procesamiento de información compleja.![image](https://github.com/EduardoSalazarA/IntroSenales/assets/128836484/d8d75b06-da1a-485b-93de-ea4b70b08990)

## Referencias
- “Electroencefalografía (EEG) - Trastornos neurológicos - Manual MSD versión para profesionales”. MSD Manual. Recuperado el 3 de junio de 2023, de https://www.msdmanuals.com/es/professional/trastornos-neurol%C3%B3gicos/pruebas-y-procedimientos-neurol%C3%B3gicos/electroencefalograf%C3%ADa-eeg
