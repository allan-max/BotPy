import interactions
from src.repositories.discord_repository import logsrepository

repo = logsrepository()

class ban_user(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name = 'banir',
                                    options=[
                                        
                                        interactions.Option(name = 'usuario', description = 'Usuário para ser banido', required = True, type = interactions.OptionType.USER),
                                        interactions.Option(name = 'motivo', description = 'Motivo do banimento', required = True, type = interactions.OptionType.STRING)
                                    
                                    ])
    async def ban_user(self, ctx:interactions.CommandContext, usuario:interactions.User, motivo:str):

        await ctx.defer(ephemeral = True)

        id_user = usuario.id.__int__()

        message = motivo
        author_name = ctx.author.name
        guildid = ctx.guild.id.__int__()
        log_type = str('Ban')
        mute_time = str('indefinido')

        await usuario.ban(days= 7, reason = motivo)
        
        repo.add_user({
            "ids": id_user,
            "message_user": message,
            "author_name": author_name,
            "guild_id": guildid,
            "log_type": log_type,   
            "mute_time": mute_time
        }) 
        embed1 = interactions.Embed()
        embed2 = interactions.Embed()

        embed1.title = 'Usuário banido'
        embed1.description = f'O usuário <@{id_user}> - {id_user} foi banido com sucesso.'
    
        embed2.title = 'Você foi banido'
        embed2.description = f'motivo: {motivo}\nResponsavel: {author_name}'

        
def setup(bot):
    ban_user(bot)