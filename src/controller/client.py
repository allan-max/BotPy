import interactions
from src.repositories.discord_repository import logsrepository

intents = interactions.Intents.ALL
bot = interactions.Client(intents=intents)
repo = logsrepository()

@bot.event
async def on_ready():
    print('Tô on')


