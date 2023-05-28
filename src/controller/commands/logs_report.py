import interactions
from src.repositories.discord_repository import logsrepository
import os

repo = logsrepository()
class logs(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='logs',
                          
                          options=[
                               interactions.Option(name='usuario', description='ID do usuário', required=True, type=interactions.OptionType.USER)
                          ])
    
    async def logs(self, ctx:interactions.CommandContext, usuario:interactions.User):
       
        await ctx.defer(ephemeral= True)

        ids = usuario.id.__int__()
        guild_id = ctx.guild.id.__int__()
        logs = repo.find_all_user_id(ids) and repo.find_all_guild_id(guild_id)
        embed = interactions.Embed()
        
        if logs:
           
            embed_start_message = embed
            embed_content_message = embed

            embed_start_message.description = f"Logs do Id: {ids} - <@{ids}>"
            embed_start_message.color = int(f'03fc28', 16)

            await ctx.send(embeds=embed_start_message)  

            embed_content_message.description = ''

            for log in logs:                
                
                embed_content_message.description += f"ID: {ids}\nMotivo: {log['message_user']}\nTipo: {log['log_type']}\nTempo: {log['mute_time']}hora(s)\nResponsavel: {log['author_name']}\n\n"
                embed_content_message.color = int(f'03fc28', 16)
                    
            await ctx.send(embeds=embed_content_message)
    

        else: 
            
            embed_error = embed
            embed_error.description = f":x: Nenhum log encontrado para o usuário: {ids} - <@{ids}>"
            embed_error.color = int(f'ff0000', 16)
            
            await ctx.send(embeds=embed_error)
   
def setup (bot):
    logs(bot)
    