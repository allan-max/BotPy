import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef
from bson import ObjectId

repo = logsrepository()
repo2 = roledef()


class remover_logs(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='remover_log',
                          
                          options=[
                               interactions.Option(name='id', description='Id do log', required=True, type=interactions.OptionType.STRING)
                          ])
    
    async def logs(self, ctx:interactions.CommandContext, id:str):
        
        await ctx.defer()

        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            author = ctx.author
            logs = repo2.find_role(role[i]) 
            
            if logs:
                
                repo.remove_user(ObjectId(id))
                return
       
            else:
                
                author = ctx.author
                embed_else = interactions.Embed()

                embed_else.title = 'Erro ao usar o comando'
                embed_else.description = f'Você não tem permissão para usar o comando'
                embed_else.color = int('ff0000', 16)
                await author.send(embeds=embed_else)
            return
        
        else:
                embed_else1 = interactions.Embed()

                embed_else1.title = 'Erro ao usar o comando'
                embed_else1.description = f'Você não tem permissão para usar o comando'
                embed_else1.color = int('ff0000', 16)
                author = ctx.author
                await author.send(embeds=embed_else1)   
        return

def setup (bot):
    remover_logs(bot)
    