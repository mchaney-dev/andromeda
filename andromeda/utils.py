import os
import shutil
import datetime

def cleanup() -> None:
    """
    Cleans up all previously generated Andromeda files.

    Returns None.
    """
    os.chdir(os.path.dirname(__file__))
    if os.path.exists('andromeda-latest'):
        shutil.rmtree('andromeda-latest')
    if os.path.exists('logs'):
        shutil.rmtree('logs')

def log(msg, priority='INFO') -> str:
    """
    Logs a message to the console and to a log file located at `andromeda-latest/logs/andromeda.log`, formatted as `MM-DD-YYYY HH:MM:SS - [PRIORITY]: MESSAGE`.

    Returns the message (string).
    """
    if not os.path.exists(f'{os.path.dirname(__file__)}/logs'):
        os.mkdir(f'{os.path.dirname(__file__)}/logs')
    os.chdir(f'{os.path.dirname(__file__)}/logs')
    timestamp = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    message = f'{timestamp} - [{priority}]: {msg}'
    if not os.path.exists('andromeda.log'):
        with open('andromeda.log', 'x') as f:
            f.write(f'{message}\n')
        f.close()
    else:
        with open('andromeda.log', 'a') as f:
            f.write(f'{message}\n')
        f.close()
    print(message)