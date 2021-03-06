import discord
from discord.ext import commands

class Mod:
    def __init__(self, bot):
        self.bot = bot
        
@commands.command(pass_context=True)
@commands.has_role('Bot Commander')
async def kick(ctx, user: discord.Member, *, reason: str=None):
    """Kicks a user from your server."""
    author = ctx.message.author
    server = author.server
    try:
       await self.bot.send_message(user, "You have been kicked from {}!\nReason: {}".format(author.server, reason))
       await self.bot.kick(user)
    except:
       await self.bot.say("I cannot kick that user, or I don't have `kick_members` permission.")
       
def setup(bot):
    n = Mod(bot)
    bot.add_cog(n)
