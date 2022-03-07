#-------------Imports y Froms----------------
import discord, json
import random, string, os, colorama, sys
import time, datetime, asyncio, requests
from os import system, name
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.cooldowns import BucketType
from console.utils import set_title
from colorama import Fore		
from colorama import init
init()
#-------------Imports y Froms----------------
#-----------------Titulo y el Input osusaasdsadada------------------
version = "ULTIMATE"
set_title(f'GC Generator Bot {version} by Plutos | Enjoy the Tool')
input(f"Thank you for using Plutobear#0001's tool!\nThis tool is for{Fore.RED} EDUCATIONAL PURPOSES ONLY!{Fore.RESET}\nI will not be responsible for the misuse of the program\n{Fore.RED}Most of the codes will not work because they are random and string functions{Fore.RESET}, so good luck with that :D\nWith that said, hit {Fore.YELLOW}ENTER{Fore.RESET} to continue!")
print(Fore.BLUE + """

╭╮╱╱╭┳╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮
┃╰╮╭╯┃┃╱╱╱╱╱╱╱┃┃╱╱╱╱╱┃╭━╮┃
╰╮┃┃╭┫╰━┳╮╭┳━━┫┃╭┳━━╮┃┃╱╰╋━━┳━╮
╱┃╰╯┃┃╭╮┃┃┃┃╭━┫╰╯┫━━┫┃┃╭━┫┃━┫╭╮╮
╱╰╮╭╯┃╰╯┃╰╯┃╰━┫╭╮╋━━┃┃╰┻━┃┃━┫┃┃┃
╱╱╰╯╱╰━━┻━━┻━━┻╯╰┻━━╯╰━━━┻━━┻╯╰╯                                               
""" + Fore.RESET)
#-----------------Titulo y el Input osusaasdsadada------------------
#-----Config Data----------------------------------------
with open('config.json') as f:
	config = json.load(f)
token = config.get('token')
prefix = config.get("prefix")
game = config.get("RPC")
rate = config.get("rate")
per = config.get("per")
t = BucketType.default
anouncement = requests.get('https://pastebin.com/raw/jeqPhRxu')
#-----Config Data----------------------------------------
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
print(f"{Fore.MAGENTA}Message of the day, by Plutos: {anouncement.text}{Fore.RESET}")
#-----------------------------------------Eventos de la GiftCards osiosi----------------------------------------------------------------------------
def Vbucks():
    vbucks1 = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    vbucks2 = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"2 unchecked vbuck codes: {vbucks1} , {vbucks2}, Redeem them here: https://www.epicgames.com/fortnite/en-US/vbuckscard? "
#-----------------------------------------Fin de Eventos de la GiftCards osiosi-------------------------------------------------------------------
#-----------Inicio------------
@client.event
async def on_ready():
    print(f"{Fore.GREEN}The bot is online!{Fore.RESET}")
    print("------------------------------")
    print(f"Logged in: {Fore.RED}{client.user.name}{Fore.RESET}")
    print(f'ID of the Bot: {Fore.RED}{client.user.id}{Fore.RESET}')
    print(f"Version of {Fore.BLUE}Discord{Fore.RESET}: {discord.__version__}")
    print(f"Version of the Bot: {Fore.LIGHTMAGENTA_EX}{version}{Fore.RESET}")
    print("-------------------------------")
    print(f"{Fore.MAGENTA}--Commands Loggers--{Fore.RESET}")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(game))
#-----------Inicio------------
#----------------Eventos-------------------------------
@client.command()
@commands.guild_only()
@commands.cooldown(rate, per, t)
async def vbucks(ctx):
    await ctx.author.send(Vbucks())
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has generated a {Fore.GREEN}Vbucks Code{Fore.RESET} in time {datetime.datetime.now()}!")
    embed=discord.Embed(title="Hey your code in the DMs!", url="Plutobear#0001", description="Thank for using the bot", color=0x07f262)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/fortnite/images/e/eb/V-Bucks_-_Icon_-_Fortnite.png/revision/latest?cb=20170806013747")
    embed.add_field(name="I sent you the code in DM", value="Please go to check it!", inline=False)
    embed.set_footer(text="Vbucks Generator Tool")
    await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def cleancmd(ctx):
    os.system('cls')
    print(f"{Fore.RED}I cleaned all the cmd{Fore.RESET}")
    await ctx.send("Successfully")

