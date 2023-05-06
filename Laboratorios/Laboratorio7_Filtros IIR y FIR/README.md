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
<p>Un filtro se define como un circuito o sistema capaz de dejar pasar selectivamente señales eléctricas dentro de un rango de frecuencias específico a partir de una señal de entrada que consta de una combinación de diferentes frecuencias. Una aplicación común de los filtros se da en sistemas estéreo de alto rendimiento, donde ciertos rangos de frecuencias de audio necesitan ser amplificados o suprimidos para mejorar la calidad del audio o la eficiencia en términos de uso de energía [1]. </p>
<p></p>
<h2 id="metodo">Metodología</h2>
<h3 id="profe">Usando filtro FIR e IIR</h2> 
<p>Realizamos el filtrado mediante el uso de un filtro FIR y un filtro IIR.</p>
<p>Primero incluimos las librerías que vamos a usar para el diseño de los filtros.</p>
<pre>
<code>#Importación de librerías
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Seleccionamos estilo de ploteo
plt.style.use("ggplot")</code>
</pre>
<p>Realizamos la lectura de las señales que se encuentran en archivo .txt para ello usamos la librería numpy.</p>
<pre>
<code>#Lectura de documento txt con tabulación (/t) como delimitador
array1 = np.genfromtxt("Basal_ECG.txt", delimiter="\t")
array2 = np.genfromtxt("Aguantando_respiracion_ECG.txt", delimiter="\t")
array3 = np.genfromtxt("Post_ejercicio_ECG.txt", delimiter="\t")

