# 🧠 Mental Care Website

The Mental Care Website is a comprehensive platform designed to provide mental health support, resources, and services. It offers interactive features such as an AI-powered chatbot, meditation guides, emotion detection, blogs, and professional consultation booking.

---

## 🌐 Overview

Built with **HTML, CSS, JavaScript**, and integrated with:
- 🤖 **Botpress** for the mental health chatbot
- 🧠 **Flask + PyTorch (ResNet18)** for deep learning-based emotion detection

---

## ✨ Features

### 🏠 Home Page
- Engaging UI with a **background video** and interactive layout
- Motivational quote section that updates every few seconds
- Smooth navigation with call-to-action buttons

### 🧰 Mental Health Services
- List of therapy and counseling services
- Book appointments with professionals
- Cards UI for services with descriptions and booking links

### 💬 AI Chatbot (Botpress)
- Intelligent Botpress-based mental health chatbot
- Helps with common queries, resource links, and finding help
- Available 24/7 to assist users

### 😄 Emotion Detection
- **Live Webcam** and **Image Upload** support
- Analyzes facial expressions to detect emotions using:
  - **Flask + PyTorch** (backend model)
- Displays real-time emotion prediction results

### 🧘 Meditation & Relaxation
- Guided meditation videos and music
- Tabs for different meditation techniques (stress, sleep, focus, etc.)
- Mobile-friendly responsive layout

### 📝 Blogs & Stories
- Mental health blogs and inspiring user stories
- Comment system for user engagement
- Helps users gain insights and feel supported

---

## 💻 Run Locally (Emotion Detection with Flask)


### 🧾 Prerequisites

- Python 3.7+
- Git

---


---

### ⚙️ Setup Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mental-health.git
cd mental-health/emotion-detector


### Create and Activate Virtual Environment

# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate



### Install Python Dependencies

pip install -r requirements.txt

### Run Flask App

python app.py
