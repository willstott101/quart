import os
import sys

from setuptools import setup, find_packages

if sys.version_info < (3,6):
    sys.exit('Python 3.6 is the minimum required version')

PROJECT_ROOT = os.path.dirname(__file__)

with open(os.path.join(PROJECT_ROOT, 'quart', '__about__.py')) as file_:
    version_line = [line for line in file_ if line.startswith('__version__')][0]

__version__ = version_line.split('=')[1].strip().strip("'").strip('"')

with open(os.path.join(PROJECT_ROOT, 'README.rst')) as file_:
    long_description = file_.read()

INSTALL_REQUIRES = [
    'aiofiles',
    'h11',
    'h2',
    'itsdangerous',
    'jinja2',
    'multidict',
    'sortedcontainers',
]

setup(
    name='Quart',
    version=__version__,
    description="An asyncio web microframework with Flask's API",
    long_description=long_description,
    url='https://github.com/pgjones/quart/',
    author='P G Jones',
    author_email='philip.graham.jones@googlemail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    py_modules=['quart'],
    install_requires=INSTALL_REQUIRES,
    tests_require=INSTALL_REQUIRES + [
        'hypothesis',
        'pytest',
        'pytest-asyncio',
    ],
)