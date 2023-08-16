import interactions
from src.repositories.discord_repository import logsrepository
from src.repositories.discord_repository import roledef

repo = logsrepository()
repo2 = roledef()

class kick_user(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name = 'kickar',
                                    options=[
                                        
                                        interactions.Option(name = 'usuario', description = 'Usuário para ser banido', required = True, type = interactions.OptionType.USER),
                                        interactions.Option(name = 'motivo', description = 'Motivo do banimento', required = True, type = interactions.OptionType.STRING)
                                    
                                    ])
    async def ban_user(self, ctx:interactions.CommandContext, usuario:interactions.User, motivo:str):

        await ctx.defer(ephemeral = True)
        
        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            logs = repo2.find_role(role[i]) 
        
            if logs:
                id_user = usuario.id.__int__()
                author = ctx.author
                message = motivo
                author_name = ctx.author.name
                guildid = ctx.guild.id.__int__()
                log_type = str('Kick')
                mute_time = str('Indefinido')
                
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

                embed1.title = 'Usuário kickado'
                embed1.description = f'O usuário <@{id_user}> - {id_user} foi kickado com sucesso.'
                embed1.color = int(f'ff00', 16)

                embed2.title = 'Você foi kickado'
                embed2.description = f'Motivo: {motivo}\nResponsavel: {author_name}'
                embed2.color = int(f'ff0000', 16)

                await ctx.send(embeds=embed1)
                await usuario.send(embeds=embed2)
                
                await usuario.kick()
                
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

        
def setup(bot):
    kick_user(bot)