import interactions
from src.repositories.discord_repository import roledef

repo = roledef()

class role_def(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name = "definir_cargo_de_staff",
                                    options=[
                                        interactions.Option(name = "cargo", description = "cargo para usar os comandos de admin", required= True, type = interactions.OptionType.ROLE)
                                    ])

    async def role_def(self, ctx:interactions.CommandContext, cargo:interactions.Role):
        
        if ctx.member.permissions == 140737488355327:
            
            author = ctx.member
            role = cargo.id.__int__()
            guild_id = ctx.guild.id.__int__()

            repo.add_user({
                'role': role,   
                'guild_id' : guild_id
            })
        
        else:
                
            embed_else = interactions.Embed()

            embed_else.title = 'Erro ao usar o comando'
            embed_else.description = f'Você não tem permissão para usar o comando'
            embed_else.color = int('ff0000', 16)
            await author.send(embeds=embed_else)     

def setup (bot):
    role_def(bot)