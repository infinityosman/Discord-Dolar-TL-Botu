import os
import discord
from discord.ext import commands,tasks
import requests
from bs4 import BeautifulSoup
import asyncio
from datetime import datetime

import config


intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix="!", intents=intents)

async def status_task():
    while True:
        URL = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        r = requests.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') 
        tlkarsiligi= soup.find('span', attrs = {'class':'value up'}).text
        oncekikapanis= soup.find('span', attrs = {'class':'text2'}).text
        degisim = soup.find('span', attrs = {'class':'text3'}).text
        sembol = ""
        mylist = []
        mylist.append(degisim)
        if mylist[0][0] == "-":
          sembol = "↙"
          eksisiz = ""
          mylist2 = []
          mylist2.append(degisim)
          uzunluk = len(mylist2[0])
          eksisiz = mylist2[0][1:uzunluk]
        else:
          sembol ="↗"
          eksisiz = ""
          mylist2 = []
          mylist2.append(degisim)
          uzunluk = len(mylist2[0])
          eksisiz = mylist2[0][0:uzunluk]
        await client.change_presence(activity=discord.Game(name="₺"+ tlkarsiligi+" | "+sembol+" "+eksisiz))
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(tlkarsiligi+"-----"+time)
        await asyncio.sleep(10)
        URL = "https://bigpara.hurriyet.com.tr/doviz/dolar/"
        r = requests.get(URL)
      
        soup = BeautifulSoup(r.content, 'html5lib') 
        tlkarsiligi= soup.find('span', attrs = {'class':'value up'}).text
        oncekikapanis= soup.find('span', attrs = {'class':'text2'}).text
        degisim = soup.find('span', attrs = {'class':'text3'}).text
        sembol = ""
        mylist = []
        mylist.append(degisim)
        if mylist[0][0] == "-":
          sembol = "↙"
          eksisiz = ""
          mylist2 = []
          mylist2.append(degisim)
          uzunluk = len(mylist2[0])
          eksisiz = mylist2[0][1:uzunluk]
        else:
          sembol ="↗"
          eksisiz = ""
          mylist2 = []
          mylist2.append(degisim)
          uzunluk = len(mylist2[0])
          eksisiz = mylist2[0][0:uzunluk]
        await client.change_presence(activity=discord.Game(name="₺"+ tlkarsiligi+" | "+sembol+" "+eksisiz))
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(tlkarsiligi+("-----")+time)
        await asyncio.sleep(10)


@client.event
async def on_ready():
  print('{0.user} olarak giriş yapıldı!'.format(client))
  client.loop.create_task(status_task())
  
  


client.run(config.botapi_key)
