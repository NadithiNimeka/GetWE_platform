# 🌟 Deep Learning approuch to

![GetWE Web](https://nadithinimeka.github.io/GetWE_platform/)  
![GitHub Repo](https://github.com/NadithiNimeka/GetWE_platform.git)  
![Dataset](https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset)  
---

## 🚀 Overview

**A Deep Learning Approach to Hate Speech Detection: Leveraging BiLSTM and Contextual Word Embeddings** is a cutting-edge social media platform designed to promote safer online interactions by leveraging **Deep learning** for hate speech detection. using contextual word embeddings together with a bidirectional LSTM architecture can successfully classify social media comments with 88% accuracy into three categories: hate speech, offensive language, and neutral. Accuracy, reliability, and practical use were achieved through a modular pipeline that included data ingestion, text normalization, tokenization, sequence standardization, model training, and inference. 

### Key Features
- **Hate Speech Detection with DL**: using hatespeech and offensive dataset created A neural network using Keras(`project01.ipynb`) and Used the trained Keras model (`Keras_Hatespeech_model.h5`) converted to TensorFlow.js for real-time hate speech detection in posts and comments.
- **Social Media Dashboard**: Includes comment, like, and share functionalities with "For You" and "Following" feeds, user profiles, trending topics, and a "Who to Follow" section.
- **Rule-Based Fallback**: A comprehensive list of offensive words ensures robust hate speech detection even without the ML model.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Deep Learning**:
  - **Jupiter Notebook** : `project01.ipynb` containing all the model building (Taining ad Testing)
  - **Model**: Pre-trained Keras model (`Keras_Hatespeech_model.h5`) converted to TensorFlow.js for web deployment.
  - **Vocabulary**: `hate_comment_detection.json` for tokenizing text input.
  - **Inference**: TensorFlow.js (`tf.min.js`) for real-time hate speech prediction.
- **Main Libraries**:
  - TensorFlow
  - Keras
- **Deployment**: Compatible with GitHub Pages or local servers

---

## ⚙️ Setup Instructions

### Prerequisites
- A modern web browser (Chrome, Edge, Firefox, etc.)
- Python/ Jupiter Notebook(to run a local server)

### Steps to Run the model

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NadithiNimeka/GetWE_platform.git
   ```
2. **Open the Project01.ipynb jupiternotebook file in the codespace**

3. **Change the datasets File path on column 2**

4. **Choose a Python Evironment and run the code**


### Steps to Run the UI Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SocialDetect-Dashboard.git
   ```
2. **Run a Local Server**:
   ```bash
   python -m http.server 8000
   ```
3. **Open in Browser**:
   - Navigate to `http://localhost:8000/index.html`.

### Running on Web
- The app is hosted on GitHub Pages: [GetWE-Dashboard Live](https://nadithinimeka.github.io/GetWE_platform/).
- Simply visit the link to use the app directly in your browser.

### Running on Android
- Scan the QR code with Expo Go on your Android device (if hosted locally).
---

## 🌐 Features in Detail

### 1. **Hate Speech Detection with Machine Learning**
- **Model**: Utilizes a Keras model trained on a hate speech dataset (`labeled_data.csv`) to classify text as hate speech, offensive, or neutral.
- **Conversion**: Converted to TensorFlow.js format (`tfjs_model/model.json`) for web deployment using `convert_model.py`.
- **Rule-Based Fallback**: Includes an extensive list of offensive words for robust detection if the ML model isn’t used.
- **Implementation**: Real-time detection for both posts and comments, blocking offensive content with user-friendly alerts.

### 2. **Social Media Dashboard**
- **Feeds**: Toggle between "For You" and "Following" feeds to view posts.
- **User Interaction**: Post creation, commenting, liking, and sharing (share functionality placeholder for future implementation).
- **User Profiles**: View user details, follower counts, and recent posts in a modal.
- **Trending Topics**: Displays trending hashtags with post counts for engagement.
---

## 🧠 Machine Learning Details

### Model Training
- **Dataset**: Originally trained on `labeled_data.csv` (not included in the repo) with labeled hate speech data.
- **Preprocessing**: Text tokenization using Keras `Tokenizer`, saved as `hate_comment_detection.json`.
- **Model Architecture**: A deep learning model built with Keras, converted to TensorFlow.js for web inference.
- **Inference**: Uses TensorFlow.js to predict hate speech in real-time on the client side.

---
