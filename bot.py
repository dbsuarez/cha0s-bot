import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

bot.run('https://discordapp.com/api/webhooks/479578802771460098/l4bXi_-rFslHdWvjYGnL_mZPfl84v6uXBaol5YQqkFy_QloUlOE8PIfH572nuruZeJG0')
