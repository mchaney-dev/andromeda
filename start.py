from state import save_state, load_state
from model import Andromeda
import os

print('Initializing...')
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if not os.path.exists('andromeda_state.pkl'):
    andromeda = Andromeda()
    save_state(andromeda, 'andromeda')
print('Loading model state...')
andromeda = load_state('andromeda')
print('Done.')
