# Script1

## Pre-requisitos
1. Verificar que la librería `requests` esté instalada. En caso de no estarlo, instalarla ejecutando el siguiente comando:
   ```bash
   pip install requests
   ```

2. Asegurarse de que Docker esté instalado. Si no está instalado, seguir las instrucciones disponibles en [este enlace](https://docs.docker.com/get-docker/).

## Pasos para ejecutar el proyecto

1. Descargar la imagen de Docker de AltoroJ ejecutando el siguiente comando en la terminal:
   ```bash
   docker run --name altoroj -d -p 8130:8080 jasonhubs/altoroj:3.1.1
   ```

2. Verificar que el contenedor esté corriendo. Si no se ha iniciado automáticamente, se puede iniciar manualmente con el siguiente comando:
   ```bash
   docker start altoroj
   ```

3. Ejecutar el **script número 1** en Python abriendo el archivo correspondiente y corriendo el siguiente comando:
   ```bash
   python script1.py
   ```
