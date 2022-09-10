import os
from os import system
from datetime import datetime
import discord
from keep_alive import keep_alive
from dotenv import load_dotenv
from replit import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = (991831467917328487)

    async def on_ready(self):
        print("Running")
        #Channel = client.get_channel(991830052134191154)
        #text= "Bitte hier eintragen, wenn ihr in der Werkstatt, im Außendienst oder Zivil seid. \n 🧰 → @In der Werkstatt \n 🚗 → @Außendienst \n 🆓 → @Zivil"
        #huncho = await Channel.send(text)
        #await huncho.add_reaction('🧰')
        #await huncho.add_reaction('🚗')
        #await huncho.add_reaction('🆓')

    #Reaction added
    async def on_raw_reaction_add(self, payload):

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        if payload.emoji.name == '🧰':
            role = discord.utils.get(guild.roles, name='Werkstatt')
            await payload.member.add_roles(role)
            key = str(payload.member.display_name)
            now = datetime.now()
            value = str(now.strftime("%d %m %Y %H:%M"))
            db[key] = value

        if payload.emoji.name == '🚗':
            role = discord.utils.get(guild.roles, name='Außendienst')
            await payload.member.add_roles(role)
            key = str(payload.member.display_name)
            now = datetime.now()
            value = str(now.strftime("%d %m %Y %H:%M"))
            db[key] = value

        if payload.emoji.name == '🆓':
            role = discord.utils.get(guild.roles, name='Zivi')
            await payload.member.add_roles(role)
            key = str(payload.member.display_name)
            now = datetime.now()
            value = str(now.strftime("%d %m %Y %H:%M"))
            db[key] = value

    #Reaction removed
    async def on_raw_reaction_remove(self, payload):

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🧰':
            role = discord.utils.get(guild.roles, name='Werkstatt')
            await member.remove_roles(role)
            key = str(member.display_name)
            now = datetime.now()
            now2 = now.strftime("%d %m %Y %H:%M")
            begin = db[key]
            begin_time = datetime.strptime(begin, "%d %m %Y %H:%M")
            end_time = datetime.strptime(now2, "%d %m %Y %H:%M")
            diff = end_time - begin_time
            Channel = client.get_channel(991829968709500939)
            text2 = key + " war " + str(
                diff)[:-3] + " Std&Min in der Werkstatt."
            await Channel.send(text2)

        if payload.emoji.name == '🚗':
            role = discord.utils.get(guild.roles, name='Außendienst')
            await member.remove_roles(role)
            key = str(member.display_name)
            now = datetime.now()
            now2 = now.strftime("%d %m %Y %H:%M")
            begin = db[key]
            begin_time = datetime.strptime(begin, "%d %m %Y %H:%M")
            end_time = datetime.strptime(now2, "%d %m %Y %H:%M")
            diff = end_time - begin_time
            Channel = client.get_channel(991829968709500939)
            text2 = key + " war " + str(diff)[:-3] + " Std&Min im Außendienst."
            await Channel.send(text2)

        if payload.emoji.name == '🆓':
            role = discord.utils.get(guild.roles, name='Zivi')
            await member.remove_roles(role)
            key = str(member.display_name)
            now = datetime.now()
            now2 = now.strftime("%d %m %Y %H:%M")
            begin = db[key]
            begin_time = datetime.strptime(begin, "%d %m %Y %H:%M")
            end_time = datetime.strptime(now2, "%d %m %Y %H:%M")
            diff = end_time - begin_time
            Channel = client.get_channel(991975908976107530)
            text2 = key + " war " + str(diff)[:-3] + " Std&Min Zivil."
            await Channel.send(text2)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
keep_alive()
try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
