from happytransformer import HappyGeneration, GENSettings, GENTrainArgs, GENEvalArgs
import os
from typing import Optional
from .utils import log

class Model(object):
    """
    The base class for a text generation model.

    Parameters:
    `model_type` (string): Optional. The type of model to use. Defaults to `GPT-NEO`.
    `model_path` (string): Optional. The path to the model to use. Defaults to `mchaney/andromeda`, the custom model used in development, but can be any model from the HuggingFace model hub, or a path to a local folder containing the model's files.

    Returns a `Model` object.
    """

    def __init__(self, model_type: Optional[str] = 'GPT-NEO', model_path: Optional[str] = 'mchaney/andromeda'):
        cwd = os.path.abspath(os.path.dirname(__file__))
        os.chdir(cwd)
        self.name = 'andromeda'
        self.path = f'{cwd}/andromeda-latest'
        if not os.path.exists(self.path):
            log('Initializing...')
            os.mkdir(self.path)
            os.chdir(self.path)
            os.mkdir(f'{self.path}/training')
            os.mkdir(f'{self.path}/training/checkpoints')
            os.mkdir(f'{self.path}/training/data')
            _model = HappyGeneration(model_type=model_type, model_name=model_path)
            _model.save(self.path)
        log('Loading model...')
        self._model = HappyGeneration(model_type=model_type, model_name=model_path, load_path=self.path)
        self.train_args = GENTrainArgs()
        self.eval_args = GENEvalArgs()
        self.config = GENSettings()
        log('Done.')

    def train(self, input_filepath: str):
        """
        Trains the model. Training arguments can be configured using the `train_args` attribute.

        Parameters:
        `input_filepath` (string): The path to the file containing the training data.

        Returns `None`.
        """

        log(f'Training {self.name} on {input_filepath} with arguments: {self.train_args}')
        return self._model.train(input_filepath, args=self.train_args)

    def evaluate(self, input_filepath: str):
        """
        Evaluates the model. Evaluation arguments can be configured using the `eval_args` attribute.

        Parameters:
        `input_filepath` (string): The path to the file containing the evaluation data.

        Returns `loss` (float).
        """

        log(f'Evaluating {self.name} on {input_filepath} with arguments: {self.eval_args}')
        loss = self._model.eval(input_filepath, args=self.eval_args)
        log(f'Loss: {loss}')
        return loss

    def generate(self, text: str, raw: Optional[bool] = False):
        """
        Generates text using the model. Generation arguments can be configured using the `config` attribute.

        Parameters:
        `text` (string): The text to use as the prompt for the model.
        `raw` (bool): Optional. Whether to return the raw output from the model. Defaults to False.

        Returns the generated text as a string, or the raw output from the model (an object of type `GenerationResult`).
        """

        log(f'Generating text - {self.name} with configuration: {self.config}')
        result = self._model.generate_text(text, args=self.config)
        if not raw:
            return result.text
        else:
            return result

    def save(self):
        """
        Saves the model to disk, overwriting any previously saved files. The model will be saved to the `path` attribute, along with any configuration changes.

        Parameters: None

        Returns `None`.
        """

        log(f'Saving {self.name}...')
        self._model.save(self.path)
        log('Done.')