@client.command()
@commands.is_owner()
async def gcdrop(ctx):
    await ctx.message.delete()
    print(f"A {Fore.RED}drop of GiftCards{Fore.RESET} is being executed :D")
    await ctx.send(Nitro())
    print(f"> Nitro Code Sended")
    await ctx.send(NitroBox())
    print(f"> Xbox Nitro Code Sended")
    await ctx.send(Steam())
    print(f"> Steam Key Sended")
    await ctx.send(Playstation())
    print(f"> PSN Code Sended")
    await ctx.send(Xbox())
    print(f"> Xbox Code Sended")
    await ctx.send(Nintendo())
    print(f"> Nintendo E-Shop Code Sended")
    await ctx.send(ProxyScrape())
    print(f"> ProxyScrape Premiun Key Sended")
    await ctx.send(Playstore())
    print(f"> Playstore Code Sended")
    await ctx.send(Itunes())
    print(f"> Itunes Code Sended")
    await ctx.send(Amazon())
    print(f"> Amazon Code Sended")
    await ctx.send(Paysafecard())
    print(f"> Paysafe Card Code Sended")
    await ctx.send(Blizzard())
    print(f"> Blizzard Code Sended")
    await ctx.send(Spotify())
    print(f"> Spotify Code Sended")
    await ctx.send(Netflix())
    print(f"> Netflix Code Sended")
    await ctx.send(Nike())
    print(f"> Nike Code Sended")
    await ctx.send(Robux())
    print(f"> Robux Code Sended")
    await ctx.send(MCWin10())
    print(f"> Minecraft Win 10 Key Code Sended")
    await ctx.send(MCCode())
    print(f"> Minecraft Code Sended")
    await ctx.send(DiscordToken())
    print(f"> Discord Token Code Sended")
    await ctx.send(Uplay())
    print(f"> Uplay Key Sended")
    await ctx.send(MalwareBytes())
    print(f"> MalwareBytes Key Sended")
    await ctx.send(Avast())
    print(f"> Avast Code Sended")
    await ctx.send(ExpressVPN())
    print(f"> Express VPN Code Sended")
    await ctx.send(HMA())
    print(f"> Hide My Ass Code Sended")
    await ctx.send(ZALTV())
    print(f"> ZalTV Code Sended")
    await ctx.send(Paypal())
    print(f"> Paypal Code Sended")
    await ctx.send(Webkinz())
    print(f"> Webkinz Code Sended")
    await ctx.send(IMVU())
    print(f"> IMVU Code Sended")
    await ctx.send(PokemonTGC())
    print(f"> Pokemon TCG Code Sended")
    print(f"-{Fore.RED}ALL THE GIFTCARDS HAS BEEN SENDED TO THE GUILD IN TIME: {datetime.datetime.now()}{Fore.RESET}-")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command(pass_context=True)
async def clean(ctx):
    if ctx.author.guild_permissions.administrator:
            llimit = ctx.message.content[10:].strip()
            await ctx.channel.purge(limit=int(llimit))
            await ctx.send('Cleared by <@{.author.id}>'.format(ctx))
            await ctx.message.delete()
    else:
        await ctx.send("You cant do that!")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')

@client.command()
@commands.has_permissions(administrator = True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return
    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)
    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!\nhttps://tenor.com/view/saussi%C3%A7on-explode-boom-gif-16089684")
    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@client.command()
async def info(ctx):
    embed=discord.Embed(title="Info", url="discord.gg/plutos", description="Thank for using the bot\nTotally free tool in c.to for the discord community", color=0xa18c8c)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/782292942067990569/828297174961225728/gift-card.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/782292942067990569/828297834674782228/397ce7ff2fc83a09a8ec26e2a9fd0c3b.jpg")
    embed.set_footer(text="GC Generator Bot Tool")
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    await ctx.send("Help")
    await ctx.send(file=File("Commands.txt"))

@client.command()
async def http(ctx):
    f = open("Proxies/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=http&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/http-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scrapped some {Fore.CYAN}HTTP Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

@client.command()
async def socks4(ctx):
    f = open("Proxies/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks4&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/socks4-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.GREEN}Socks4 Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

@client.command()
async def socks5(ctx):
    f = open("Proxies/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol=socks5&amp;timeout=10000&amp')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Proxies/socks5-proxies.txt"))
    print(f"  > User {Fore.RED} {ctx.author} {Fore.RESET} has scraped some {Fore.YELLOW}Socks5 Proxies{Fore.RESET} in time {datetime.datetime.now()}!")

client.run(token)
