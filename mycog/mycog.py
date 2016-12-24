import discord
from discord.ext import commands

class Mycog:
    """Boop!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """*boops you instead*"""
        
        async def mycom(self, user : discord.Member):
        """Boop a user."""

        #Your code will go here
        if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("*boops you instead*")
                return
            
            await self.bot.say(*boops " + user.mention + "*")

def setup(bot):
    bot.add_cog(Mycog(bot))
