import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef
from bson import ObjectId

repo = logsrepository()
repo2 = roledef()


class remover_log_role(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='remover_log_de_staff',
                          
                          options=[
                               interactions.Option(name='id', description='Id do log', required=True, type=interactions.OptionType.STRING)
                          ])
    
    async def remover_logs_role(self, ctx:interactions.CommandContext, id:str):
        
        await ctx.defer()

        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            author = ctx.author
            logs = repo2.find_role(role[i]) 
            
            if logs:
                             
                if repo2.find_user_id(ObjectId(id)):
                     
                    repo2.remove_user(ObjectId(id))

                    embed = interactions.Embed()
                    embed.title = "Log apagado"
                    embed.description = "O Log foi apagado com sucesso"
                    embed.color = int(f'ff00', 16)

                    await ctx.send(embeds=embed)
                    return
                
                else:
                    
                    author = ctx.author
                    embed1 = interactions.Embed()
                    embed1.title = "Erro"
                    embed1.description = "O Log não foi encontrado, confira se colocou o ID do Log correto"
                    embed1.color = int(f'ff0000', 16)
                    await author.send(embeds=embed1)
                return
                
            else:
         
                embed_else = interactions.Embed()

                embed_else.title = 'Erro ao usar o comando'
                embed_else.description = f'Você não tem permissão para usar o comando'
                embed_else.color = int(f'ff0000', 16)
            author = ctx.author
            await author.send(embeds=embed_else)
            return
        
        else:
            embed_else1 = interactions.Embed()

            embed_else1.title = 'Erro ao usar o comando'
            embed_else1.description = f'Você não tem permissão para usar o comando'
            embed_else1.color = int(f'ff0000', 16)
        author = ctx.author
        await author.send(embeds=embed_else1)   
        return

def setup (bot):
    remover_log_role(bot)
    