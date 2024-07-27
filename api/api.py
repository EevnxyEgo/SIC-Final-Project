from flask import Flask, jsonify, request
from pymongo import MongoClient
import tensorflow as tf
import numpy as np
import joblib
import logging
from datetime import datetime
from config import get_config

app = Flask(__name__)

# Load konfigurasi from config.py
config = get_config()

# konfigurasi log
logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# konfigurasi MongoDB
mongo_client = MongoClient(config.MONGO_URI)
db = mongo_client['sensor_data']
collection = db['readings']

# Load model and scaler yang sudah dilatih
try:
    model = tf.keras.models.load_model(config.MODEL_PATH)
    scaler = joblib.load(config.SCALER_PATH)
except Exception as e:
    logger.error(f"Error loading model or scaler: {e}")
    raise

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        data = list(collection.find({}, {'_id': 0}))
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error retrieving data: {e}")
        return jsonify({'error': 'Error retrieving data'}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        content = request.json
        temperature = round(content.get('temperature', 0.0), 2)
        humidity = round(content.get('humidity', 0.0), 2)
        airQuality = round(content.get('airQuality', 0.0), 2)
        
        # Validasi tambahan
        if any(val is None for val in [temperature, humidity, airQuality]):
            return jsonify({'error': 'Invalid input data'}), 400

        features = np.array([[temperature, humidity, airQuality]])
        features = scaler.transform(features)
        
        prediction = model.predict(features)
        logger.info(f"Prediction input: {features}")
        logger.info(f"Prediction output: {prediction}")

        asthma_attack = int(prediction[0][0] > 0.5)
        
        # Save data to MongoDB dengan timestamp
        data_to_store = {
            'temperature': temperature,
            'humidity': humidity,
            'airQuality': airQuality,
            'asthma_attack': asthma_attack,
            'timestamp': datetime.utcnow().isoformat()  # untuk melihat data trends
        }
        collection.insert_one(data_to_store)
        
        return jsonify({'asthma_attack': asthma_attack})
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': 'Error during prediction'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
