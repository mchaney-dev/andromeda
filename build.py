from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, pipeline
import os

class Model:
    def __init__(self, model_name: str, version: str = 'latest'):
        self.tokenizer = AutoTokenizer.from_pretrained(f'{model_name}')
        self.model = AutoModelForCausalLM.from_pretrained(f'{model_name}')
        self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)
        self.name = self.generator.model.config.name_or_path
        self.config = AutoConfig.from_pretrained(f'{model_name}')
        self.version = version

    def generate(self, inputs: str, num_workers: int = 1, batch_size: int = 1, return_inputs: bool = False, **kwargs):
        output = self.generator(text_inputs=inputs, num_workers=num_workers, batch_size=batch_size)
        output = output[0]['generated_text']
        if not return_inputs:
            if output.startswith(inputs):
                output = output[len(inputs):]
            return output
        else:
            return output

    def save(self, path: str):
        self.tokenizer.save_pretrained(path)
        self.config.save_pretrained(path)
        self.model.save_pretrained(path)

model = Model('EleutherAI/gpt-neo-125M')
cwd = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if not os.path.exists(f'{cwd}/checkpoints'):
    os.mkdir(f'{cwd}/checkpoints')
if not os.path.exists(f'{cwd}/checkpoints/andromeda-{model.version}'):
    os.mkdir(f'{cwd}/checkpoints/andromeda-{model.version}')
model.save(f'{cwd}/checkpoints/andromeda-{model.version}')