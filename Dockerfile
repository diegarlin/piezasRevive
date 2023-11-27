# Utiliza una imagen base de Python para Windows
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY . /app

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Puerto en el que tu aplicación escucha (ajusta según tus necesidades)
EXPOSE 8000

# Ejecuta los comandos de migraciones al construir el contenedor
RUN python manage.py makemigrations
RUN python manage.py migrate

# Comando para ejecutar tu aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]