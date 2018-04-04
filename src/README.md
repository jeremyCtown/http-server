# LAB: http-server

Version 0.0.1

## Description

This is an HTTP-server that connects to cowpy and renders different cowacters based on input. It conducts GET and POST operations.

## Setup
### General Requirements: 
Python 3 with ENV

### ENV Requirements: 
attrs==17.4.0
certifi==2018.1.18
chardet==3.0.4
cowpy==1.0.3
idna==2.6
more-itertools==4.1.0
pluggy==0.6.0
py==1.5.3
pytest==3.5.0
requests==2.18.4
six==1.11.0
urllib3==1.22

## User Interface
/ - redirects to /cowsay
/cowsay - provides user with information about how to perform a query in the address bar
/cow?msg=text - returns a cow with the message in a thought bubble
    Example: /cow?msg='Coding with python is fumb!'

## Change Log

V0.0.1 - 4-03-2018 1800h - First release
V0.0.0 - 4-03-2018 1400h - Project initiated


