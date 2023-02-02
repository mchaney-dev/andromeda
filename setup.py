from setuptools import setup
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))
with open('./README.md', 'r') as f:
    description = f.read()

setup_args = dict(
    name='andromeda-nlp',
    version='1.0.0',
    author='mchaney-dev',
    keywords=['nlp', 'natural language processing', 'text generation', 'python', 'pytorch'],
    packages=['andromeda'],
    description='Easy longform text generation for creative writing.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/mchaney-dev/andromeda',
    license='MIT'
)

install_requires = [
    'torch',
    'happytransformer',
    'shutil',
    'datetime'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)