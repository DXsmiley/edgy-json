from setuptools import setup, find_packages
# Consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='edgy-json',
    version='0.0.5',
    url='https://github.com/DXsmiley/edgy-json',
    author='DXsmiley',
    author_email='dxsmiley@hotmail.com',
    license='MIT',

    description='Verify JSON like a hipster.',
    long_description=long_description,

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
    ],

    keywords='validate verify json',

    py_modules=["edgy"]
)
