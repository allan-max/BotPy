import interactions
from src.repositories.discord_repository import logsrepository
from bson import ObjectId

repo = logsrepository()

class remover_logs(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='remover_log',
                          
                          options=[
                               interactions.Option(name='id', description='Id do log', required=True, type=interactions.OptionType.STRING)
                          ])
    
    async def logs(self, ctx:interactions.CommandContext, id:str):
        
        repo.remove_user(ObjectId(id))

def setup (bot):
    remover_logs(bot)
    