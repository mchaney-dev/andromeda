import pickle
import os
import shutil
import datetime
from git import Repo

def save_model_state(obj, name):
    os.chdir(os.path.dirname(__file__))
    with open(f'{name}_state.pkl', 'xb') as f:
        pickle.dump(obj, f)

def load_model_state(name):
    os.chdir(os.path.dirname(__file__))
    with open(f'{name}_state.pkl', 'rb') as f:
        return pickle.load(f)

def cleanup():
    os.chdir(os.path.dirname(__file__))
    if os.path.exists('andromeda_state.pkl'):
        os.remove('andromeda_state.pkl')
    if os.path.exists('andromeda-latest'):
        shutil.rmtree('andromeda-latest')
    if os.path.exists('logs'):
        shutil.rmtree('logs')

def log(msg, priority='INFO'):
    if not os.path.exists(f'{os.path.dirname(__file__)}/logs'):
        os.mkdir(f'{os.path.dirname(__file__)}/logs')
    os.chdir(f'{os.path.dirname(__file__)}/logs')
    timestamp = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    message = f'{timestamp} - [{priority}]: {msg}'
    if not os.path.exists('andromeda.log'):
        with open('andromeda.log', 'x') as f:
            f.write(message)
        f.close()
    else:
        with open('andromeda.log', 'a') as f:
            f.write(message)
        f.close()
    print(message)