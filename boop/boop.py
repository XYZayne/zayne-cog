import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def boop(self, user : discord.Member):
        """*boops " + user.mention + "*"""

        #Your code will go here
        await self.bot.say("*boops you instead*")


def setup(bot):
    bot.add_cog(Mycog(bot))
