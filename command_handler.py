# command_handler.py
import sqlite3
import os
import webbrowser
import pywhatkit
import datetime
import wikipedia
import pyautogui
import sys

def get_commands():
    conn = sqlite3.connect('commands.db')
    c = conn.cursor()
    c.execute('SELECT Command_Name, Action, Description FROM commands')
    commands = c.fetchall()
    conn.close()
    return commands

class CommandHandler:
    def __init__(self):
        self.commands = get_commands()

    def execute_command(self, query, context):
        for command in self.commands:
            command_name, action, description = command
            if command_name.lower() in query:
                try:
                    exec(action, globals(), context)
                except Exception as e:
                    print(f"Failed to execute command: {command_name}. Error: {e}")
                break

    def refresh_commands(self):
        self.commands = get_commands()

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(f"The current time is {current_time}")

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"Current date is {current_date}")

def get_weather_update():
    # Placeholder function, you can replace with actual implementation.
    print("Weather update placeholder")

def open_this_pc():
    os.startfile("::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")

def open_google(search_query):
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

def search_youtube(query):
    pywhatkit.playonyt(query)

def search_wikipedia(search_query):
    query = search_query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia:", results)
    except wikipedia.DisambiguationError as e:
        print("DisambiguationError:", e.options)
    except wikipedia.exceptions.PageError:
        print("No Result Found")

def screenshot(file_name):
    path = "C:/Users/Hafiz/Pictures/Screenshots/"
    file_path = f"{path}{file_name}.png"
    image = pyautogui.screenshot()
    image.save(file_path)
    print("Screenshot has been taken and saved successfully.")

# More command functions as needed...
