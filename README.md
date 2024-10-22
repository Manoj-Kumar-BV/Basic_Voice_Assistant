---

# Basic Voice Assistant

This project is a simple voice assistant built using Flask, Python, and web technologies. The voice assistant can process spoken commands and provide spoken responses using text-to-speech (TTS) functionality.

## Features

- **Speech Recognition**: Users can speak commands using their microphone.
- **Text-to-Speech**: The assistant responds verbally to user queries.
- **Basic Commands**: Supports limited(can be updated in future) commands such as greeting, telling time, and sharing jokes.

## Technologies Used

- **Flask**: A micro web framework for Python to handle HTTP requests.
- **Pyttsx3**: A text-to-speech conversion library for Python.
- **HTML/CSS**: For the front-end user interface.
- **JavaScript**: For implementing speech recognition in the browser.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Manoj-Kumar-BV/Basic_Voice_Assistant.git
   cd Basic_Voice_Assistant
   ```

2. **Install required packages**:
   You will need to install Flask and Pyttsx3 if you haven't already. Run the following command:
   ```bash
   pip install Flask pyttsx3
   ```

3. **Run the Flask server**:
   Start the Flask application by running:
   ```bash
   python app.py
   ```

4. **Open the application in your browser**:
   Navigate to `http://localhost:5000` (or `copy the path of the index.html file and paste it in your web browser only after running app.py file` in your web browser to access the voice assistant.

## Usage

- Click the microphone button to speak your command.
- The assistant will recognize your speech and respond both on the screen and through audio.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
Feel free to modify or add any sections or features as needed!

---
