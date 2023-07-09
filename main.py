'''
The purpose of this template is to create a Discord bot that sends a message once a day at a random time.
Obvioulsy, you can modify sync time, sleep time, etc. to suit your needs.

In order to run properly, you'll have to add the channel ID in which the message will be sent, the message you want to send and your bot Token ID.
Be careful with your Token ID, you have to keep it secret. Do not share it with anyone !
'''
import asyncio
import discord   # discord.py==2.3.1
import datetime
import random


# Constant used to sync background task loop with midnight
SYNC_TIME = datetime.time(hour=0, minute=0)


class MyBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    async def setup_hook(self) -> None :
        self.bg_task = self.loop.create_task(self.my_background_task())


    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(0000000000000000000)   # ADD YOUR CHANNEL ID HERE

        now = datetime.datetime.now()
        print(f"[~] Waiting for synchronization ({SYNC_TIME}).")
        while not (SYNC_TIME.hour == now.hour and SYNC_TIME.minute == now.minute):
            await asyncio.sleep(10)
            now = datetime.datetime.now()
 
        while not self.is_closed():
            print("[+] Synchronization done !")
            # Pick a random second of the day to send the message
            max_second_to_wait = 86400   # 60s * 60m * 24h
            time_to_sleep = random.randint(0, max_second_to_wait)
            print(f"[~] Message will be sent in {time_to_sleep} seconds.")
            await asyncio.sleep(time_to_sleep)

            # Send message in the specific channel
            now = datetime.datetime.now()
            await channel.send("YOUR_MESSAGE_HERE")   # ADD YOUR MESSAGE HERE
            print(f"[+] Message sent ! (at {now.hour}:{now.minute:02})")

            # Sleep until next sync time
            print(f"[~] Waiting for next synchronization ({SYNC_TIME}).")
            await asyncio.sleep(max_second_to_wait - time_to_sleep)
            

if __name__ == '__main__':
    bot = MyBot(intents=discord.Intents.default())
    bot.run("TOKEN_HERE")   # ADD YOUR BOT TOKEN HERE
