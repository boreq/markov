import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='markov',
    version='0.0.0',
    author='boreq',
    author_email='boreq@sourcedrops.com',
    description = ('A markov chain.'),
    license='BSD',
    packages=[
        'markov',
    ],
    long_description=read('README.md'),
    install_requires=[
    ]
)
