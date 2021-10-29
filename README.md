# Scraping weather data using Python to receive umbrella reminders 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

## Functionality of the UmbrellaReminder Package

This package contains methods that scrape weather data using Python and sends umbrella reminders to specified email at specified time daily. If the weather condition is rainy or cloudy it will send you an "umbrella reminder" to your email reminding you to pack an umbrella before leaving the house. This package scrapes weather information from Google using bs4 and requests libraries in python.

## Usage

- Make sure you have Python installed in your system.
- Run Following command in the CMD.
 ```
  pip install UmbrellaReminder
  ```


## Example

 ```
from UmbrellaReminder import setumbrellaReminder
setumbrellaReminder("EMAIL", "PASSWORD","LOCATION","TIME")

  ```


## Note 
- Note: When you execute this program it will throw you a smtplib.SMTPAuthenticationError and also sends you a Critical Security alert to your email because, In a nutshell, Google is not allowing you to log in via smtplib because it has flagged this sort of login as "less secure", so what you have to do is go to this link "https://myaccount.google.com/lesssecureapps" while you're logged in to your google account, and allow the access.
- I have tried to implement all the functionality, it might have some bugs also. Ignore that or please try to solve that bug.
