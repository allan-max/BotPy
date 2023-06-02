import interactions
from src.repositories.discord_repository import roledef
from bson import ObjectId

repo = roledef()


class logs_role(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='logs_de_cargos')
    
    async def logs_role(self, ctx:interactions.CommandContext):
        
        await ctx.defer()

        author = ctx.author
        role = ctx.member.roles
        i = 0

        while len(role) > i:
           
            logs = repo.find_role(role[i]) 
            guild_id = ctx.guild.id.__int__()
            guild = repo.find_guild_role(guild_id)
         
            if logs and guild:

                embed_log = interactions.Embed()
    
                embed_log.description = ' '
                
                for log in guild:
                    
                    embed_log.description += f"ID do Log: {log['_id']}\n\nCargo: <@&{log['role']}>\nDefinido por: {log['author']}\n\n"
                    embed_log.color = int(f'ff00', 16)
            
                await ctx.send(embeds=embed_log)
                return
                
            else:   
                embed_else1 = interactions.Embed()

                embed_else1.title = 'Erro ao usar o comando'
                embed_else1.description = f'Você não tem permissão para usar o comando'
                embed_else1.color = int(f'ff0000', 16)
            
                await author.send(embeds=embed_else1)   
            return
        
        else:   
            embed_else1 = interactions.Embed()

            embed_else1.title = 'Erro ao usar o comando'
            embed_else1.description = f'Você não tem permissão para usar o comando'
            embed_else1.color = int(f'ff0000', 16)
        
            await author.send(embeds=embed_else1)   
        return
        

def setup (bot):
    logs_role(bot)