import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='k2_registry',
    version='0.0.1',
    author_email='simon.emmott@yahoo.co.uk',
    author='Simon Emmott',
    description='Simple registry framework',
    packages=['k2', 'k2.registry', 'tests'],
    long_description=read('README.md')
)