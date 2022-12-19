from happytransformer import HappyGeneration, GENSettings, GENTrainArgs
import os

class Model(HappyGeneration):
    def __init__(self):
        cwd = os.path.abspath(os.path.dirname(__file__))
        os.chdir(cwd)
        self.name = 'andromeda'
        self.version = '0.0.1'
        self.path = f'{cwd}/andromeda-latest'
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.chdir(self.path)
            os.mkdir(f'{self.path}/training')
            os.mkdir(f'{self.path}/training/checkpoints')
            os.mkdir(f'{self.path}/training/data')
            self.model = HappyGeneration(model_type='GPT-NEO', model_name='EleutherAI/gpt-neo-125M')
            self.model.save(self.path)
        else:
            self.model = HappyGeneration(model_type='GPT-NEO', model_name='EleutherAI/gpt-neo-125M', load_path=self.path)