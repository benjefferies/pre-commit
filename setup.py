from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit',
    description='Pre-commit hooks for http://pre-commit.com/.',
    url='https://github.com/benjefferies/pre-commit',
    version='0.0.1',

    author='Ben Jefferies',
    author_email='benjefferies@echosoft.uk',

    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],

    packages=find_packages(include=['commit_msg']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'trello-checker = commit_msg.trello_checker.py:main',
        ],
    },
)
