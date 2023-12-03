docker build -t piezasrevive .

docker save -o piezasRevive.tar piezasrevive
docker load -i piezasRevive.tar

docker run -p 8080:8080 piezasrevive

Visa (débito)	4000056655665556	3 dígitos aleatorios	Cualquier fecha futura