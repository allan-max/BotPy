import interactions
from src.repositories.discord_repository import reportrepository

repo = reportrepository()

class report_channel_define(interactions.Extension):
    def __init__(self, bot):
        self.bot = bot
    @interactions.extension_command(name='definir_canal_para_report',
                          
                          options=[
                               interactions.Option(name= 'canal_membro', description='Canal de texto para o usuario usar o report', required=True, type=interactions.OptionType.CHANNEL),
                               interactions.Option(name= 'canal_staff', description='Canal de texto para o report ser enviado', required=True, type=interactions.OptionType.CHANNEL),          
                               interactions.Option(name= 'cargo', description='Cargo para ser marcado quando um usuario usar o report', required=True, type=interactions.OptionType.ROLE),
                          ])
        
    async def reportchanneldefine(self, ctx:interactions.CommandContext, cargo:interactions.Role, canal_membro:interactions.Channel, canal_staff:interactions.Channel):
        
        await ctx.defer(ephemeral= True)

        channel_staff = int(canal_staff.id)
        channel_member = int(canal_membro.id)
        cargo = int(cargo.id)
        guild_id = ctx.guild.id.__int__()
        
        repo.add_user({
            "channel_staff": channel_staff,
            "channel_member": channel_member,
            "guild_id": guild_id,
            "cargo": cargo
        })

        await ctx.send(f'{ctx.author.mention} Foi definindo com sucesso o canal de membros e staff para o report')

def setup (bot):
    report_channel_define(bot)