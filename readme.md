# 🚘 WakeDrive: Real-Time Driver Drowsiness Detection

> Driver Alertness Monitoring Using Deep Learning

---

## 📌 Project Summary

**WakeDrive** was developed to address the critical issue of driver fatigue—a leading cause of road accidents. This system monitors drivers in real-time and detects fatigue indicators such as **yawning** and **eye closures** using advanced deep learning techniques. It integrates custom-trained models into a live video pipeline and generates **multi-level alerts** to help prevent accidents.

This is a complete end-to-end pipeline, from data collection and preprocessing to model training, evaluation, and **real-time deployment** using **OpenCV** and **multithreading**.

---

## 🏷️ Industry Tags

- Automotive Safety
- Computer Vision
- Driver Monitoring Systems
- Deep Learning
- Real-Time Applications

---

## 🧰 Tech Stack

- **Frameworks:** TensorFlow, Keras
- **Language:** Python
- **Computer Vision:** OpenCV
- **Model Architecture:** EfficientNetB0
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Python Multithreading
- **Audio Alerts:** Python `winsound` module

---

## 🚨 Problem Statement

Driver fatigue detection systems often lack **real-time performance**, robustness to varying **lighting conditions**, and accurate alert mechanisms.

Key objectives:

- Accurately detect **yawns** and **eye closures**
- Ensure robustness across facial variations and lighting
- Generate **timely, multi-level alerts** for the driver

---

## ✅ Solution Outline

### 📂 Data Preparation

- **Custom Dataset:** Yawn/No Yawn and Open/Closed Eyes
- **Preprocessing:**
  - Resize to 224x224
  - Augmentation for generalization
  - Dataset Split: 80% Train, 10% Validation, 10% Test

### 🤖 Model Training

- **Base Model:** EfficientNetB0 (pretrained on ImageNet)
- **Custom Layers:** BatchNorm, Dropout, Dense
- **Training Details:**
  - Optimizer: `Adamax`
  - Loss: `CategoricalCrossentropy`
  - Metrics: Accuracy
  - Epochs: 5
- **Evaluation:** Confusion matrix, classification report

### 🧠 System Design

- **Face & Eye Detection:** Haar Cascade classifiers
- **Model Integration:** TensorFlow models
- **Multithreading:** Simultaneous face, eye, and yawn detection

### 🔔 Alert Levels

| Level   | Trigger                         | Alert Sound         |
| ------- | ------------------------------- | ------------------- |
| Level 1 | Slight fatigue (e.g., blinking) | Low-frequency beep  |
| Level 2 | Moderate fatigue                | Mid-frequency beep  |
| Level 3 | Severe fatigue                  | High-frequency beep |

---

## 🎯 Features

1. **Real-Time Yawn Detection**
2. **Eye State Classification (Open/Closed)**
3. **Multithreading for Low Latency**
4. **Multi-Level Alert System**
5. **Live Overlay of Predictions**
6. **Scalable Architecture** (e.g., add head-nod detection)

---

## 📈 Model Performance

| Metric              | Eye Detection | Yawn Detection |
| ------------------- | ------------- | -------------- |
| Validation Accuracy | 92%           | 91%            |
| Test Accuracy       | > 90%         | > 90%          |

---

## 💡 Challenges & Solutions

| Challenge                                     | Solution                                  |
| --------------------------------------------- | ----------------------------------------- |
| Poor lighting conditions                      | Data augmentation + pretrained models     |
| Real-time latency                             | Multithreading to parallelize detection   |
| Distinguishing blinks from prolonged closures | Time-based thresholds for better accuracy |

---

## 🚀 How to Set Up the Project

### 1. Clone the Repository

````bash
git clone https://github.com/yourusername/WakeDrive-Drowsiness-Detection.git
cd WakeDrive-Drowsiness-Detection


## 🚀 How to Set Up the Project

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/WakeDrive-Drowsiness-Detection.git
cd WakeDrive-Drowsiness-Detection
````

### 2. (Optional but recommended) Create a Virtual Environment

```bash
python -m venv fyp_env
# Activate virtual environment
# On Windows:
fyp_env\Scripts\activate
# On Unix/macOS:
source fyp_env/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the System

Open and run any of the following for testing:

- `Finalized_FYP_CODE.ipynb`
- `human-eyes-detection-open-close_Final.ipynb`
- `human-mouth-detection-yawn-no_yawn_Final.ipynb`

> Ensure the `model/` directory contains the trained EfficientNetB0 models.

---

## 🎁 Deliverables

- Trained Models: Eye state & yawn detection
- Detection Pipeline: Python + OpenCV + winsound
- Performance Reports
- 📽️ Demo Video: `RTDDD_Demo.mkv`
- Full Technical Documentation

---

## 💼 Client Impact

- **Proactive Safety:** Reduces accident risk due to drowsiness
- **Fast Detection:** Real-time with minimal lag
- **Low Hardware Requirements:** Works on lightweight setups
- **Positive UX:** Clear visuals + intuitive alerts = happy users

---

## ✅ Conclusion

WakeDrive is a reliable and scalable system designed to ensure safer driving experiences through deep learning and real-time detection. Its practical architecture and high accuracy make it ready for deployment in modern vehicles.

> **“Safer roads through smarter tech.”**

---
