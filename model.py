from happytransformer import HappyGeneration, GENSettings, GENTrainArgs
import os
from utils import save_model_state, load_model_state, log

class Model(HappyGeneration):
    def __init__(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        os.chdir(cwd)
        self.name = 'andromeda'
        self.version = '0.0.1'
        self.path = f'{cwd}/andromeda-latest'
        if not os.path.exists(self.path):
            log('Initializing...')
            os.mkdir(self.path)
            os.chdir(self.path)
            os.mkdir(f'{self.path}/training')
            os.mkdir(f'{self.path}/training/checkpoints')
            os.mkdir(f'{self.path}/training/data')
            _model = HappyGeneration(model_type='GPT-NEO', model_name='EleutherAI/gpt-neo-125M')
            _model.save(self.path)
            self.model = HappyGeneration(model_type='GPT-NEO', model_name='EleutherAI/gpt-neo-125M', load_path=self.path)
            log('Saving model state...')
            save_model_state(self.model, 'andromeda')
            log('Done.')
        log('Loading model state...')
        self.model = load_model_state('andromeda')
        log('Done.')