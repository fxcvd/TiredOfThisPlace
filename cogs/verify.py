from os import name
import discord
from app import config
from discord.ext import commands


class Verify(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != config["verify"]["message"]:
            return

        role = discord.utils.get(payload.member.guild.roles, id=config["welcome"]["role"])
        await payload.member.add_roles(role)

    @commands.has_role(config["roles"]["admin"])
    @commands.command(name="verifyall")
    async def _verifyall(self, ctx):
        role = discord.utils.get(ctx.guild.roles, id=config["welcome"]["role"])
        for member in ctx.author.guild.members:
            await member.add_roles(role)

        await ctx.send("выдана верификация всем пользователям сервера!")

    @commands.has_role(config["roles"]["admin"])
    @commands.command(name="verify")
    async def _verify(self, ctx):
        color = config["verify"]["color"]
        image = config['verify']['image']

        embed = discord.Embed(
            title="Небольшая проверочка...", 
            description=f"**Нажми** на **реакцию** чтобы получить доступ к серверу !мяв",
            color=discord.Colour.from_rgb(color["r"], color["g"], color["b"]),
        )

        embed.set_footer(text="Защита от ботов :<")
        embed.set_image(url=image)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Verify(bot))
