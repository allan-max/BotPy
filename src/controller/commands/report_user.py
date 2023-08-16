import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef


repo = logsrepository()
repo2 = roledef()

class aviso_user(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='avisar',
                          
                        options=[
                               interactions.Option(name='avisado', description='ID do usuário', required=True, type=interactions.OptionType.USER),
                               interactions.Option(name='motivo', description='Motivo do aviso', required=True, type=interactions.OptionType.STRING),
                          ])
    
    async def aviso(self, ctx:interactions.CommandContext, avisado:interactions.User, motivo:str):
        
        await ctx.defer()
        
        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            logs = repo2.find_role(role[i])    
            
            if logs:
                
                ids = avisado.id.__int__()
                message_user = motivo
                author = ctx.author
                author_name = ctx.author.name
                guild_id = ctx.guild.id.__int__()
                log_type = str("Aviso")
                mute_time = str("Indefinido")

        
                repo.add_user({
                    "ids": ids,
                    "message_user": message_user,
                    "author_name": author_name,
                    "guild_id": guild_id,
                    "log_type": log_type,   
                    "mute_time": mute_time
                })
                
                embed_message_user = interactions.Embed()
                embed_message_channel = interactions.Embed()

                embed_message_user.title = 'Você foi avisado'
                embed_message_user.description = f'Motivo: {message_user}\nResponsavel: {author_name}\nEspero que não se repita.'
                embed_message_user.color = int('ffff00', 16)
                
                await avisado.send(embeds=embed_message_user)
                
                embed_message_channel.title = 'Aviso'
                embed_message_channel.description = f':white_check_mark: O usuário <@{ids}> foi avisado com sucesso.'
                embed_message_channel.color = int(f'ff00', 16)
                
                await ctx.send(embeds=embed_message_channel) 
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
    aviso_user(bot)

