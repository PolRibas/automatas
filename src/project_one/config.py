import os
import yaml
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
print('\nUsing environment:', ENVIRONMENT, '\nFrom the directory:', BASE_DIR,'\n')

config_file = f"config_{ENVIRONMENT}.yaml"
with open(os.path.join(BASE_DIR, config_file), 'r') as f:
    config = yaml.safe_load(f)


DATA_DIR = os.path.join(BASE_DIR, config['paths']['data_dir'])
RAW_DATA_DIR = os.path.join(BASE_DIR, config['paths']['raw_data_dir'])
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, config['paths']['processed_data_dir'])
LOG_DIR = os.path.join(BASE_DIR, config['paths']['log_dir'])
MODEL_DIR = os.path.join(BASE_DIR, config['paths']['model_dir'])

NUM_EPOCHS = config['training']['num_epochs']
BATCH_SIZE = config['training']['batch_size']
LEARNING_RATE = config['training']['learning_rate']

DISKS = config['disks']

API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')


# Crear directorios si no existen
def create_dirs():
    dirs = [RAW_DATA_DIR, PROCESSED_DATA_DIR, LOG_DIR, MODEL_DIR]
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

# Ejecutar la función al importar
create_dirs()