import setuptools

setuptools.setup(
    name='andromeda-nlp',
    version='0.1.3',
    description='Easy longform text generation for creative writing.',
    long_description='Easy longform text generation for creative writing.',
    author='mchaney-dev',
    author_email='mchaneydev@gmail.com',
    url='https://github.com/mchaney-dev/andromeda',
    install_requires=['torch', 'happytransformer', 'datetime', 'typing'],
    packages=setuptools.find_packages(),
    license_files=['LICENSE']
)