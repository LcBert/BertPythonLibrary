from setuptools import find_packages, setup

setup(
    name='BotAI',
    packages=find_packages(include=["BotAI"]),
    version='0.1.0',
    description='',
    author='Me',
    license='MIT',
    install_requires=["openai"],
)