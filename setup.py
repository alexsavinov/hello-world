from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='book library',
    version='1.0',
    url='https://github.com/alexsavinov/hello-world',
    author='Alexey Savinov',
    author_email='savinov.alexey@gmail.com',
    platforms='any',
    license='BSD',
    description=(
        'The simple book library management system.'
    ),
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
)