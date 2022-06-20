## Telegram_bot

Telegram bot for pizzeria, built with Python, Aiogram library, SqLite.


#### Example user mode:   
![Image description](https://github.com/Vilay397/Telegram_bot/blob/main/Intro.gif)

________________________________________________________________________________________________________________________________________

#### Example administrator mode:
![Image description](https://github.com/Vilay397/Telegram_bot/blob/main/Intro2.PNG)

## Installation and Setup Instructions

Clone this repository. You will need python, virtualenv, and aiogram library installed on your machine.

### Set up a virtual environment:

`python -m venv venv`

`venv\Scripts\activate`

#### Installation:

`pip install aiogram`
   
________________________________________________________________________________________________________________________________________

### Create bot run (.bat):

`@echo off`

`call %~dp0Telegram_bot\venv\Scripts\activate`

`cd %~dp0Telegram_bot`

`set TOKEN= <your token>`

`python bot_telegram.py`

`pause`


