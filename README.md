# PRERREQUISITOS



1. Tener instalado Docker Desktop para la importación de imágenes y ejecución de contenedores. Si no lo tiene instalado descargarse el [ejecutable ](https://www.docker.com/products/docker-desktop/)para el sistema operativo que esté usando y hacerse cuenta.
2. Tener abierto esta aplicación en todo momento.
3. Descargar el archivo .tar del [repositorio](https://github.com/diegarlin/piezasRevive), de la última release publicada.


# IMPORTACIÓN Y EJECUCIÓN



1. Abrir un terminal en la carpeta donde se encuentre el archivo .tar, probablemente descargas. Escribir cmd y pulsar intro tal como se ve en las captura.

    

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


2. Escribir estos 2 comandos:
    1. docker load -i piezasRevive.tar 

		Copiar, pegarlo pulsar intro y esperar hasta que vuelva a salir una linea de la cmd



    2. docker run -p 8080:8080 piezasrevive

        Saldrá un mensaje que pone

3. Tras ello entramos en el navegador y ponemos [http://localhost:8080/](http://localhost:8080/), y ya tendrá la aplicación funcionando.


# RECOMENDACIONES E INSTRUCCIONES



* Si pagamos mediante la pasarela de pago la tarjeta debe ser:

    4000056655665556	


    CVV: 3 dígitos aleatorios 


    Fecha caducidad: Cualquier fecha futura

* La entrega express durará 2 días y la entrega normal durará 4 días desde el día actual
