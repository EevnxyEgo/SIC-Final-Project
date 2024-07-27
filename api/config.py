import os

class Config:

    MONGO_URI = 'mongodb://localhost:27017/sensor_data'
    MODEL_PATH = 'models/asthma_model.h5'
    SCALER_PATH = 'models/scaler.pkl'
    LOG_LEVEL = 'INFO'
    
# Fungsi yang dipanggil oleh api.py
def get_config():
    config = Config()
    config.MODEL_PATH = os.getenv('MODEL_PATH', config.MODEL_PATH)
    config.SCALER_PATH = os.getenv('SCALER_PATH', config.SCALER_PATH)
    config.MONGO_URI = os.getenv('MONGO_URI', config.MONGO_URI)
    return config
