# andromeda v1.0.1

[![build](https://github.com/mchaney-dev/andromeda/actions/workflows/test_build.yml/badge.svg)](https://github.com/mchaney-dev/andromeda/actions/workflows/test_build.yml) [![release](https://github.com/mchaney-dev/andromeda/actions/workflows/test_release.yml/badge.svg)](https://github.com/mchaney-dev/andromeda/actions/workflows/test_release.yml) [![docs](https://readthedocs.org/projects/andromeda-nlp/badge/?version=latest)](https://andromeda-nlp.readthedocs.io/en/latest/?badge=latest)

Easy longform text generation.

## Installation
Install from PyPI:
```
pip install andromeda-nlp
```

## Documentation
Read the documentation for this project [here](https://andromeda-nlp.readthedocs.io/en/latest/).

## Goals
- Serve as an easy-to-understand introduction to text generation, even for those with little to no programming experience
- The package should be modular and expandable; contributions are always encouraged

## Contributing
To contribute, [look at open issues](https://github.com/mchaney-dev/andromeda/issues), fork the repository and open a pull request with your changes. If you experience a bug or would like a feature to be added, please feel free to open an issue.
### Managing Dependencies
#### Installing Poetry
This project makes use of Poetry as a build backend and dependency management system. After cloning the repository, follow [these instructions](https://python-poetry.org/docs/#installation) to get Poetry up and running on your system. Use `poetry --version` to confirm installation.

#### Installing Project Dependencies
Navigate to the location of your locally cloned repository. To install all dependencies listed in the `pyproject.toml` file at the root of this repository, use:
```
poetry install
```
You should then be ready to make your desired changes and open a pull request.

## Roadmap
- [x] Add base features (ability to save/load model, change model configuration, training and eval utilities)
- [ ] Add utility functions for running the package in a Google Colab instance
- [ ] Add visualizers for training and evaluation
- [ ] Add live Google Colab demo to documentation
