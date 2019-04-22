import discord
import apexApi
import json

TOKEN = "NTY5MDk1OTkyMzY1MDIzMjMy.XLrqRw.CDsy9PuIWTypSwnzZgcR1oMbtao"

client = discord.Client()

@client.event
async def on_message(message):
    msg = ""
    if message.author == client.user:
        return

    if message.content.startswith("!hi"):
        author = message.author.mention
        msg = "Heey {} long time no see!\nUse command !prefs to see what i can do for you.".format(author)
        await message.channel.send(msg)

    elif message.content.startswith("!prefs"):
        msg = "Well, you insist you want to know.\nI was developed to give you stats about your recent games in Apex-Legends.But since i am new to this system and still learning to develop myself, i will only send you your current banner information for now, so be patient!\n\navailable commands:```!banner : current banner information --accountname```\n"
        await message.channel.send(msg)

    elif message.content.startswith("!banner"):
        l = message.content.split(" ")
        msg = ""
        # too many accountnames given
        if len(l) > 2:
            msg = "You making me crazy, give me only one accountname! "
        else:
            # no accountname
            if len(l) == 1:
                msg = "Give me your accountname!"
            # one accountname given
            else:
                username = l[1]
                apexapi = apexApi.apexApi(5,username)
                banner_stats = apexapi.get()
                try:
                    msg = build_response(banner_stats)
                except:
                    try:
                        msg = banner_stats["errors"][0]["message"]
                    except:
                        msg = "Something went wrong, dont know what to do !"
        await message.channel.send(msg)

def writeStats(banner_stats):
    with open("banner_stats.json","w") as output:
        json.dump(banner_stats,output,indent = 4)

def build_response(banner_stats):
    writeStats(banner_stats)
    res = ""
    legend_name = banner_stats["data"]["children"][0]["metadata"]["legend_name"]
    legend_img = banner_stats["data"]["children"][0]["metadata"]["icon"]
    res += "legend name : {}\n".format(legend_name)
    bg_img = banner_stats["data"]["children"][0]["metadata"]["bgimage"]

    l = collect_stats(banner_stats)
    for x in l:
        key, value = getKV(x)
        if not key in res: res += "{} : {}\n".format(key,value)
    res += legend_img
    return res

def collect_stats(banner_stats,l=[]):
    for k,v in banner_stats.items():
        if k == "children":
            for c in v[0]["stats"]:
                l.append(c)
        elif k == "stats":
            for c in v:
                l.append(c)
        else:
            if isinstance(v,dict):
                collect_stats(v,l=l)
    return l

def getKV(d):
    key = d["metadata"]["key"]
    value = d["displayValue"]
    return key,value

@client.event
async def on_read():
    print("logged in")
    print(client.user.name)
    print(client.user.id)

client.run(TOKEN)
