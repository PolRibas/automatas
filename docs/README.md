# Automatas

Este proyecto es un ejemplo de una estructura de proyecto en Python.

## Instalación

```bash
pip install -r requirements.txt
```

# Configuración del Proyecto

El proyecto utiliza un archivo de configuración para centralizar los parámetros y constantes clave.

## Creación de un Entorno Virtual

```bash
source venv/bin/activate
```

## Instalación de Dependencias

```bash
pip install requests beautifulsoup4 selenium playwright
playwright install
```

## Archivo `config.py`

Contiene las siguientes configuraciones:

- **Rutas de directorios:**
  - `DATA_DIR`: Directorio principal de datos.
  - `RAW_DATA_DIR`: Datos sin procesar.
  - `PROCESSED_DATA_DIR`: Datos procesados.
  - `LOG_DIR`: Directorio de logs.
  - `MODEL_DIR`: Directorio de modelos.

- **Parámetros de entrenamiento:**
  - `NUM_EPOCHS`: Número de épocas.
  - `BATCH_SIZE`: Tamaño de lote.
  - `LEARNING_RATE`: Tasa de aprendizaje.

- **Variables de entorno:**
  - `API_KEY`: Clave de API (se carga desde `.env`).

## Uso de Variables de Entorno

Las variables sensibles se manejan mediante el archivo `.env`. Asegúrate de crear este archivo en la raíz del proyecto y añadirlo al `.gitignore`.

Ejemplo de `.env`:

