# andromeda

[![windows](https://github.com/mchaney-dev/andromeda/actions/workflows/windows_test.yml/badge.svg)](https://github.com/mchaney-dev/andromeda/actions/workflows/windows_test.yml) [![macOS](https://github.com/mchaney-dev/andromeda/actions/workflows/macos_test.yml/badge.svg)](https://github.com/mchaney-dev/andromeda/actions/workflows/macos_test.yml) [![ubuntu](https://github.com/mchaney-dev/andromeda/actions/workflows/ubuntu_test.yml/badge.svg)](https://github.com/mchaney-dev/andromeda/actions/workflows/ubuntu_test.yml)

Easy longform text generation for creative writing.

## Installation
Install from PyPI:
```
pip install andromeda-nlp
```

## Quickstart
To quickly generate text, try the following:
```
from andromeda import Model

model = Model()
model.generate('The quick brown fox jumped over the lazy dog.')
```
The default model (GPT-Neo with 125M parameters) will be downloaded from Huggingface (or it will be automatically loaded from disk, if it already exists).

The model configuration can be easily changed:
```
model.config.do_sample = True
```
Finally, save the model (changes to the config will be saved as well):
```
model.save()
```


## Documentation

## Goals
- Serve as an easy-to-understand introduction to text generation, even for those with little to no programming experience
- Investigate the efficacy and practicality of using an NLP model for assistance with creative writing
- The package should be modular and expandable; contributions are always encouraged

## To-dos
- ~~Release as pip package~~
- Fully implement training arguments
- Add sample training data for finetuning
- Create a downloader for different default models, including a custom finetuned model
- Complete documentation

## Contributing
To contribute, [look at open issues](https://github.com/mchaney-dev/andromeda/issues), fork the repository and open a pull request with your changes. Or, if you experience an issue, please open one!
