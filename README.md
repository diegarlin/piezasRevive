PRERREQUISITOS
Tener instalado Docker Desktop para la importación de imágenes y ejecución de contenedores. Si no lo tiene instalado descargarse el ejecutable para el sistema operativo que esté usando y hacerse cuenta.
Tener abierto esta aplicación en todo momento.
Descargar el archivo .tar del repositorio, de la última release publicada.

IMPORTACIÓN Y EJECUCIÓN
Abrir un terminal en la carpeta donde se encuentre el archivo .tar, probablemente descargas. Escribir cmd y pulsar intro tal como se ve en las captura.

Escribir estos 2 comandos:

docker load -i piezasRevive.tar 
		Copiar, pegarlo pulsar intro y esperar hasta que vuelva a salir una linea de la cmd

docker run -p 8080:8080 piezasrevive
Saldrá un mensaje que pone

Tras ello entramos en el navegador y ponemos http://localhost:8080/, y ya tendrá la aplicación funcionando.

RECOMENDACIONES E INSTRUCCIONES
Si pagamos mediante la pasarela de pago la tarjeta debe ser:

4000056655665556	
CVV: 3 dígitos aleatorios 
Fecha caducidad: Cualquier fecha futura

La entrega express durará 2 días y la entrega normal durará 4 días desde el día actual

