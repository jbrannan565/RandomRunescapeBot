from discord.ext import commands

from _lib.runescape_fetcher import RunscapeFetcher

class Fetcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fetcher = RunscapeFetcher()

    @commands.command(help='Get a random fact from the runescape wiki.') 
    async def random(self, ctx):
        text, url = self.fetcher.get_text()
        if text:
            await ctx.send(f"""Did you know that:\n
            {text}

            Learn more: {url}
            """)
        else:
            await ctx.send(f"Something went wrong...")
