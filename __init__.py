from utils import save_model_state, load_model_state, log
from model import Model
import os

log('Initializing...')
os.chdir(os.path.abspath(os.path.dirname(__file__)))
if not os.path.exists('andromeda_state.pkl'):
    andromeda = Model()
    log('Saving model state...')
    save_model_state(andromeda, 'andromeda')
    log('Done.')
log('Loading model state...')
andromeda = load_model_state('andromeda')
log('Done.')