#
# COPYRIGHT (c) CRUCIATE, JACOB, 2018 XD
#

import discord
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import datetime
import asyncio
from discord import Game

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="!help"), status=discord.Status("dnd")) 




async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current servers: ")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(1200)

@bot.command(pass_context=True)
async def info(ctx, username):
    headers = {'Authorization':'Bearer [insert_au_bearer]'}
    search = requests.get('https://api-quiz.hype.space/users?q=' + username, headers = headers)
    searchdata = search.json()
    user = searchdata["data"][0]["userId"]
    finalsearch = requests.get('https://api-quiz.hype.space/users/' + str(user), headers = headers)
    
    finaldata = finalsearch.json()
    
    totalwins = finaldata["winCount"]
    games = finaldata["gamesPlayed"]
    totalearnt = finaldata["leaderboard"]["total"]
    weeklyrank = finaldata["leaderboard"]["rank"]
    alltimerank = finaldata["leaderboard"]["alltime"]["rank"]
    weeklymoney = finaldata["leaderboard"]["weekly"]["total"]
    highestQ = finaldata["highScore"]
    namename = finaldata["username"]
    imagelink = finaldata["avatarUrl"]
    created = finaldata["created"]
    timecreated = datetime.datetime.strptime(created, '%Y-%m-%dT%H:%M:%S.%fZ')
    timelist = list(str(timecreated))
    timeyear = timelist[0:4]
    if timelist[5] == "0":
        timemonth = timelist[6]
    else:
        timemonth = timelist[5:7]

    if timelist[8] == "0":
        timeday = timelist[9]
    else:
        timeday = timelist[8:10]

    timeyear = ''.join(timeyear)
    timemonth = ''.join(timemonth)
    timeday = ''.join(timeday)

    if timemonth == '1':
        finalmonth = "January"

    elif timemonth == '2':
        finalmonth = "February."

    elif timemonth == '3':
        finalmonth = "March"

    elif timemonth == '4':
        finalmonth = "April"

    elif timemonth == '5':
        finalmonth = "May"

    elif timemonth == '6':
        finalmonth = "June"

    elif timemonth == '7':
        finalmonth = "July"

    elif timemonth == '8':
        finalmonth = "August"

    elif timemonth == '9':
        finalmonth = "September"

    elif timemonth == '10':
        finalmonth = "October"

    elif timemonth == '11':
        finalmonth = "November"

    elif timemonth == '12':
        finalmonth = "December"

# BEGIN DAY DEFINITIONS #

    if int(timeday) == 1 or int(timeday) == 21 or int(timeday) == 31:
        finalday = timeday + "st"

    elif int(timeday) == 2 or int(timeday) == 22:
        finalday = timeday + "nd"

    elif int(timeday) == 3 or int(timeday) == 23:
        finalday = timeday + "rd"

    elif int(timeday) > 3 and int(timeday) < 21: 
        finalday = timeday + 'th'

    elif int(timeday) > 23 and int(timeday) < 31:
        finalday = timeday + 'th'

    finaldate = timeday, finalmonth, timeyear
    finalfinaldate = (f'{finalday} {finalmonth} {timeyear}')
    
    # Win Percentage

    percent = float(totalwins) / float(games)
    percent  = round(percent, 2)
    winrate = str(int(percent * 100)) + '%'

    embed = discord.Embed(title="User Information", color=0x7647a2)
    embed.add_field(name="Account Name:", value ="{}".format(namename), inline=True)
    embed.add_field(name="Total Winnings:", value="{}".format(totalearnt), inline=True)
    embed.add_field(name="All Time Rank:", value="{}".format(alltimerank), inline=True)
    embed.add_field(name="Weekly Winnings:", value="{}".format(weeklymoney), inline=True)
    embed.add_field(name="Weekly Rank:", value="{}".format(weeklyrank), inline=True)
    embed.add_field(name="Highest Question:", value="{}".format(highestQ), inline=True)
    embed.add_field(name="Total Wins:", value="{}".format(totalwins), inline=True)
    embed.add_field(name="Account Created:", value="{}".format(finalfinaldate))
    embed.add_field(name="Games Played:", value="{}".format(games))
    embed.add_field(name="Win Rate:", value="{}".format(winrate))
    embed.set_thumbnail(url="{}".format(imagelink))
    embed.set_footer(text="Follow this GitHub https://github.com/Aaron-JM")
    await bot.say(embed=embed)

bot.remove_command('help')

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="HQ Assist Help", color=0x7647a2)
    embed.add_field(name="!info [user]", value="Gives information for the HQ username provided in command")
    embed.add_field(name="!botinfo", value="Gives information about HQ Assist")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title="HQ Assist", description="HQ Assist Info:", color=0x7647a2)
    embed.add_field(name="Bot's Name:", value="HQ Assist", inline=True)
    embed.add_field(name="Bot's ID:", value="449822055634829313", inline=True)
    embed.add_field(name="Servers:", value="{}".format(len(bot.servers)), inline=True)
    embed.add_field(name="Developer:", value="Cruciate#9243", inline=True)
    embed.add_field(name="Development Assistance:", value="Jacob#4235 & Jsonmarley#9752", inline=True)
    embed.set_thumbnail(url='https://i.imgur.com/D0tzEkz.png')
    await bot.say(embed=embed)

bot.loop.create_task(list_servers())

bot.run("NDczMDI4MDAyNjI0NTY5MzQ0.Dj861A.qZGjZinhZOwo4xfnNHH4B1iiFyI")
