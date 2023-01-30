import setuptools

setuptools.setup(
    name='andromeda-nlp',
    version='0.1.2',
    description='Easy longform text generation for creative writing.',
    long_description='Easy longform text generation for creative writing.',
    author='mchaney-dev',
    author_email='mchaneydev@gmail.com',
    url='https://github.com/mchaney-dev/andromeda',
    requires=['torch', 'happytransformer', 'shutil', 'datetime', 'typing'],
    license='MIT'
)