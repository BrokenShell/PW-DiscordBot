from discord.ext import commands
from Combat.cogs.combat_ops import combat
from Combat.pirates import Pirate
from Combat.data import DataModel


class Character(commands.Cog):
    """ Pirate Commands """
    db = DataModel()

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create(self, ctx, *, name):
        if self.db.find({'Name': name}):
            await ctx.send('Pirate already exists. Please choose a different name.')
        else:
            await ctx.send(Pirate(name, ctx.author))

    @commands.command()
    async def test_author(self, ctx):
        await ctx.send(ctx.author)

    @commands.command()
    async def duel(self, ctx, *, target: str):
        player = self.db.load({'Player': str(ctx.author)})
        opponent = self.db.load({'Name': target})
        result = combat(player, opponent)
        await ctx.send(result)


def setup(bot):
    bot.add_cog(Character(bot))
    print('[•] Character Cog Loaded')
