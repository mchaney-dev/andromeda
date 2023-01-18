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
The [default model](https://huggingface.co/mchaney/andromeda) will be downloaded from Huggingface, unless otherwise specified.

The model configuration can be easily changed:
```
model.config.do_sample = True
```
Finally, save the model (changes to the config will be saved as well):
```
model.save()
```

## Documentation
TBA

## Goals
- Serve as an easy-to-understand introduction to text generation, even for those with little to no programming experience
- Investigate the efficacy and practicality of using an NLP model for assistance with creative writing
- The package should be modular and expandable; contributions are always encouraged

## To-dos
- ~~Initial release as pip package~~
- ~~Fully implement training arguments~~
- ~~Create a downloader for different default models, including a custom finetuned model~~
- Add sample training data for finetuning
- Complete documentation

## Contributing
To contribute, [look at open issues](https://github.com/mchaney-dev/andromeda/issues), fork the repository and open a pull request with your changes. Or, consider opening an issue or requesting a feature.