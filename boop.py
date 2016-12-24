import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

class Boop:
    """Boop command."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/boop/items.json", "load")

    def save_items(self):
        fileIO("data/boop/items.json", 'save', self.items)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def boop(self, ctx, *, user : discord.Member=None):
        """Boop a user"""
        if ctx.invoked_subcommand is None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("*boops you instead*")
                return
            await self.bot.say("*boops*" + user.name)

def check_folders():
    if not os.path.exists("data/boop"):
        print("Creating data/boop folder...")
        os.makedirs("data/boop")

def check_files():
    f = "data/boop/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)

def setup(bot):
    check_folders()
    check_files()
    n = Boop(bot)
    bot.add_cog(n)