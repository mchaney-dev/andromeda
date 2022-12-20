from happytransformer import HappyGeneration, GENSettings, GENTrainArgs, GENEvalArgs
import os
from .utils import log

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
        log('Loading model...')
        self.model = HappyGeneration(model_type='GPT-NEO', model_name='EleutherAI/gpt-neo-125M', load_path=self.path)
        self.train_args = GENTrainArgs()
        self.eval_args = GENEvalArgs()
        self.config = GENSettings()
        log('Done.')

    def train(self, input_filepath: str):
        log(f'Training {self.name} v{self.version} on {input_filepath} with arguments: {self.train_args}')
        return self.model.train(input_filepath, args=self.train_args)

    def evaluate(self, input_filepath: str):
        log(f'Evaluating {self.name} v{self.version} on {input_filepath} with arguments: {self.eval_args}')
        return self.model.eval(input_filepath, args=self.eval_args)

    def generate(self, text: str):
        log(f'Generating text with {self.name} v{self.version} with configuration: {self.config}')
        return self.model.generate_text(text, args=self.config)

    def save(self):
        log(f'Saving {self.name} v{self.version}...')
        self.model.save(self.path)
        log('Done.')