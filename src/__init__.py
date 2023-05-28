from src.controller.client import bot
from src.config import ConfigurationAPIDiscord
import os

def main():
    for filename in os.listdir('src/controller/commands'):
        if filename.endswith('.py'):
            bot.load(f'src.controller.commands.{filename[:-3]}')
    


    bot.start(ConfigurationAPIDiscord.token)