# ✋ Hand Gesture Recognition using OpenCV & MediaPipe

## 📌 Overview

This project performs **real-time hand gesture recognition** using your webcam. It uses MediaPipe to detect hand landmarks and OpenCV to process video frames, allowing recognition of simple hand gestures.

Recognized gestures include:

* ✊ Fist
* 👍 Thumbs Up
* ☝️ One
* ✌️ Peace
* ✋ Open Hand

---

## 🚀 Features

* Real-time hand tracking
* Detects left and right hands
* Fast and lightweight (no heavy ML model required)
* Easy to run and modify
* Supports external/mobile cameras

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe

---

## 📂 Project Structure

Hand-Gesture-Recognition
│── main.py
│── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/yashtambeml/PRODIGY_ML_TASK04.git
cd hand-gesture-recognition

### 2️⃣ Install dependencies

pip install opencv-python mediapipe

---

## ▶️ Usage

Run the project:
python main.py

### 🎮 Controls

* Press **ESC** to exit the application

---

## 📷 How It Works

1. Captures video from webcam
2. Flips frame for mirror view
3. Converts image to RGB
4. Detects hand landmarks using MediaPipe
5. Identifies which fingers are open/closed
6. Classifies gesture based on finger positions

---

## 🧠 Gesture Logic

Each finger is represented as:

* 1 → Open
* 0 → Closed

Examples:

* [1, 1, 1, 1, 1] → Open Hand
* [0, 0, 0, 0, 0] → Fist
* [1, 0, 0, 0, 0] → Thumbs Up

## ⚠️ Troubleshooting

### ❌ Gesture detection not accurate

* Ensure proper lighting
* Keep hand fully visible
* Avoid cluttered background
* Keep camera steady

---

## 🔮 Future Improvements

* Add more gestures
* Use deep learning model for better accuracy
* Add gesture-based system controls
* Multi-hand detection support

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Yash Tambe
Machine Learning Enthusiast 🚀
