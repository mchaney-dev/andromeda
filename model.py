from transformers import AutoTokenizer, GPTNeoForCausalLM, AutoConfig, pipeline, Trainer, TrainingArguments, AutoModelForCausalLM
import os
from torch import cuda


class Andromeda:
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
            os.mkdir(f'{self.path}/logs')
            self.model = AutoModelForCausalLM.from_pretrained('EleutherAI/gpt-neo-125M')
            self.tokenizer = AutoTokenizer.from_pretrained('EleutherAI/gpt-neo-125M')
            self.config = AutoConfig.from_pretrained('EleutherAI/gpt-neo-125M')
            self.save()
        else:
            self.model = GPTNeoForCausalLM.from_pretrained(f'{cwd}/andromeda-latest')
            self.tokenizer = AutoTokenizer.from_pretrained(f'{cwd}/andromeda-latest')
            self.config = AutoConfig.from_pretrained(self.path)
        self.device = 0 if cuda.is_available() else -1
        self.pipeline = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, config=self.config, device=self.device)

    def generate(self, inputs: str, return_inputs: bool = False, **kwargs):
        generator = self.pipeline
        output = generator(
            text_inputs=inputs,
            do_sample=True,
            max_new_tokens=self.config.max_length,
            temperature=self.config.temperature,
            top_k=self.config.top_k,
            top_p=self.config.top_p,
            bad_words_ids=self.config.bad_words_ids,
            repetition_penalty=self.config.repetition_penalty,
            length_penalty=self.config.length_penalty,
            **kwargs
            )
        output = output[0]['generated_text']
        if not return_inputs:
            if output.startswith(inputs):
                output = output[len(inputs):]
        return output

    def save(self):
        self.tokenizer.save_pretrained(self.path)
        self.config.save_pretrained(self.path)
        self.model.save_pretrained(self.path)
