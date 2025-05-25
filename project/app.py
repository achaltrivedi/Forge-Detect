import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

# Upload folder inside static/uploads
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your model (make sure the path is correct relative to your app.py)
MODEL_PATH = "final_casia_model.h5"
model =  tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded.")

# Labels dictionary
labels = {0: 'authentic', 1: 'tampered'}


@app.route('/')
def index():
    # Serve index.html from static folder
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Load and preprocess the image for prediction
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict and prepare response
    prediction = model.predict(img_array)[0][0]
    label_index = int(prediction > 0.5)
    confidence = float(prediction if label_index else 1 - prediction)

    response = {
        'filename': filename,
        'prediction': labels[label_index],
        'confidence': round(confidence * 100, 2)
    }

    return jsonify(response)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Serve uploaded files (images)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # Use debug=False in production
    app.run(debug=True, host='0.0.0.0')

