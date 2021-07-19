#
#       RazeBot
#      by @fxcvd
#

from discord.ext import commands
from discord.flags import Intents
from app import config
from glob import glob


client = commands.Bot(
    command_prefix=config["prefix"],
    help_command=None,
    intents=Intents.all()
)


if __name__ == "__main__":
    for cog in glob("cogs/*.py"):
        cog = cog.replace("cogs/", "").replace(".py", "") #remove fullpath

        client.load_extension(f"cogs.{cog}")

        print(f"{cog} loaded!")


    client.run(config["token"])