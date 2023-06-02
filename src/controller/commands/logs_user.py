import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef

repo = logsrepository()
repo2 = roledef()

class logs(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='logs',
                          
                          options=[
                               interactions.Option(name='usuario', description='ID do usuário', required=True, type=interactions.OptionType.USER)
                          ])
    
    async def logs(self, ctx:interactions.CommandContext, usuario:interactions.User):
       
        await ctx.defer()

        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            logs2 = repo2.find_role(role[i]) 
            
            if logs2:

                ids = usuario.id.__int__()
                guild_id = ctx.guild.id.__int__() 
                logs = repo.find_all_user_id(ids)
                guild = repo.find_all_guild_id(guild_id)
            
                if logs and guild:
                
                    embed_start_message = interactions.Embed()
                    embed_content_message = interactions.Embed()

                    embed_start_message.description = f"Logs do Id: {ids} - <@{ids}>"
                    embed_start_message.color = int(f'ff00', 16)

                    await ctx.send(embeds=embed_start_message)  

                    embed_content_message.description = ''

                    for log in logs:                
                        
                        embed_content_message.description += f"ID do Log: {log['_id']}\n\nID do Usuário: {log['ids']}\nMotivo: {log['message_user']}\nTipo: {log['log_type']}\nTempo: {log['mute_time']}\nResponsavel: {log['author_name']}\n\n"
                        embed_content_message.color = int(f'ff00', 16)
                    
                    await ctx.send(embeds=embed_content_message)
                    return

                else: 
                    
                    embed_error = interactions.Embed()
                    embed_error.description = f":x: Nenhum log encontrado para o usuário: {ids} - <@{ids}>"
                    embed_error.color = int(f'ff0000', 16)
                    
                    await ctx.send(embeds=embed_error)
                return
                
            else:
                
                author = ctx.author
                embed_else = interactions.Embed()

                embed_else.title = 'Erro ao usar o comando'
                embed_else.description = f'Você não tem permissão para usar o comando'
                embed_else.color = int(f'ff0000', 16)
                
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
    logs(bot)
    