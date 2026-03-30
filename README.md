# 🕵️‍♂️ Image Forgery Detection System

A deep learning-powered web application designed to detect forged or tampered images. This project leverages Convolutional Neural Networks (CNNs) to analyze image patterns and classify them as **authentic** or **tampered**.

Built using **Flask** for the backend and **TensorFlow/Keras** for model inference, the system provides a simple and interactive interface for users to upload images and receive real-time analysis.

---

## 🚀 Features

- 🔍 Detects image forgery using a trained CNN model  
- 📤 Upload image via web interface  
- ⚡ Real-time prediction (authentic vs tampered)  
- 📊 Confidence score for predictions  
- 🖼️ Optional heatmap visualization (for tampered regions)  
- 🌐 Lightweight Flask-based deployment  

---

## 🧠 How It Works

1. User uploads an image through the web interface  
2. The image is preprocessed (resized, normalized, formatted)  
3. The trained CNN model performs inference  
4. Output is classified into:
   - ✅ Authentic  
   - ❌ Tampered  
5. Results (with confidence score) are displayed to the user  

---

## 🏗️ Tech Stack

### 🔹 Backend
- Flask (Python)
- TensorFlow / Keras

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Model
- Convolutional Neural Network (CNN)
- Binary Classification (Authentic vs Tampered)
