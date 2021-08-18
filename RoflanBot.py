import discord
from discord import client
from discord import message
from discord import colour
from discord.embeds import Embed
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import os
from random import seed
from random import randint
import time
import textwrap
import json
import requests

TOKEN = 'ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs'

bot = commands.Bot(command_prefix='.', help_command=None)

errorEmbed = discord.Embed(
    title = 'Ошибка',
    colour = discord.Colour.from_rgb(255, 51, 51)
)

@bot.event
async def on_ready():
    print(f'{bot.user} connected with Discord!')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Помощь')
    embed.colour = discord.Colour.from_rgb(88, 101, 242)
    embed.add_field(name = 'Общее', value= "Данное меню - `.help`\nПодбросить монетку - `.random`", inline = False)
    embed.add_field(name = 'Фотографии', value= "Цитата от Жака Фреско - `.fresco текст`\nУхудшить качество изображения - `.bad уровень шакализации (0-10)`", inline = False)
    embed.add_field(name = 'Активности', value= "Смотреть ютуб в войсе - `.yt`\nИграть в шашки в войсе - `.chess`\nИграть в Betrayal.io в войсе - `.betrayal`\nИграть в Poker Night в войсе - `.poker`\nИграть в Fishington.io в войсе - `.fishing`", inline = False)
    await ctx.send(embed = embed)

@bot.command()
async def fresco(ctx, *, text = "дебил текст введи"):
    try:
        para = textwrap.wrap(text, width=15)

        MAX_W, MAX_H = 1280, 720
        im = Image.open("Fresco/fresco.jpg")
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype('/Fresco/pala.ttf', 70)

        current_h, pad = 50, 10
        for line in para:
            w, h = draw.textsize(line, font=font)
            draw.text((((MAX_W - w) / 2)-300, current_h), line, font=font, fill=(0,0,0,0))
            current_h += h + pad

        im.save(f"Fresco/RoflanBot_fresco.jpg")

        await ctx.send(file = discord.File(f"Fresco/RoflanBot_fresco.jpg"))
        os.remove(f"Fresco/RoflanBot_fresco.jpg")

    except:
        errorEmbed.description = "Напишите .fresco <текст>"
        await ctx.send(embed = errorEmbed)

@bot.command()
async def bad(ctx, qualityLvl :int = 1):
    if int(qualityLvl) >= 0 and int(qualityLvl) < 10:
        try:
            for attach in ctx.message.attachments: 
                await attach.save(f"BadQuality/RoflanBot_{attach.filename}")

                im = Image.open(f"BadQuality/RoflanBot_{attach.filename}")
                im.save(f"BadQuality/RoflanBot_{attach.filename}", quality=int(qualityLvl))

                await ctx.send(file = discord.File(f"BadQuality/RoflanBot_{attach.filename}"))

                os.remove(f"BadQuality/RoflanBot_{attach.filename}")
        except:
            errorEmbed.description = "Загрузите фото и напишите .bad <1-10>"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Качество должно быть числом от 0 до 10"
        await ctx.send(embed = errorEmbed)
        
@bot.command()
async def random(ctx):
    side = randint(0, 1)
    
    await ctx.send("https://tenor.com/view/pepe-coin-flip-gif-13326836", delete_after=0.1)

    time.sleep(1)

    if side == 0:
        embed = discord.Embed(
            title = 'Орел',
            colour = discord.Colour.from_rgb(0, 128, 255)
        )
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(
            title = 'Решка',
            colour = discord.Colour.from_rgb(240, 15, 235)
        )
        await ctx.send(embed = embed)
        
@bot.command()
async def yt(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 755600276941176913,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            errorEmbed.description = "Зайдите в канал"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Зайдите в канал"
        await ctx.send(embed = errorEmbed)
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
    
    embed = discord.Embed(
        title = 'YouTube Together',
        description = 'Перейдите по ссылке ниже, чтобы открыть ютуб в войс канале!',
        colour = discord.Colour.from_rgb(88, 101, 242)
    )
    
    await ctx.send(embed = embed)
    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def chess(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 832012774040141894,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            errorEmbed.description = "Зайдите в канал"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Зайдите в канал"
        await ctx.send(embed = errorEmbed)
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
    
    embed = discord.Embed(
        title = 'Chess',
        description = 'Перейдите по ссылке ниже, чтобы открыть шашки в войс канале!',
        colour = discord.Colour.from_rgb(88, 101, 242)
    )
    
    await ctx.send(embed = embed)
    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def betrayal(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 773336526917861400,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            errorEmbed.description = "Зайдите в канал"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Зайдите в канал"
        await ctx.send(embed = errorEmbed)
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
    
    embed = discord.Embed(
        title = 'Betrayal.io',
        description = 'Перейдите по ссылке ниже, чтобы открыть Betrayal.io в войс канале!',
        colour = discord.Colour.from_rgb(88, 101, 242)
    )
    
    await ctx.send(embed = embed)
    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def poker(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 755827207812677713,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            errorEmbed.description = "Зайдите в канал"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Зайдите в канал"
        await ctx.send(embed = errorEmbed)
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
    
    embed = discord.Embed(
        title = 'Poker Night',
        description = 'Перейдите по ссылке ниже, чтобы открыть покер в войс канале!',
        colour = discord.Colour.from_rgb(88, 101, 242)
    )
    
    await ctx.send(embed = embed)
    await ctx.send(f"https://discord.com/invite/{link['code']}")

@bot.command()
async def fishing(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 814288819477020702,
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODc2NDEwNjI0MDA2MDM3NTE0.YRjq_w.yyEhVfZd8nCFuJm1h1vgCPq8lvs",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            errorEmbed.description = "Зайдите в канал"
            await ctx.send(embed = errorEmbed)
    else:
        errorEmbed.description = "Зайдите в канал"
        await ctx.send(embed = errorEmbed)
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
    
    embed = discord.Embed(
        title = 'Fishington.io',
        description = 'Перейдите по ссылке ниже, чтобы открыть Fishington.io в войс канале!',
        colour = discord.Colour.from_rgb(88, 101, 242)
    )
    
    await ctx.send(embed = embed)
    await ctx.send(f"https://discord.com/invite/{link['code']}")

bot.run(TOKEN)