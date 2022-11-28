import requests

from discord import app_commands, Intents, Client, Interaction

print("\n".join([
    "----------------------",
    "| ////////////////// |",
    "|   Enter Bot Token  |",
    "| ////////////////// |",
    "----------------------"
]))


while True:
    token = input("> ")

    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    data = r.json()
    if data.get("id", None):
        break

    print("\nInvalid Bot Token. Try again.")


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync(guild=None)


client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    """ This is called when the bot is ready and has a connection with Discord
        It also prints out the bot's invite URL that automatically uses your
        Client ID to make sure you invite the correct bot with correct scopes.
    """
    print("\n".join([
        f"Logged {client.user} (ID: {client.user.id})",
        "",
        f"Link Invite Bot {client.user} To Server:",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"
    ]))


async def _init_command_response(interaction: Interaction) -> None:
    """ This is called when the command is ran
        The reason the command is outside of the command function
        is because there are two ways to run the command and slash commands
        do not natevily support aliases, so we have to fake it.
    """

    print(f"> {interaction.user} used the command.")

    await interaction.response.send_message("\n".join([
        f"สวัสดี **{interaction.user}**, ขอบคุณที่ทักทายฉัน.",
        "",
        "__**ยศของฉันอยู่ไหน?**__",
        "Discord จะตรวจสอบยศเป็นระยะๆ, "
        "ภายใน 24 ชั่วโมงหรือมากกว่านั้นคุณจะได้รับยศ,"
        "",
        "__**ผ่านไป 24 ชั่วโมงแล้ว, ฉันจะรับยศอย่างไร?**__",
        "หากเลย 24 ชั่วโมงไปแล้ว คุณสามารถไปที่ "
        "https://discord.com/developers/active-developer และกรอก 'แบบฟอร์ม' ที่นั่น",
        "",
        "__**Active Developer Badge Updates**__",
        "การอัปเดตเกี่ยวกับยศ Active Developer สามารถพบได้ใน "
        "เซิร์ฟเวอร์ Discord Developers -> discord.gg/discord-developers - ในช่อง #active-dev-badge",
    ]))


@client.tree.command()
async def hello(interaction: Interaction):
    """ พิม hello หรืออะไรซักอย่าง """
    await _init_command_response(interaction)


@client.tree.command()
async def givemebadge(interaction: Interaction):
    """ hello หรืออะไรสักอย่าง แต่ใช้ชื่ออื่น """
    await _init_command_response(interaction)

client.run(token)