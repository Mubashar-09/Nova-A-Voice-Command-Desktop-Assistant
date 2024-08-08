import sqlite3

def create_database():
    conn = sqlite3.connect('commands.db')
    c = conn.cursor()

    # Drop the table if it exists
    c.execute('''DROP TABLE IF EXISTS commands''')

    # Create the table
    c.execute('''CREATE TABLE commands
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  Command_Name TEXT NOT NULL,
                  Action TEXT NOT NULL,
                  Description TEXT)''')

    # Prepopulate the table with existing commands
    commands = [
        ('time', 'get_time()', 'Get the current time'),
        ('date', 'get_date()', 'Get the current date'),
        ('weather', 'get_weather_update()', 'Get the current weather update'),
        ('open notepad', 'os.startfile("C:\\\\Windows\\\\System32\\\\notepad.exe")', 'Open Notepad'),
        ('open ms word', 'os.startfile("C:\\\\Program Files\\\\Microsoft Office\\\\Office14\\\\WINWORD.EXE")', 'Open MS Word'),
        ('open ms excel', 'os.startfile("C:\\\\Program Files\\\\Microsoft Office\\\\Office14\\\\EXCEL.EXE")', 'Open MS Excel'),
        ('open powerpoint', 'os.startfile("C:\\\\Program Files\\\\Microsoft Office\\\\Office14\\\\POWERPNT.EXE")', 'Open MS PowerPoint'),
        ('open this pc', 'self.open_this_pc()', 'Open This PC'),
        ('start typing', 'self.voice_typing()', 'Start voice typing'),
        ('save this file', 'self.save_word_document()', 'Save the current document'),
        ('copy', 'self.copy_text()', 'Copy selected text'),
        ('paste', 'self.paste_text()', 'Paste copied text'),
        ('select all', 'self.select_all()', 'Select all text'),
        ('delete', 'self.delete_text()', 'Delete selected text'),
        ('rename file', 'self.rename_file()', 'Rename a file'),
        ('select file', 'self.select_file()', 'Select a file'),
        ('create new folder', 'self.create_new_folder()', 'Create New Folder'),
        ('press enter', 'self.press_enter()', 'Press Enter'),
        ('play music', 'self.play_music()', 'Play music'),
        ('open google', 'self.open_google()', 'Open Google and search'),
        ('open youtube', 'pywhatkit.playonyt("{query}")', 'Open YouTube'),
        ('open facebook', 'webbrowser.open("https://www.facebook.com")', 'Open Facebook'),
        ('open stack overflow', 'webbrowser.open("https://stackoverflow.com")', 'Open Stack Overflow'),
        ('open github', 'webbrowser.open("https://github.com")', 'Open GitHub'),
        ('open instagram', 'webbrowser.open("https://www.instagram.com")', 'Open Instagram'),
        ('wikipedia', 'self.search_wikipedia()', 'Search on Wikipedia'),
        ('screenshot', 'self.screenshot()', 'Take a screenshot'),
        ('shutdown', 'os.system("shutdown /s /t 1")', 'Shut down the system'),
        ('restart', 'os.system("shutdown /r /t 1")', 'Restart the system'),
        ('sleep', 'os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")', 'Put the system to sleep'),
        ('commands', 'self.open_commands_window()', 'Open command management window'),
        ('exit', 'sys.exit()', 'Exit the application'),
        ('close notepad', 'os.system("taskkill /f /im notepad.exe")', 'Exit Notepad'),
        ('close ms word', 'os.system("taskkill /f /im WINWORD.exe")', 'Exit MS Word'),
        ('close ms excel', 'os.system("taskkill /f /im excel.exe")', 'Exit MS Excel'),
        ('close powerpoint', 'os.system("taskkill /f /im powerpoint.exe")', 'Exit PowerPoint'),
        ('stop the music', 'os.system("taskkill /f /im MPC-HC64.exe")', 'Stop Music'),
        ('close google', 'os.system("taskkill /f /im chrome.exe")', 'Exit Google')
    ]

    c.executemany('INSERT INTO commands (Command_Name, Action, Description) VALUES (?, ?, ?)', commands)

    conn.commit()
    conn.close()

def get_commands():
    conn = sqlite3.connect('commands.db')
    c = conn.cursor()
    c.execute('SELECT Command_Name, Action, Description FROM commands')
    commands = c.fetchall()
    conn.close()
    return commands

def save_commands(commands):
    conn = sqlite3.connect('commands.db')
    c = conn.cursor()
    c.execute('DELETE FROM commands')
    c.executemany('INSERT INTO commands (Command_Name, Action, Description) VALUES (?, ?, ?)', commands)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database and table created successfully.")
    commands = get_commands()
    for command in commands:
        print(command)
