import discord, json, requests
from discord.ext import commands
from utils import parsing, mysql_module

mysql = mysql_module.Mysql()

class Deposit:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def deposit(self, ctx):
        """ Display my public wallet address to deposit funds  """
        user = ctx.message.author
        # Check if user exists in db
        mysql.check_for_user(user.id)
        user_addy = mysql.get_address(user.id)
        await self.bot.say(user.mention + "'s Deposit Address: `" + str(user_addy) + "`" + "\n\nRemember to use bws.balance to check your balance and not an explorer. The address balance and your actual balance are not always the same!\n\n:warning: DISCLAIMER: This is BETA software! Do not send large amounts of BWS! The developers are not reliable for any lost BWS!\n\n REMINDER: Do not store your coins on this server - they are not backed up and can be lost at any point! You have been warned! :warning:")

def setup(bot):
    bot.add_cog(Deposit(bot))


