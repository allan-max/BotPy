import interactions
from src.repositories.discord_repository import reportrepository
from src.repositories.discord_repository import roledef

repo = reportrepository()

repo2 = roledef()

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
        
        role = ctx.member.roles
        i = 0
        
        while len(role) > i:
            
            author = ctx.author

            logs = repo2.find_role(role[i]) 
            
            if logs:

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
    report_channel_define(bot)