import os
from setuptools import setup
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='UmbrellaReminder',
    version='0.0.2',
    description=('A Python package which scrapes weather data from google and sends umbrella reminders to specified email at specified time daily. '),
    author= 'Edula Vinay Kumar Reddy',
    url = 'https://github.com/VinayEdula/UmbrellaReminder',
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    packages=setuptools.find_packages(),
    keywords=['weather','Reminder','scraping','Rain Reminder', 'Umbrella Reminder','Weather Reminder'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['UmbrellaReminder'],
    package_dir={'':'src'},
    install_requires = [
        'requests',
        'schedule',
        'beautifulsoup4'
    ]
)