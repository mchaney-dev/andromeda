from transformers import AutoTokenizer, GPTNeoForCausalLM, AutoConfig, pipeline
import os
import random
from torch import cuda


class Andromeda:
    def __init__(self):
        self.name = 'andromeda'
        self.version = '0.0.1'
        self.path = f'{os.path.abspath(os.path.dirname(__file__))}/andromeda-latest'
        self.model = GPTNeoForCausalLM.from_pretrained(self.path)
        self.tokenizer = AutoTokenizer.from_pretrained(self.path)
        self.config = AutoConfig.from_pretrained(self.path)
        self.device = 0 if cuda.is_available() else -1
        self.pipeline = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer, config=self.config, device=self.device)

    def generate(self, inputs: str, return_inputs: bool = False, **kwargs):
        generator = self.pipeline
        output = generator(
            text_inputs=inputs,
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
        else:
            return output

    def save(self):
        self.tokenizer.save_pretrained(self.path)
        self.config.save_pretrained(self.path)
        self.model.save_pretrained(self.path)