import requests

from discord import app_commands, Intents, Client, Interaction

# This will print the information in console
print("\n".join([
    "---------------"
    "ENTER BOT TOKEN"
    "---------------"
]))


while True:
    # While loop starts and used Python.input() to get the token
    token = input("> ")

    # Then validates if the token you provided was correct or not
    r = requests.get("https://discord.com/api/v10/users/@me", headers={
        "Authorization": f"Bot {token}"
    })

    # If the token is correct, it will continue the code
    data = r.json()
    if data.get("id", None):
        break  # Breaks the while loop

    # If the token is incorrect, it will print the error message
    # and ask you to enter the token again (while Loop)
    print("\n")
    print("\nInvalid Token. Try Again.")
    print("\n")


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)


# Variable to store the bot class and interact with it
# Since this is a simple bot to run 1 command over slash commands
# We then do not need any intents to listen to events
client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    print("\n".join([
        f"Logged in as {client.user} (ID: {client.user.id})",
        "",
        f"Invite Bot {client.user} To Your Server:",
        "",
        f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot"
    ]))


async def _init_command_response(interaction: Interaction) -> None:

    # Responds in the console that the command has been ran
    print(f"> {interaction.user} used the command.")

    # Then responds in the channel with this message
    await interaction.response.send_message("\n".join([
        f"สวัสดี **{interaction.user}**, ขอบคุณที่ทักทายฉัน",
        "",
        "__**ยศของฉันอยู่ที่ไหน?**__",
        "",
        "Discord จะตรวจสอบเป็นระยะๆ 24 ชั่วโมงเป็นเวลาที่แนะนำให้รอ"
        "",
        "__**ผ่านไป 24 ชั่วโมงแล้ว ฉันจะรับยศได้อย่างไร?**__",
        "",
        "หากเลย 24 ชั่วโมงไปแล้ว คุณสามารถไปที่ "
        "https://discord.com/developers/active-developer และกรอก 'แบบฟอร์ม' ที่นั่น",
        "",
        "__**Active Developer Badge Updates**__",
        "",
        "การอัปเดตเกี่ยวกับยศ Active Developer สามารถพบได้ใน "
        "เซิฟ Discord Developers -> discord.gg/discord-developers - ในช่อง #active-dev-badge",
    ]))


@client.tree.command()
async def hello(interaction: Interaction):
    """ ทักทายหรืออะไรซักอย่าง """
    # Calls the function "_init_command_response" to respond to the command
    await _init_command_response(interaction)


@client.tree.command()
async def givemebadge(interaction: Interaction):
    """ ทักทายหรืออะไรสักอย่าง, แต่ใช้ชื่ออื่น """
    # Calls the function "_init_command_response" to respond to the command
    await _init_command_response(interaction)


# Runs the bot with the token you provided
client.run(token)
