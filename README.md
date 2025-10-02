# Text-to-Audio Converter with Customizable Pauses

This is a Streamlit web application that allows you to upload a text file (.txt) and convert its contents into a single MP3 audio file. The unique feature of this tool is the ability to insert a customizable silent pause between each line of the text.

This is perfect for:

Speech Practice: Giving yourself time to repeat or practice lines.

Script Reading: Adding natural-sounding breaks between dialogue or scenes.

Study Notes: Creating audio flashcards with review time in between points.

✨ Features
Easy File Upload: Accepts standard .txt files.

Custom Pause Duration: Use a slider to set the exact pause length (in seconds) between each line of text.

MP3 Output: Generates a single, combined MP3 file for easy listening and downloading.

In-Browser Playback: Listen to the generated audio directly in the app before downloading.

Progress Tracking: Shows a progress bar while the audio is being processed.

🛠️ Technologies Used
Python

Streamlit: For creating the interactive web application interface.

gTTS (Google Text-to-Speech): To convert each line of text into speech.

Pydub: For audio manipulation (combining audio segments and generating silent pauses).

🚀 Installation and Setup
Prerequisites
You need Python 3.7+ installed on your system.

Additionally, since pydub relies on a separate audio processing library, you need to install FFmpeg on your machine.

Windows: The easiest way is usually via a package manager like Chocolatey (choco install ffmpeg).

macOS: Use Homebrew (brew install ffmpeg).

Linux (Debian/Ubuntu): Use the system package manager (sudo apt update && sudo apt install ffmpeg).

Project Setup
Clone the Repository:

Bash

git clone [YOUR_REPO_URL]
cd [YOUR_REPO_DIRECTORY]
Create and Activate a Virtual Environment (Recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
Install Dependencies:

Bash

pip install -r requirements.txt
(Note: If you don't have a requirements.txt yet, create one by running pip freeze > requirements.txt after installing the packages or manually create it with the following contents:)

streamlit
gTTS
pydub
🏃 How to Run the App
Make sure your virtual environment is active and all dependencies (including FFmpeg) are installed.

Run the Streamlit app from your terminal:

Bash

streamlit run app_name.py
(Replace app_name.py with the actual name of your Python file, e.g., text_to_audio_converter.py)

The app will automatically open in your web browser, usually at http://localhost:8501.

⚙️ How to Use the App
Upload Your Text File: Click the "Choose a .txt file" button and upload your file. The text will be processed line-by-line.

Review Content: A preview of the file content will be displayed.

Set Pause Duration: Use the slider to select the pause duration between lines, from 0.5 to 5.0 seconds.

Generate Audio: Click the "Generate Audio 🎧" button. The app will process the file, and a progress bar will show the conversion status.

Play and Download: Once complete, an audio player will appear, allowing you to listen to the result. You can then click the "Download Audio File (.mp3)" button to save the file to your computer.

🤝 Contributing
Contributions are welcome! Feel free to open an issue for bug reports or feature requests.

📝 License
This project is licensed under the MIT License - see the LICENSE.md file for details.
