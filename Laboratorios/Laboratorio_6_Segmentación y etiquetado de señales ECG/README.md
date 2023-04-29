<h1>Laboratorio 6: Segmentación y etiquetado para señales de ECG</h1>
<p>En este labotorio utilizaremos las señales EGC obtenidas por el Bitalino para realizar una segmentación con la cual obtener una sola curva QRS caracteristica de la señal analizada. La curva QRS se etiqueta de acuerdo a la señal a la que correponde y se le asigna un valor .</p>
<table>
  <tr>
    <th>Descripción</th>
    <td>Categoría</td> </tr>
    <tr><td>Basal</td>
    <td>0</td></tr>
    <tr><td>Respiración</td>
    <td>1</td></tr>
    <tr><td>Post-ejercicio</td>
    <td>2</td></tr>
<table>
  
<h2>Tabla de Contenidos</h2>
<ul>
  <li> <a href="#Basal"> Consideraciones en el procesamiento de señal ECG basal</a> </li>
  <li> <a href="#Respiración"> Consideraciones en el procesamiento de señal ECG en respiración </a> </li>
  <li> <a href="#Ejercicio"> Consideraciones en el procesamiento de señal ECG post-ejercicio </a> </li> 

</ul>
<h2 id="Basal">Consideraciones en el procesamiento de señal ECG basal</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>Debido a que nuestra señal al inicio presenta data errónea, que no es caracteristica de una señal ECG, se recortó la señal en X, además se realizó un ploteo de los ultimos valores d la señal y obtuvimos que se corta en un pico que puede causar errores al momento de segmentar, recortamos la señal en Y, lo que nos deja una señal recortada de la señal original en un rango de [X:Y] </li>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Señal basal entera.png" width="400">              
    <align="center"><img src="../../Imagenes/Segmentación ECG/Señal basal final.png" width="450"></p>
  <li>Ignacio</li>
  <li>Elena</li>
  </ul>
  <h2 id="Respiracion">Consideraciones en el procesamiento de señal ECG en respiración</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>Ignacio</li>
  <li>Elena</li>
  </ul>
  <h2 id="Ejercicio">Consideraciones en el procesamiento de señal ECG en post ejercicio</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>Se realiza</li>
  <li>Elena</li>
  </ul>
