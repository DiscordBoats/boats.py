import discordboats
import asyncio
import os

client = discordboats.Client()


async def runtest():
    bot = await client.get_bot("477594964742635531")
    has_voted = await client.has_voted("397745647723216898","477594964742635531")
    user = await client.get_user("397745647723216898")
    widget = await client.get_widget("477594964742635531")
    print(bot["id"], has_voted, user["id"], widget)
asyncio.get_event_loop().run_until_complete(runtest())
print("passed tests!")

