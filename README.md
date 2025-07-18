# AI-Desktop-Voice-Assistant

A smart, voice-enabled AI desktop assistant built in Python that can understand natural language commands, perform various desktop tasks, respond intelligently using a trained neural network model, and assist in day-to-day productivity tasks.

# Features:

Voice Command Recognition (via speech_recognition)

Speech Response (via pyttsx3)

NLP Chatbot using a custom-trained ANN (Keras)

Schedule Reminders with contextual greetings (day + time-based)

Web Automation (Google search, opening social media platforms)

Contextual Q&A using trained intents and label encoder

Open/Close Apps: Calculator, Notepad, Paint, etc.

Volume Control through voice commands

System Monitoring: CPU usage, Battery percentage

Real-time Social Media Access: Facebook, WhatsApp, LinkedIn, Instagram, Discord


# Technologies & Libraries Used:

Python 3.x

TensorFlow / Keras – Neural network for intent classification

SpeechRecognition – Captures and interprets voice input

Pyttsx3 – Text-to-speech voice response

Scikit-learn – Label encoding

Pickle / JSON – Model and intent storage

Webbrowser – Automate browser-based tasks

PyAutoGUI – System volume control

Psutil – CPU & battery monitoring

ElevenLabs API (optional) – For realistic TTS voice (commented out in base version)


# Project Structure:
AI_Assistant/
    api_key.py # For Real Voice
    
    chat_model.h5 # Trained Keras model
    
    intents.json # NLP intents and responses
    
    label_encoder # Label encoder for intents
    
    main.py # Main Python Script
    
    model_test.py # Test the Model 
    
    model_train.py # Trained the Model
    
    requirements.txt # Dependencies Required
    
    tokenizer.pkl # Tokenize the Word


# How it Works:

The assistant listens for a command.

Converts speech to text using Google's Speech Recognition.

If it's a general command (like opening apps, checking system), it executes directly.

If it's a natural question (who, what, etc.), it sends it to the trained neural network to classify intent and respond.

Uses TTS (Text-to-Speech) to reply audibly.