#Nos quedamos con el dato del sensor
basal_sensor = array1[:,-2]
resp_sensor = array2[:,-2]
ejer_sensor = array3[:,-2]</code>
</pre>
<p>Calculamos la FFT de cada una de las señales y las graficamos.</p>
<pre>
<code>def plot_FFT(signal, n_signal, Fs, plot_title, plot_xlim):
    N = len(n_signal)
    X = np.fft.fft(signal, N)
    
    X = X[0:N//2]
    F = np.linspace(0, Fs/2, N//2)
    
    Xm = np.abs(X)
    Xm = np.round(Xm,3)
    Xm[0] = 0
    
    plt.figure(figsize=(20, 4))
    plt.plot(F,Xm)
    plt.title(plot_title)
    plt.xlabel("Frequency")
    plt.xlim(0, plot_xlim)
    return X

Fs = 1000

n_basal = np.arange(0,basal_sensor.shape[0])
n_resp = np.arange(0,resp_sensor.shape[0])
n_ejer = np.arange(0,ejer_sensor.shape[0])

FFT_basal = plot_FFT(basal_sensor, n_basal, Fs, 'Basal', 150)
FFT_resp = plot_FFT(resp_sensor, n_resp, Fs, 'Respiracion', 150)
FFT_ejer = plot_FFT(ejer_sensor, n_ejer, Fs, 'Post-ejercicio', 150)</code>
</pre>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT basal.png"></p> 
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT respiracion.png"></p> 
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT ejercicio.png"></p> 
<p></p>
<p>Creamos el filtro FIR pasabandas con un metodo de enventanado Hamming,con frecuencias de corte inferior de 0.5 Hz y de corte superior de 100 Hz [3]. También se realizó un filtro Notch para eliminar el ruido electrico con frecuencia de 60 Hz .</p>
<pre>
<code>import scipy.signal as sig

#Se utilizo esta longitud de la ventana, principalmente por su precision a las frecuencias bajas, ya que por bibliografia las señales de ruido de un ECG
#son menores a 0.5Hz y mayores a 100Hz
M = 601

def filtro_FIR(M, Fs, f1, f2, signal):
    #Filtro FIR
    w = sig.firwin(numtaps=M, fs=Fs, pass_zero=False, cutoff=[f1,f2], window='hamming')
    w = np.round(w,3)
    y = sig.lfilter(w, np.array(1),signal)
    
    #Coeficientes para el filtro notch que filtrada el ruido electrico w0=60Hz, con un factor de calidad Q=w0/bw, si queremos un ancho de banda de 2Hz -> Q=30
    b, a = sig.iirnotch(w0=60, Q=30, fs=Fs)  
     
    #Filtramos el ruido electrico que se encuentra en 60Hz
    y = sig.filtfilt(b, a, y)
    
    return y, w

filtro = filtro_FIR(M, Fs, 0.5, 100, basal_sensor)[1]
plot_filtro = plot_FFT(filtro, n_basal, Fs, 'Filtro', 150)

basal_fir = filtro_FIR(M, Fs, 0.5, 100, basal_sensor)[0]
FFT_basalFIR = plot_FFT(basal_fir, n_basal, Fs, 'Basal filtrada', 150)

resp_fir = filtro_FIR(M, Fs, 0.5, 100, resp_sensor)[0]
FFT_respFIR = plot_FFT(resp_fir, n_resp, Fs, 'Respiracion filtrada', 150)

ejer_fir = filtro_FIR(M, Fs, 0.5, 100, ejer_sensor)[0]
FFT_ejerFIR = plot_FFT(ejer_fir, n_ejer, Fs, 'Post-ejercicio filtrada', 150)</code>
</pre>
<p>Graficamos el espectro de frecuencia filtrado de cada señal.</p>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/Espectro filtro FIR.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT basal filtrado.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT respiracion filtrado.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT ejercicio filtrado.png">
<p></p>
<p>Graficamos las señales filtradas y la señal con el desfase arreglado.</p>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/Señales filtradas FIR.png">
<p></p>
<p>Creamos el filtro IIR Butterworth pasabandas  con las mismas frecuencias de corte que el filtro FIR, frecuencia de corte inferior igual a 0.5 Hz y frecuencia de corte superior igual a 100 Hz, .</p>
<pre>
<code>from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Especificaciones del filtro
fc1 = 0.5  # frecuencia de corte inferior
fc2 = 100  # frecuencia de corte superior
order = 2  # orden del filtro

#Diseñar filtro
b, a = signal.butter(order, [fc1/(Fs/2), fc2/(Fs/2)], btype='bandpass')
w, h = signal.freqz(b, a, worN=8000)
f = w / (2 * np.pi) * fs
db = 20 * np.log10(abs(h))

#Gráfico de respuesta en frecuencia del filtro
fig, ax = plt.subplots(figsize=(16,3))
ax.plot(f, db)
ax.set_xscale('log')
ax.set_xlabel('Frecuencia (Hz)')
ax.set_ylabel('Magnitud (dB)')
ax.set_title('Respuesta en frecuencia del filtro IIR Butterworth')
ax.axvline(x=fc1, color='r', linestyle='--')
ax.axvline(x=fc2, color='r', linestyle='--')
plt.show()

#Aplicando filtro IIR
basal_iir = sig.filtfilt(b, a, basal_sensor)
resp_iir = signal.filtfilt(b, a, resp_sensor)
ejer_iir = signal.filtfilt(b, a, ejer_sensor)


#Coeficientes para el filtro notch que filtrada el ruido electrico w0=60Hz, con un factor de calidad Q=w0/bw, si queremos un ancho de banda de 2Hz -> Q=30
bn, an = sig.iirnotch(w0=60, Q=30, fs=Fs)  
     
#Filtramos el ruido electrico que se encuentra en 60Hz
basal_iir = sig.filtfilt(bn, an, basal_iir)
FFT_basalIIR = plot_FFT(basal_iir, n_basal, Fs, 'Basal filtrada', 150)

resp_iir = sig.filtfilt(bn, an, resp_iir)
FFT_respIIR = plot_FFT(resp_iir, n_resp, Fs, 'Respiracion filtrada', 150)

ejer_iir = sig.filtfilt(bn, an, ejer_iir)
FFT_ejerIIR = plot_FFT(ejer_iir, n_ejer, Fs, 'Post-ejercicio filtrada', 150)</code>
</pre>
<p>Graficamos el espectro de frecuencia filtrado de cada señal.</p>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/Espectro filtro IIR.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT basal filtrado IIR.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT respiracion filtrado IIR.png">
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/FFT ejercicio filtrado IIR.png">
<p></p>
<p>Graficamos las señales filtradas y la señal con el desfase arreglado.</p>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/Señales filtradas IIR.png">
<p></p>
<p>Hacemos una gráfica para comparar el filtro FIR del filtro IIR.</p>
<p></p>
<p align="center"><img src="../../Imagenes/Filtro FIR IIR/Comparación FIR IIR.png">
<p></p>

<h3 id="bita">Usando librería de BiosignalsNotebooks</h2> 
<p>Para realizar el filtrado de la señal mediante la librería BiosignalsNotebooks nos guiamos de la siguiente página [4] </p>
<p>Primero incluimos todas las librerías que vamos a usar para el diseño de los filtros.</p>
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
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Basal original.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Basal FIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Basal IIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Basal bitalino.png"></p> </td>
		</tr>
		<tr>
			<td>Respiración</td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Respiracion original.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Respiracion FIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Respiracion IIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Respiracion bitalino.png"></p> </td>
		</tr>
		<tr>
			<td>Post-ejercicio</td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Ejercicio original.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Ejercicio FIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Ejercicio IIR.jpg"></p> </td>
			<td><p align="center"><img src="../../Imagenes/Filtro_bitalino/Ejercicio bitalino.png"></p> </td>
		</tr>
	</table>
<h2 id="conclu">Conclusiones</h2>
<h2 id="biblio">Bibliografía</h2>
<p>[1]</p>
<p>[2]</p>
<p>[3] https://doi.org/10.17533/udea.redin.14718</p>
<p>[4] http://notebooks.pluxbiosignals.com/notebooks/Categories/Pre-Process/digital_filtering_filtfilt_rev.html</p>

