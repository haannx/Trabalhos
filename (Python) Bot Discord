# Trabalhos
Alguns dos meus trabalhos em Python

#Bot para o discord. é um bot de atendimento, onde a pessoa pode solicitar informações de recrutamento, e em caso de interesse abrir ticket para falar com a administração
ele tem algumas funções a mais como o (/dado) que gira uma dado e de modo aleátorio fornece um valor de 1 a 6. Caso queira usar precisa modificar algumas partes do código para
o ser servidor como na linha 15, colocando seu id do servidor, na linha 16 o id do cargo de atendente, na linha 17 o token/id do bot e na linha 110, novamente o token/id do bot.

#OBS: ele precisa de um servidor em nuvem para rodar, pode usar sites como replit ou squarecloud.

import discord
from discord import app_commands
from discord.ext import commands
import random

id_do_servidor = 
id_cargo_atendente = 
token_bot = 

class Dropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(value="duvidas",label="Como Entro na Equipe?", emoji="👋"),
            discord.SelectOption(value="pedirrec",label="Pedir Recrutamento...", emoji="📨"),
        ]
        super().__init__(
            placeholder="Selecione uma opção...",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="persistent_view:dropdown_help"
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "duvidas":
            await interaction.response.send_message("👉 Caso queira se tornar um membro da FLK terá de fazer o teste. Você pode ficar por dentro dos testes dando uma olhada nos canais de teste!",ephemeral=True)
        elif self.values[0] == "pedirrec":
            await interaction.response.send_message("👉 Clique abaixo para criar um ticket e pedir seu recrutamento!",ephemeral=True,view=CreateTicket())

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Dropdown())

class CreateTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=15)
        self.value = None

    @discord.ui.button(label="Abrir Ticket",style=discord.ButtonStyle.blurple,emoji="➕")
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        self.value = True
        self.stop()

        ticket = None
        for thread in interaction.channel.threads:
            if f"{interaction.user.id}" in thread.name:
                if thread.archived:
                    ticket = thread
                else:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
        
        if ticket is not None:
            await ticket.unarchive()
            await ticket.edit(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080,invitable=False)
        else:
            ticket = await interaction.channel.create_thread(name=f"{interaction.user.name} ({interaction.user.id})",auto_archive_duration=10080)#,type=discord.ChannelType.public_thread)
            await ticket.edit(invitable=False)

        await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
        await ticket.send(f"📩  **|** {interaction.user.mention} Ticket criado! Por favor, aguarde até ser atendido por nossos recrutadores! Caso queira fechar o ticket use **/fecharticket**")

class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def setup_hook(self) -> None:
        self.add_view(DropdownView())

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild=discord.Object(id=1046884798444085328)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.") 

client = Client()
tree = app_commands.CommandTree(client)

@tree.command(guild=discord.Object(id=1046884798444085328), name="setup", description="Setup")
@commands.has_permissions(manage_guild=True)
async def setup(interaction: discord.Interaction):
    await interaction.response.send_message("🛡 **Óla, seja bem-vindo(a) ao servidor da FLK, em caso de duvida abra um ticket selecionando uma das opções abaixo!**", view=DropdownView()) 

@tree.command(guild=discord.Object(id=1046884798444085328), name="fecharticket", description="Feche um atendimento atual.")
async def fecharticket(interaction: discord.Interaction):
    mod = interaction.guild.get_role(id_cargo_atendente)
    if str(interaction.user.id) in interaction.channel.name or mod in interaction.author.roles:
        await interaction.response.send_message(f"O ticket foi arquivado por {interaction.user.mention}, obrigado por entrar em contato!")
        await interaction.channel.edit(archived=True)
    else:
        await interaction.response.send_message("Isso não pode ser feito aqui...")

@tree.command(guild=discord.Object(id=id_do_servidor), name="dado", description="rolar dado")
async def roll_dice(interaction: discord.Interaction):
    numero = random.randint(1, 6)
    await interaction.response.send_message(f"numero {numero}!", ephemeral=True) 

client.run(token_bot)
