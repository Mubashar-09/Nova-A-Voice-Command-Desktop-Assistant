import sys
import time
import pyautogui
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import webbrowser
import wikipedia
import pywhatkit
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import QThread, QTimer, QTime, QDate, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from novaui import Ui_novagui
import spacy
import database
from commands import Ui_command_screen  # Import the new UI class for commands

# Load SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Communicate(QtCore.QObject):
    text_changed = pyqtSignal(str)


# Create an instance of the communication class
comm = Communicate()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    comm.text_changed.emit(audio)


# Function to get the current time
def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    time_message = f"The current time is {current_time}"
    speak(time_message)


def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    date_message = f"Current date is {current_date}"
    speak(date_message)


# Function to get weather update
def get_weather_update():
    api_key = 'your_apikey'
    city_name = 'your city'
    country_code = 'CC'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}&uni,s=metric'

    response = requests.get(u6rl)
    if response.status_code == 200:
        weather_data = response.json()
        weather_update = f"The weather in Sahiwal, Pakistan is {weather_data['weather'][0]['description']} with a temperature of {weather_data['main']['temp']}°C. Humidity is {weather_data['main']['humidity']}% and wind speed is {weather_data['wind']['speed']} m/s."
        speak(weather_update)
    else:
        speak("Failed to retrieve weather data.")


# Greeting function
def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good morning sir")
    elif 12 <= hour < 18:
        speak("Hello, Good afternoon sir")
    else:
        speak("Hello, Good evening sir")
    speak("I am Nova, A voice command desktop assistant. How can I help you?")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.typing = False
        self.commands = database.get_commands()

    def run(self):
        self.taskexecution()

    # Voice into text
    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300 
            r.dynamic_energy_threshold = True
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=7)  # Add timeouts to prevent hanging
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}")
                return query.lower()
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                speak("Listening timed out, please try again.")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                speak("Sorry, I could not understand that. Please try again.")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                speak("Network error, please try again.")
                return ""

    def search_wikipedia(self):
        speak("What would you like to search on Wikipedia?")
        search_query = self.take_command()
        query = search_query.replace("wikipedia", "")
        speak("Searching Wikipedia...")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        except wikipedia.DisambiguationError as e:
            print(e.options)
            speak("Can you be more specific?")
        except wikipedia.exceptions.PageError:
            print("No Result Found")
            speak("No Result Found")

    def process_text(self, text):
        doc = nlp(text)
        processed_text = []

        for token in doc:
            if token.text.lower() in ["comma", "full stop"]:
                if token.text.lower() == "comma":
                    processed_text.append(",")
                else:
                    processed_text.append(".")
            elif token.text.lower() in ["new line", "enter"]:
                processed_text.append("\n")
            else:
                processed_text.append(token.text)

        return " ".join(processed_text)

    def voice_typing(self):
        speak("Voice typing started. Please speak your text.")
        self.typing = True
        while self.typing:
            command = self.take_command()
            if "stop typing" in command:
                speak("Voice typing stopped.")
                self.typing = False
            else:
                processed_command = self.process_text(command)
                pyautogui.write(processed_command)

    def save_word_document(self):
        speak("Please provide a name for the document.")
        file_name = self.take_command().replace(" ", "_")  # Replaces spaces with underscores for file names
        if file_name:
            # Simulate saving the document with keyboard shortcuts
            pyautogui.hotkey("ctrl", "s")
            time.sleep(1)  # Wait for the save dialog to open
            pyautogui.write(file_name)
            pyautogui.press("enter")
            time.sleep(1)  # Wait for the save process to complete
            speak("Document has been saved.")

    def open_google(self):
        speak("What should I search on Google, sir?")
        search_query = self.take_command()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    def screenshot(self):
        speak("Please tell me the name for this file")
        file_name = self.take_command().lower()
        path = "C:/Users/Hafiz/Pictures/Screenshots/"
        file_path = f"{path}{file_name}.png"
        speak("Please wait a moment...")
        time.sleep(3)
        image = pyautogui.screenshot()
        image.save(file_path)
        speak("Screenshot has been taken and saved successfully.")

    def play_music(self):
        speak("Playing music")
        music_dir = "E:\\Music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))

    # Function to copy text
    def copy_text(self):
        speak("Copying text")
        pyautogui.hotkey("ctrl", "c")

    # Function to paste text
    def paste_text(self):
        speak("Pasting text")
        pyautogui.hotkey("ctrl", "v")

    # Function to select all text
    def select_all(self):
        speak("Selecting all items")
        pyautogui.hotkey("ctrl", "a")

    def create_new_folder(self):
        speak("creating new folder ")
        pyautogui.hotkey("ctrl", "shift", "n")

    # Function to delete selected text
    def delete_text(self):
        speak("selected item has been deleted")
        pyautogui.press("delete")

    # Function to rename a file
    def rename_file(self):
        speak("Please tell me the new name for the file")
        new_name = self.take_command().replace(" ", "_")
        if new_name:
            pyautogui.hotkey("f2")
            pyautogui.write(new_name)
            pyautogui.press("enter")
            speak("File has been renamed")

    # Function to select a file with a specific name in the open dialog
    def select_file(self, file_name):
        if file_name:
            pyautogui.write(file_name)
            speak(f"File {file_name} selected")

    def press_enter(self):
        pyautogui.press("enter")

    def open_this_pc(self):
        speak("Opening This PC")
        os.startfile("::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")

    def taskexecution(self):
        wish()
        while True:
            self.query = self.take_command()

            if 'stop listening' in self.query or 'goodbye' in self.query:
                speak("Goodbye Sir. If you need you can call me anytime!")
                break

            self.query = self.query.lower()

            # Reload commands from the database to ensure any updates are reflected
            self.commands = database.get_commands()

            for command in self.commands:
                command_name, action, description = command
                if command_name.lower() in self.query:
                    try:
                        exec(action)
                    except Exception as e:
                        speak(f"Failed to execute command: {command_name}. Error: {e}")
                    break


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_novagui()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.startTask)
        self.ui.Exit.clicked.connect(self.close)
        self.ui.ManageCommands.clicked.connect(self.openCommandWindow)
        self.startExecution = MainThread()
        self.timer = QTimer(self)

        # Connect the signal to update the text edit
        comm.text_changed.connect(self.update_terminal)

        # Start a timer to update the time and date display
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)  # Update every second

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images/Orb.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Images/2RNb.gif")
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.startExecution.start()

    def openCommandWindow(self):
        #if self.command_window is None:
            self.command_window = QtWidgets.QMainWindow()
            self.ui_command_screen = Ui_command_screen()
            self.ui_command_screen.setupUi(self.command_window)
            self.command_window.show()

    def showTime(self):
        try:
            current_time = QTime.currentTime()
            current_date = QDate.currentDate()
            label_time = current_time.toString('hh:mm:ss')
            label_date = current_date.toString(Qt.DateFormat.ISODate)  # Corrected line
            self.ui.textBrowser_2.setText(label_time)
            self.ui.textBrowser.setText(label_date)
        except Exception as e:
            print("Error in showTime:", e)

    def update_terminal(self, text):
        self.ui.textEdit.append(text)

    def write(self, text):
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.textEdit.insertPlainText(text)
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)

    def flush(self):
        pass


startExecution = MainThread()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nova = Main()
    nova.show()
    sys.exit(app.exec())
