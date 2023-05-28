import interactions
from src.repositories.discord_repository import reportrepository

repo = reportrepository()

class warn_report(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name = 'reportar',
                                    options=[
                                    interactions.Option(name= 'reportado', description= 'usuário a ser reportado', required= True, type= interactions.OptionType.USER), 
                                    interactions.Option(name= 'motivo', description= 'motivo do report', required= True, type= interactions.OptionType.STRING),
                                    interactions.Option(name= 'canal', description='canal do ocorrido', required= True, type= interactions.OptionType.CHANNEL)
                                    ])
    
    async def report(self, ctx:interactions.CommandContext, reportado:interactions.User, motivo:str, canal:interactions.Channel):
        
        await ctx.defer()

        author = ctx.author
        user_report = ctx.author.id
        user_report_name = reportado.id
        reason =  motivo
        reported_channel = canal.id
        channel_report = ctx.channel.id.__int__()
      
        logs = repo.find_channel_member(channel_report)
        
        if logs:    
            for log in logs:
                channel_id = log['channel_staff']
                cargo = log['cargo']
                for channel in ctx.guild.channels:                        
                        if channel.id == channel_id:
                            embed1 = interactions.Embed()
                            
                            embed1.title = 'Report'
                            embed1.description = f'O usuário <@{user_report}>\nreportou: {user_report_name} - <@{user_report_name}>\nMotivo: {reason}\nchat: <#{reported_channel}>'
                            embed1.color = int('03fc28', 16)
                            await channel.send(f'||<@&{cargo}>||')
                            await channel.send(embeds=embed1)
                         
        else:
                
                embed_else = interactions.Embed()

                embed_else.title = 'Erro ao usar o comando'
                embed_else.description = f'Não pode utilizar o comando de reportar fora do canal de report'
                embed_else.color = int('ff0000', 16)
                await author.send(embeds=embed_else)            
                
                        

                
                    


def setup (bot):
    warn_report(bot)