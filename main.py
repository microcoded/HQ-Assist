#
# COPYRIGHT (c) CRUCIATE, JACOB, 2018 XD
#
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
import datetime
import asyncio
from discord import Game

bot = commands.Bot(command_prefix='!')
headers = {'Authorization':'Bearer [insert_au_bearer]'}
USheaders = {'Authorization':'Bearer [insert_us_bearer]'}
DEheaders = {'Authorization' : 'Bearer [insert_de_bearer]'}
UKheaders = {'Authorization' : 'Bearer [insert_uk_bearer]'}

try: #error handling
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
        weeklyrank = str(weeklyrank)
        alltimerank = str(alltimerank)
        if weeklyrank == "101":
            weekrank = "--"
        else:
            weekrank = weeklyrank

        if alltimerank == "101":
            allrank = "--"
        else:
            allrank = alltimerank

        #work out region
        regionstart = list(totalearnt)

        if regionstart[0] == "A":
            region = "AU :flag_au:"
        elif regionstart[0] =="$":
            region = "US/Global :flag_us:"
        elif regionstart[0] == "€":
            region = "DE :flag_de:"
        else:
            region = "UK :flag_gb:"

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
        embed.add_field(name="All Time Rank:", value="{}".format(allrank), inline=True)
        embed.add_field(name="Weekly Winnings:", value="{}".format(weeklymoney), inline=True)
        embed.add_field(name="Weekly Rank:", value="{}".format(weekrank), inline=True)
        embed.add_field(name="Highest Question:", value="{}".format(highestQ), inline=True)
        embed.add_field(name="Total Wins:", value="{}".format(totalwins), inline=True)
        embed.add_field(name="Account Created:", value="{}".format(finalfinaldate))
        embed.add_field(name="Games Played:", value="{}".format(games))
        embed.add_field(name="Win Rate:", value="{}".format(winrate))
        embed.add_field(name="Region:", value="{}".format(region))
        embed.set_thumbnail(url="{}".format(imagelink))
        embed.set_footer(text="Follow this GitHub https://github.com/Aaron-JM")
        await bot.say(embed=embed)

    bot.remove_command('help')

    @bot.command(pass_context=True)
    async def help(ctx):
        embed = discord.Embed(title="HQ Assist Help", color=0x7647a2)
        embed.add_field(name="!info [user]", value="Gives information for the HQ username provided in command")
        embed.add_field(name="!botinfo", value="Gives information about HQ Assist")
        embed.add_field(name="!nextshow", value="Displays the upcoming HQ game in AEST")
        await bot.say(embed=embed)


    @bot.command(pass_context=True)
    async def botinfo(ctx):
        embed = discord.Embed(title="HQ Assist", description="HQ Assist Info:", color=0x7647a2)
        embed.add_field(name="Bot's Name:", value="HQ Assist", inline=True)
        embed.add_field(name="Bot's ID:", value="449822055634829313", inline=True)
        embed.add_field(name="Servers:", value="{}".format(len(bot.servers)), inline=True)
        embed.add_field(name="Developer:", value="Cruciate#9243", inline=True)
        embed.add_field(name="Development Assistance:", value="Jacob#2961 & Jsonmarley#9752", inline=True)
        embed.set_thumbnail(url='https://i.imgur.com/D0tzEkz.png')
        await bot.say(embed=embed)

    @bot.command(pass_context=True)
    async def nextshow(ctx):
        search = requests.get('https://api-quiz.hype.space/shows/now', headers = headers)
        data = search.json()
        livecheck = str(data["active"])
        print(livecheck)
        prize = data["nextShowPrize"]
        title = data["upcoming"][0]["nextShowLabel"]["title"]
        if str(livecheck) == "True":
            finaltime = "**Live Now :movie_camera:**"
        else:
            time = data["nextShowTime"]
            prize = data["nextShowPrize"]
            title = data["upcoming"][0]["nextShowLabel"]["title"]
            showtime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
            # you gotta somehow reformat the time above to the one below - gtg
            # showtime = str(datetime.datetime.strptime(time, '%I:%M %p'))
            #back to math we go then?
            showlist = list(str(showtime))
            time = "".join(showlist[11:13])
            minutes = "".join(showlist[13:16])
            inttime = int(time)
        #
        # AU MANUAL TIME CONVERSION
        #
            if inttime < 13 and inttime > 2:
                    autime = inttime - 2
                    finaltime = str(autime) + minutes + "pm AEST"
            elif inttime > 14 and inttime < 24:
                    autime = inttime - 14
                    finaltime = str(autime) + minutes + "am AEST"
            elif inttime == 14:
                    autime = "12"
                    finaltime = autime + minutes + "am AEST"
            elif inttime == 1 or inttime == 0:
                    autime = inttime + 10
                    finaltime = str(autime) + minutes + "am AEST"
            else:                                                           
                    finaltime == "12" + minutes + "am AEST"

    #
    # US MANUAL TIME CONVERSION
    #
        ussearch = requests.get('https://api-quiz.hype.space/shows/now', headers = USheaders)
        usdata = ussearch.json()
        uslivecheck = usdata["active"]
        usprize = usdata["nextShowPrize"]
        ustitle = usdata["upcoming"][0]["nextShowLabel"]["title"]
        if str(uslivecheck) == "True":
            usfinaltime = "**Live Now :movie_camera:**"
        else:
            usustime = usdata["nextShowTime"]
            usprize = usdata["nextShowPrize"]
            ustitle = usdata["upcoming"][0]["nextShowLabel"]["title"]
            usshowtime = datetime.datetime.strptime(usustime, '%Y-%m-%dT%H:%M:%S.%fZ')
            usshowlist = list(str(usshowtime))
            ustime = "".join(usshowlist[11:13])
            usminutes = "".join(usshowlist[13:16])
            usinttime = int(ustime)
            if usinttime < 13 and usinttime > 2:
                usautime = usinttime - 2
                usfinaltime = str(usautime) + usminutes + "pm AEST"
            elif usinttime > 14 and usinttime < 24:
                usautime = usinttime - 14
                usfinaltime = str(usautime) + usminutes + "am AEST"
            elif usinttime == 14:
                usautime = "12"
                usfinaltime = usautime + usminutes + "am AEST"
            elif usinttime == 1 or usinttime == 0:
                usautime = usinttime + 10
                usfinaltime = str(usautime) + usminutes + "am AEST"
            else:                                                           
                usfinaltime == "12" + usminutes + "am AEST"

    #
    # DE MANUAL TIME CONVERSION
    #
        desearch = requests.get('https://api-quiz.hype.space/shows/now', headers = DEheaders)
        dedata = desearch.json()
        delivecheck = dedata["active"]
        deprize = dedata["nextShowPrize"]
        detitle = dedata["upcoming"][0]["nextShowLabel"]["title"]
        if str(delivecheck) == "True":
            definaltime = "**Live Now :movie_camera:**"
        else:
            deustime = dedata["nextShowTime"]
            deprize = dedata["nextShowPrize"]
            detitle = dedata["upcoming"][0]["nextShowLabel"]["title"]
            deshowtime = datetime.datetime.strptime(deustime, '%Y-%m-%dT%H:%M:%S.%fZ')
            deshowlist = list(str(deshowtime))
            detime = "".join(deshowlist[11:13])
            deminutes = "".join(deshowlist[13:16])
            deinttime = int(detime)
            if deinttime < 13 and deinttime > 2:
                deautime = deinttime - 2
                definaltime = str(deautime) + deminutes + "pm AEST"
            elif deinttime > 14 and deinttime < 24:
                deautime = deinttime - 14
                definaltime = str(deautime) + deminutes + "am AEST"
            elif deinttime == 14:
                deautime = "12"
                definaltime = deautime + deminutes + "am AEST"
            elif deinttime == 1 or deinttime == 0:
                deautime = deinttime + 10
                definaltime = str(deautime) + deminutes + "am AEST"
            else:                                                           
                definaltime == "12" + deminutes + "am AEST"

    #
    # UK MANUAL TIME CONVERSION
    #
        uksearch = requests.get('https://api-quiz.hype.space/shows/now', headers = UKheaders)
        ukdata = uksearch.json()
        uklivecheck = ukdata["active"]
        ukprize = ukdata["nextShowPrize"]
        uktitle = ukdata["upcoming"][0]["nextShowLabel"]["title"]
        if str(uklivecheck) == "True":
            ukfinaltime = "**Live Now :movie_camera:**"
        else:
            ukustime = ukdata["nextShowTime"]
            ukprize = ukdata["nextShowPrize"]
            uktitle = ukdata["upcoming"][0]["nextShowLabel"]["title"]
            ukshowtime = datetime.datetime.strptime(ukustime, '%Y-%m-%dT%H:%M:%S.%fZ')
            ukshowlist = list(str(ukshowtime))
            uktime = "".join(ukshowlist[11:13])
            ukminutes = "".join(ukshowlist[13:16])
            ukinttime = int(uktime)
            if ukinttime < 13 and ukinttime > 2:
                ukautime = ukinttime - 2
                ukfinaltime = str(ukautime) + ukminutes + "pm AEST"
            elif ukinttime > 14 and ukinttime < 24:
                ukautime = ukinttime - 14
                ukfinaltime = str(ukautime) + ukminutes + "am AEST"
            elif ukinttime == 14:
                ukautime = "12"
                ukfinaltime = ukautime + ukminutes + "am AEST"
            elif ukinttime == 1 or ukinttime == 0:
                ukautime = ukinttime + 10
                ukfinaltime = str(ukautime) + ukminutes + "am AEST"
            else:                                                           
                ukfinaltime == "12" + ukminutes + "am AEST"



        embed = discord.Embed(title="HQ Schedule", description="Next Show Times:", color=0x7647a2)
        embed.add_field(name="HQ AU :flag_au:", value="{}, {}, Prize: {}".format(title, finaltime, prize), inline=False)
        embed.add_field(name="HQ US :flag_us:", value="{}, {}, Prize: {}".format(ustitle, usfinaltime, usprize), inline=False)
        embed.add_field(name="HQ DE :flag_de:", value="{}, {}, Prize: {}".format(detitle, definaltime, deprize), inline=False)
        embed.add_field(name="HQ UK :flag_gb:", value="{}, {}, Prize: {}".format(uktitle, ukfinaltime, ukprize), inline=False)
        await bot.say(embed=embed)

    bot.loop.create_task(list_servers())

    bot.run("NDczMDI4MDAyNjI0NTY5MzQ0.Dj861A.qZGjZinhZOwo4xfnNHH4B1iiFyI")

except:
    pass
