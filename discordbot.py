import os
import discord
import time
import random
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import traceback

bot =  commands.Bot(command_prefix='.a ')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
@bot.command()
async def tannto(ctx, *, day):
    
    if day == "Mon":
        await ctx.send('三年女子が担当です')
    if day == "Tue":
        await ctx.send("三年男子が担当です")
    if day == "Wed":
        await ctx.send("一年が担当です")
    if day == "Thu":
        await ctx.send("二年女子が担当です")
    if day == "Fri":
        await ctx.send("二年男子が担当です")
    if day == "Sat":
        await ctx.send("二年二名と三年二名が担当です")
    if day == "Sun":
        await ctx.send("今日は報道の仕事がありません")

@bot.command()
async def voca(ctx, word):
    result = requests.get("https://dictionary.goo.ne.jp/word/"+word+"/")
    result = BeautifulSoup(result.text, "html.parser")
    for meta_tag in result.find_all('meta', attrs={'name': 'personal_snippet'}):
        await ctx.send(meta_tag.get('content'))

    

@bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="素晴らしいボット", description="天中の情報を提供してくれる、素晴らしいボット", color=0xeee657)

    
    embed.add_field(name="製作者", value="rukoruko")

    
    embed.add_field(name="このボットの鯖加入数", value=f"{len(bot.guilds)}")
    await ctx.send(embed=embed)






bot.run(token)
