from setuptools import find_packages, setup
setup(
    name='FileManager',
    packages=find_packages(include=['FileManager']),
    version='0.1.0',
    description='A python library for fast file management',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)