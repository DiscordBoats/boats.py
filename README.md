# boats.py
The official discord.boats API wrapper for Python

# Examples
## Post stats
```python
import discord
import discordboats
import asyncio

client = discord.Client()
dbpy = discordboats.Client("token",loop=client.loop) # Token obtained from discord.boats

async def poststats():
    while True:
        await dbpy.post_stats(client.user.id,len(client.guilds))
        await asyncio.sleep(60)

client.loop.create_task(poststats())
client.run("token") # Discord bot token

```
