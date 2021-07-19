import random

import discord
from app import config
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(config["welcome"]["id"])
        image = random.choice(config["welcome"]["image"])
        color = config["welcome"]["color"]

        embed = discord.Embed(
            title="Приветик :3", 
            description=f"Добро пожаловать, {member.mention}\n\nТы **обязательно** должен пройти <#{config['verify']['id']}>\nТакже прочитай <#{config['rules']['id']}>,\nкартинки с тиктока можно найти в группе вк,\nвопрсы по серверу к <@&{config['roles']['admin']}>.\n\n***Удачи <3***",
            color=discord.Colour.from_rgb(color["r"], color["g"], color["b"]),
        )

        embed.set_footer(text=config["links"]["vk"]["group"])
        embed.set_image(url=image)

        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Welcome(bot))
