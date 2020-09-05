from discord.ext import commands
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


def setup(bot):
    bot.add_cog(Character(bot))
    print('[•] Character Cog Loaded')


if __name__ == '__main__':
    pass
