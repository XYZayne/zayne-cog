import discord
from discord.ext import commands

class boop:
    """For all your booping needs!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def boop(self, user : discord.Member):
        """Boop a user!"""

        #Your code will go here
        await self.bot.say("*boops*" + user.mention +)

def setup(bot):
    bot.add_cog(boop(bot))
