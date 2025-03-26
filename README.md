__La estructura que he seguido en el código es la siguiente:__

- Dos ficheros .py, "main.py", en el que se ejecuta la interfaz y se llama a la clase Board del fichero "board.py", en el cual se ejecutan los comandos para colocar barcos, comprobar disparos, etc.

- Dos ficheros .py, "main_functions.py", que contiene las constantes y funciones que se llaman en "main.py", y "board_functions.py", que contiene las constantes y functiones que se llaman en "board.py"

- Un fichero "ship_coordinates.json" generado automáticamente en el directorio "src" en el que se guardan las coordenadas de los barcos ya posicionados y las de su alrededor como coordenadas prohibidas.

En cada fichero, en este mismo orden, importo las librerias necesarias, defino las constantes y defino las funciones que se utilizan en el mismo, finalizando con la ejecución de la interfaz en el caso de "main.py" y la definición de la clase en el caso de "board.py".

### Sigue los siguientes pasos para ejecutar el programa 
1. Activa el entorno virtual:

        # Windows command prompt
        .venv\Scripts\activate.bat
    
        # macOS and Linux
        source .venv/bin/activate

2. Ejecuta el programa:

        py src/main.py
