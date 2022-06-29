
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = (991702849153146982)

    async def on_ready(self):
      Channel = client.get_channel(991483254844694608)
      text= "YOUR_MESSAGE_HERE"
      huncho = await Channel.send(text)
      await huncho.add_reaction('🏃')
    
    #Reaction added
    async def on_raw_reaction_add(self, payload):


        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)


        if payload.emoji.name == '🏃':
            role = discord.utils.get(guild.roles, name='werkstatt')
            await payload.member.add_roles(role)

    #Reaction removed
    async def on_raw_reaction_remove(self, payload):


        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)


        if payload.emoji.name == '🏃':
            role = discord.utils.get(guild.roles, name='werkstatt')
            await member.remove_roles(role)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
