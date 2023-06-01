import interactions
from src.repositories.discord_repository import roledef

repo = roledef()

class role_def(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name = "definir_cargo_de_admin",
                                    options=[
                                        interactions.Option(name = "cargo", description = "cargo para usar os comandos de admin", required= True, type = interactions.OptionType.ROLE)
                                    ])

    async def role_def(self, ctx:interactions.CommandContext, cargo:interactions.Role):
        
        role = cargo.id.__int__()
        guild_id = ctx.guild.id.__int__()

        repo.add_user({
            'role': role,   
            'guild_id' : guild_id
        })
            

def setup (bot):
    role_def(bot)