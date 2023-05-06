# Laboratorio 7: Filtros IIR y FIR
------------------------------------------------
En este laboratorio utilizaremos el dataset de ECG obtenido en el Laboratorio 6 y diseñaremos un filtro IIR y uno FIR. Luego compararemos en una tabla resumen la señal cruda, la señal con filtro IIR y la señal con filtro FIR.

<ul>
  <li> <a href="#intro"> Introducción</a> </li>
  <li> <a href="#metodo"> Metodología </a> </li>
  <ul> 
    <li><a href="#profe"> Usando filtro FIR e IIR </a></li>
    <li><a href="#bita"> Usando librería de BiosignalsNotebooks </a></li>
  </ul>
  <li> <a href="#tabla"> Tabla de resumen </a> </li> 
  <li> <a href="#conclu"> Conclusiones</a> </li>
  <li> <a href="#biblio"> Bibliografía </a> </li> 
</ul>

<h2 id="intro">Introducción</h2>
<p>Un filtro se define como un sistema que permite el paso de señales eléctricas dentro de un rango de frecuencias específico y limitado, bloqueando o impidiendo el paso de todas aquellas señales que se encuentran fuera de este rango. La aplicación de estos destacan en las telecomunicaciones (TV, radio, módem, etc) y en la instrumentación electrónica (sistemas de adquisición de datos, procesamiento de señales, etc)  [1]. </p>
<p>En el procesamiento de señales, se utiliza el término “filtro” para referirse a un dispositivo o proceso responsable de suprimir parcial o totalmente ciertas características o componentes no deseados de una señal. En la práctica, esto puede significar eliminar ciertas frecuencias de la señal para reducir el ruido de fondo y suprimir las señales de interferencia que pueden afectar la calidad de la señal. [2]</p>
<h2 id="metodo">Metodología</h2>
<h3 id="profe">Usando filtro FIR e IIR</h2> 
<h3 id="bita">Usando librería de BiosignalsNotebooks</h2> 
<p>Para realizar el filtrado de la señal mediante la librería BiosignalsNotebooks nos guiamos de la siguiente página: http://notebooks.pluxbiosignals.com/notebooks/Categories/Pre-Process/digital_filtering_filtfilt_rev.html</p>
<p>Primero incluimos todas las librerías que vamos a usar para el diseño de filtros.</p>
<pre>
<code>import biosignalsnotebooks as bsnb
from numpy import arange, sin, pi
from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import pandas as pd
from IPython.display import display
import sympy</code>
</pre>
<p></p>
<p>Iniciamos con la lectura de las señales que estan en archivos .txt, para esto usamos la librería numpy.</p>
<pre>
<code>#Lectura de documento txt con tabulación (/t) como delimitador
array1 = np.genfromtxt("Basal_ECG.txt", delimiter="\t")
array2 = np.genfromtxt("Aguantando_respiracion_ECG.txt", delimiter="\t")
array3 = np.genfromtxt("Post_ejercicio_ECG.txt", delimiter="\t")</code>
</pre>
<p>Cortamos las señales en el inicio y el final para eliminar los errores que se generan al inicio y final de la medición.</p>
<pre>
<code>#Nos quedamos con el dato del sensor
#Estado basal
basal = array1[:,-2]
basal = basal[1000:31000]
#Aguantando la respiración
respiracion = array2[:,-2]
respiracion =respiracion[1000:31000]
#Post-ejercicio
ejercicio = array3[:,-2]
ejercicio = ejercicio[1000:31000]</code>
</pre>
<p></p>
<p>Definimos la frecuencia de muestreo en 1000 Hz debido a que la frecuencia del Bitalino es esa.</p>
<p></p>
<pre>
<code>Fs = 1000 #Frecuencia de muestreo del dispositivo de adquisición</code>
</pre>
<p></p>
<p>Hallamos los espectros de frecuencia de cada señal, para ello realizamos la FFT de cada una.</p>
<p></p>
<pre>
<code>N=2**10 # 10 bits
#FFT de señal basal
Basal = np.fft.fft(basal,N)
Basal = Basal[0:N//2]
Basalm = np.abs(Basal)
F = np.linspace(0,Fs/2,N//2)
#FFT de señal aguantando respiración
Respiracion = np.fft.fft(respiracion,N)
Respiracion = Respiracion[0:N//2]
Respiracionm = np.abs(Respiracion)
F = np.linspace(0,Fs/2,N//2)
#FFT de señal post-ejercicio
Ejercicio = np.fft.fft(ejercicio,N)
Ejercicio = Ejercicio[0:N//2]
Ejerciciom = np.abs(Ejercicio)
F = np.linspace(0,Fs/2,N//2)

#Graficamos las señales y sus FFT
fig, axs = plt.subplots(3, 2, figsize=(16, 9))
fig.subplots_adjust(hspace=0.5)

axs[0, 0].plot(basal)
axs[0, 0].set_title('Señal basal')
axs[0, 0].set_xlabel('Samples')
axs[0, 0].set_ylabel('mV')
axs[0, 0].grid(True)
axs[0, 0].set_xlim(0,2000)

axs[0, 1].plot(Basalm)
axs[0, 1].set_title('FFT señal basal')
axs[0, 1].set_xlabel('Frecuencias (hz)')
axs[0, 1].set_ylabel("FFT (db)")
axs[0, 1].grid(linestyle=":")
axs[0, 1].set_xlim(0,150)
axs[0, 1].set_ylim(0,10000)

axs[1, 0].plot(respiracion)
axs[1, 0].set_title('Señal aguantando la respiración')
axs[1, 0].set_xlabel('Samples')
axs[1, 0].set_ylabel('mV')
axs[1, 0].grid(True)
axs[1, 0].set_xlim(0,2000)

axs[1, 1].plot(Respiracionm)
axs[1, 1].set_title('FFT señal aguantando la respiración')
axs[1, 1].set_xlabel('Frecuencias (hz)')
axs[1, 1].set_ylabel("FFT (db)")
axs[1, 1].grid(linestyle=":")
axs[1, 1].set_xlim(0,150)
axs[1, 1].set_ylim(0,10000)

axs[2, 0].plot(ejercicio)
axs[2, 0].set_title('Señal post-ejercicio')
axs[2, 0].set_xlabel('Samples')
axs[2, 0].set_ylabel('mV')
axs[2, 0].grid(True)
axs[2, 0].set_xlim(0,2000)

axs[2, 1].plot(Ejerciciom)
axs[2, 1].set_title('FFT señal post-ejercicio')
axs[2, 1].set_xlabel('Frecuencias (hz)')
axs[2, 1].set_ylabel("FFT (db)")
axs[2, 1].grid(linestyle=":")
axs[2, 1].set_xlim(0,150)
axs[2, 1].set_ylim(0,10000)</code>
</pre>
<p></p>
<p>La gráficas de los espectros de frecuencia son los siguientes.</p>
<p align="center"><img src="../../Imagenes/Filtro_bitalino/Señales con FFT.png"></p> 
<p></p>

<p></p>
<p>Según bibliografía la frecuencia de un electrocardiograma va desde 0 a 100 Hz [3], sin embargo, como en nuestras señales observamos que la información se agrupa en las frecuencias más bajas las decidimos cortar antes del pico que representa el ruido eléctrico, para la señal basal la frecuencia de corte la establecimos como  30 Hz, para la señal aguantando la respiración la frecuencia de corte serála establecimos como  40 Hz y por ultimo para la señal post-ejercicio la frecuencia de corte la establecimos como 50 Hz .</p>
<p></p>

<p>Con la librería de BiosignalNotebooks creamos los filtros para cada caso.</p>
<p></p>
<pre>
<code># Creamos un filtro Butterworth de tercer orden y con una frecuencia de 30 Hz para la señal basal
basal_filter = bsnb.lowpass(basal, 30, order=3)
filtfilt_basal = bsnb.lowpass(basal, 30, order=3, use_filtfilt=True)
#
# Creamos un filtro Butterworth de tercer orden y con una frecuencia de 40 Hz para la señal aguantando la respiración
respiracion_filter = bsnb.lowpass(respiracion, 40, order=3)
filtfilt_respiracion = bsnb.lowpass(respiracion, 40, order=3, use_filtfilt=True)
#
# Creamos un filtro Butterworth de tercer orden y con una frecuencia de 50 Hz para la señal post ejercicio
ejercicio_filter = bsnb.lowpass(ejercicio, 50, order=3)
filtfilt_ejercicio = bsnb.lowpass(ejercicio, 100, order=3, use_filtfilt=True)</code>
</pre>
<p></p>
<p>Graficamos la señal correspondiente junto con las señales filtradas.</p>
<p align="center"><img src="../../Imagenes/Filtro_bitalino/Señales con señal filtrada.png"></p> 
<p></p>

<p></p>
<h2 id="tabla">Tabla de resumen</h2>
<table border="1">
		<tr>
			<th>Campo</th>
			<th>Señal cruda</th>
			<th>Filtro FIR</th>
			<th>Filtro IIR</th>
			<th>Filtro BiosignalNotebooks</th>
		</tr>
		<tr>
			<td>Basal</td>
			<td>Fila 1, Columna 2</td>
			<td>Fila 1, Columna 3</td>
			<td>Fila 1, Columna 4</td>
			<td>Fila 1, Columna 5</td>
		</tr>
		<tr>
			<td>Respiración</td>
			<td>Fila 2, Columna 2</td>
			<td>Fila 2, Columna 3</td>
			<td>Fila 2, Columna 4</td>
			<td>Fila 2, Columna 5</td>
		</tr>
		<tr>
			<td>Post-ejercicio</td>
			<td>Fila 3, Columna 2</td>
			<td>Fila 3, Columna 3</td>
			<td>Fila 3, Columna 4</td>
			<td>Fila 3, Columna 5</td>
		</tr>
	</table>
<h2 id="conclu">Conclusiones</h2>
<h2 id="biblio">Bibliografía</h2>