import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef
import datetime


repo = logsrepository()
repo2 = roledef()

class mute(interactions.Extension):
    
    def __init__(self, bot):
        self.bot = bot
    
    @interactions.extension_command(name='mute',                          
                          options=[
                               interactions.Option(name='usuario', description='ID do usuário', required=True, type=interactions.OptionType.USER),
                               interactions.Option(name='tempo', description='Tempo de duração do mute(Em horas)', required=True, type=interactions.OptionType.INTEGER),
                               interactions.Option(name='motivo', description='Motivo do mute', required=True, type=interactions.OptionType.STRING),
                          ])

    async def mute(self, ctx:interactions.CommandContext, usuario:interactions.User, tempo:int, motivo:str):
        
        await ctx.defer()

        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            logs = repo2.find_role(role[i]) 
            if logs: 
       
                ids = usuario.id.__int__()
                message_user = motivo
                author = ctx.author
                author_name = ctx.author.name
                guild_id = ctx.guild.id.__int__()
                log_type = str("Mute")
                mute_time = tempo.__int__()
                
                dt = datetime.datetime.utcnow() + datetime.timedelta(hours= tempo)
                
                dt = dt.strftime("%Y-%m-%dT%H:%M:%SZ")


                await usuario.modify(communication_disabled_until = dt)  
                
                repo.add_user({
                    "ids": ids,
                    "message_user": message_user,
                    "author_name": author_name,
                    "guild_id": guild_id,
                    "log_type": log_type,   
                    "mute_time": mute_time,

                })
                
                embed_mute = interactions.Embed()
                embed_error = interactions.Embed()
                embed_send = interactions.Embed()


                embed_mute.description = f":white_check_mark: O usuário {ids} - <@{ids}> foi mutado com sucesso"
                embed_mute.color = int(f'03fc28', 16)

                embed_error.title = "Erro"  
                embed_error.description = f"<@{ids}> não foi mutado"
                embed_error.color = int(f'ff0000', 16)

                embed_send.title = "Você foi mutado"
                embed_send.description = f"Você foi mutado por {author_name}\nMotivo: {message_user}\nTempo: {mute_time} hora(s)"
                embed_send.color = int(f'ff0000', 16)
                
                await ctx.send(embeds=embed_mute) 
                await usuario.send(embeds=embed_send)
                
                
                if ctx.send == None:
                    await ctx.send(embeds=embed_error)
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
    mute(bot)
