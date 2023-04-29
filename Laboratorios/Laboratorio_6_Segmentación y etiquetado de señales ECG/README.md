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
  <li> <a href="#Resultado"> Resultados </a> </li>
  <li> <a href="#codigo"> Código </a> </li> 
</ul>
<h2 id="Basal">Consideraciones en el procesamiento de señal ECG basal</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>DSegun lo que se ve en la graficacion de los datos, la senal original que se obtiene del sensor posee ruido por lo que se procede a recortar dicha senal. El primer punto de corte se hace en 2050, que es donde se empieza los ciclos cardiacos ademas se escoge ese punto ya que es donde aproximadamente empieza la onda P, se puede observar en la grafica de la senal original que antes del punto que escogimos hay dos ciclos cardiacos, pero no se eligieron esos como ciclos iniciales ya que todavia pueden estar afectados por el ruido. El segundo punto de corte se hace en 30457, ya que es donde aproximadamente termina la onda T del penultimo ciclo y empieza la onda P del ultimo ciclo. </li>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Basal zoom.png">              
  <li>Al momento de realizar la segmentación de la gráfica de la señal, hacemos una gráfica de la señal durante 1 segundo y observamos que el ciclo dura 0.56 segundos. El timepo hallado se usa en la segmentación para obtener partes que solo contengan un ciclo cardiaco. </li>
      <p></p>   
      <p align="center"><img src="../../Imagenes/Segmentación ECG/Comparación ciclo basal.png"> 
     <p></p>    
  <h2 id="Respiración">Consideraciones en el procesamiento de señal ECG en respiración</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>Segun lo que se ve en la graficacion de los datos, la senal original que se obtiene del sensor no posee tanto ruido por lo que se hara pequenos recortes para tener puntos fijos de que parte del ciclo cardiaco empezara y terminara nuestra senal. El primer punto de corte se hace en 400, que es donde empieza la onda P del segundo ciclo cardiaco de nuestra senal, ya que el primer ciclo no esta tan claro. El segundo punto de corte se hace en 30829, ya que es donde aproximadamente termina la onda T del penultimo ciclo y empieza la onda P del ultimo ciclo.</li>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Respiracion zoom.png"></p>
    <p></p>
  <li>Al momento de realizar la segmentación de la gráfica de la señal, hacemos una gráfica de la señal durante 1 segundo y observamos que el ciclo dura 0.63 segundos. El timepo hallado se usa en la segmentación para obtener partes que solo contengan un ciclo cardiaco. </li>
      <p align="center"><img src="../../Imagenes/Segmentación ECG/Comparación ciclo respiracion.png"> 
     <p></p>    
  </ul>
  <h2 id="Ejercicio">Consideraciones en el procesamiento de señal ECG en post ejercicio</h2>
  <ul>
  <li>Frecuencia de muestreo: 1000 Hz. Se usa la frecuencia de muestreo del Bitalino </li>
  <li>Segun lo que se ve en la graficacion de los datos, la senal original que se obtiene del sensor no posee tanto ruido por lo que se hara pequenos recortes para tener puntos fijos de que parte del ciclo cardiaco empezara y terminara nuestra senal. El primer punto de corte se hace en 500, que es donde empieza la onda P del segundo ciclo cardiaco de nuestra senal, para evitar pequenos ruidos que puede haber en el primer ciclo cardiaco que aparece en nuestra senal. El segundo punto de corte se hace en 20156, ya que es donde aproximadamente termina la onda T del penultimo ciclo y empieza la onda P del ultimo ciclo.</li>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Ejercicio zoom.png"> 
    <p></p>  
      <li>Al momento de realizar la segmentación de la gráfica de la señal, hacemos una gráfica de la señal durante 1 segundo y observamos que el ciclo dura 0.37 segundos. El timepo hallado se usa en la segmentación para obtener partes que solo contengan un ciclo cardiaco.</li>
    <p></p>    
      <p align="center"><img src="../../Imagenes/Segmentación ECG/Comparación ciclo ejercicio.png"> 
        <p></p>    
  </ul>
<h2 id="Resultado">Resultados</h2>
    <p> Después de la segmentación comprobamos si se ha realizado correctamente, para eso seleccionamos el segmento inicial, el medio y el final de cada señal ECG. </p>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Resultados.png"> 
      <p></p>
    <p>Los arrays resultantes de cada señal fueron arreglados para que contengan la misma cantidad de elementos y se juntaron en solo array que tiene la siguiente gráfica.</p>
    <p></p>
    <p align="center"><img src="../../Imagenes/Segmentación ECG/Array.png"> 
      
<h2 id="codigo">Código</h2>
    <p>El código de python se encuentra en el este <A HREF="https://github.com/EduardoSalazarA/IntroSenales/blob/main/Software/Laboraotrio%206_Segmentaci%C3%B3n_ECG.ipynb"> link</A> </p>
