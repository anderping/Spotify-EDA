__La estructura que he seguido en el código es la siguiente:__

El codigo sigue la siguiente estructura de carpetas dentro del directorio `'src'`:

- `"main.ipynb"`, contiene el desarollo principial del análisis, desde el tratamiento de los datos hasta el EDA. Se puede comenzar la ejecución desde la sección "Feature Enginering", donde se descarga el dataset `tracks_total.csv`, desde "EDA", donde se descarga el dataset `tracks_total_filtrado.csv`, ambos incluidos en el repositorio. O si se prefiere se puede realizar la ejecución completa desde el inicio del notebook descargando previamente los datasets originales ejecutando `dataset_download.py`.

- dentro del directorio `'utils'` están todos los modulos y funciones auxiliares creados para el desarrollo del proyecto:

        - 'dataset_download.py': fichero para realizar la descarga de los datasets utilizados para el análisis.

        - 'functions.py': fichero que contiene ciertas funciones utilizadas en main.ipynb.
        
        - 'spotify_api.py': fichero que contiene las funciones para comunicarse con la API de Spotify.

- dentro del directorio `'data'` están todos los archivos de datos utilizados en el analisis, datasets iniciales y datasets de control creados en ciertos puntos del `'main.ipynb'` para facilitar ejecuciones parciales.

### Sigue los siguientes pasos para ejecutar el programa
1. Si deseas realizar la ejecución completa del notebook,copia el archivo `.env.example` como `.env` en la carpeta raíz y rellena las claves necesarias:

        # Windows command prompt
        copy .env.example .env

        # macOS and Linux terminal
        cp .env.example .env

2. Activa el entorno virtual:

        # Windows command prompt
        .venv\Scripts\activate.bat
    
        # macOS and Linux
        source .venv/bin/activate

3. Si deseas realizar la ejecución completa del notebook, ejecuta el fichero 'dataset_download.py' para descargar los datasets:

        py src/utils/dataset_download.py

4. Abre el fichero `main.ipynb` y ejecuta desde el inicio, desde la sección "Feature Engineering" o "EDA".
