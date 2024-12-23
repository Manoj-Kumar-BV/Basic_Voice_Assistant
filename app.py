from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3
import threading
from datetime import datetime

app = Flask(__name__)
CORS(app)

def speak(text):
    def speak_thread():
        # Initialize a new TTS engine instance for each thread
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=speak_thread).start()

@app.route('/process', methods=['POST'])
def process_command():
    data = request.get_json()
    query = data.get('query', '').strip()

    if not query:
        response = "Please provide a command."
    else:
        query_lower = query.lower()
        if query_lower in ["hello", "hi"]:
            response = "Hello, how can I assist you?"
        elif query_lower == "what is your name":
            response = "I am your personal voice assistant."
        elif query_lower in ["what is the time", "what is the current time"]:
            current_time = datetime.now().strftime("%H:%M")
            response = f"The current time is {current_time}."
        elif query_lower == "what is the weather like":
            response = "I can't check the weather right now, but it's always nice to be prepared!"
        elif query_lower == "tell me a joke":
            response = "This is created using ChatGPT! hahaha, isn't it funny"
        elif query_lower == "how are you":
            response = "I'm just a program, so I don't have feelings, but thanks for asking!"
        elif query_lower == "what can you do":
            response = "I can perform basic tasks like greeting, telling time, and sharing jokes. More features can be added in the future."
        elif query_lower == "who created you":
            response = "I was created by a developer using Flask and Python."
        else:
            response = "Sorry, I didn't understand that command."

    # Speak the response
    speak(response)

    # Return the response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
