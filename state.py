import pickle
import os

def save_state(obj, name):
    os.chdir(os.path.dirname(__file__))
    with open(f'{name}_state.pkl', 'xb') as f:
        pickle.dump(obj, f)

def load_state(name):
    os.chdir(os.path.dirname(__file__))
    with open(f'{name}_state.pkl', 'rb') as f:
        return pickle.load(f)