from __future__ import print_function
from aiohttp import ClientSession
from asyncio import get_event_loop, AbstractEventLoop
from json import loads

from . import errors
from . import models


class Client:
    """
    API client for discord.boats
    """
    def __init__(self, token: str = None, *, baseurl: str = "https://discord.boats/api/v2/", loop:AbstractEventLoop=None):
        self.token = token
        self.baseurl = baseurl
        self.session = ClientSession(loop=loop if loop else get_event_loop())

    async def post_stats(self, botid: str, server_count: int):
        """

        :param botid: Bot to post server count on
        :param server_count: Server count
        """
        headers = {'Authorization': self.token}
        if not self.token:
            raise errors.InvalidTokenError("No token was supplied")
        r = await self.session.post(self.baseurl+"bot/{}".format(botid), json={'server_count': server_count}, headers=headers)

        if r.status != 200:
            raise errors.InvalidTokenError("Invalid token was supplied")

    async def get_bot(self, botid: str):
        """
        Gets a bot registered on discord.boats
        :param botid: Bot to be fetched
        :return Bot: Bot that was fetched
        """

        r = await self.session.get(self.baseurl+"bot/{}".format(botid))
        data = loads(await r.text())
        return models.Bot(data)

    async def has_voted(self, userid:str, botid:str):
        """
        Checks if a user has voted on a specified bot
        :param userid: User to check if has voted
        :param botid: Bot to check if the user has voted on
        :return bool: If the user has voted on that bot
        """

        r = await self.session.get(self.baseurl+"bot/{}/voted?id={}".format(botid,userid))
        return loads(await r.text())["voted"]

    async def get_user(self,userid:str):
        """
        Gets user registerd on discord.boats
        :param userid: User id
        :return User: The user that was fetched
        """

        r = await self.session.get(self.baseurl+"user/{}".format(userid))
        data = loads(await r.text())
        return models.User(data)

    async def get_widget(self, botid: str):
        """
        Get a bot widget
        :param botid: bot id
        :return str: Widget url
        """
        return self.baseurl+"widget/{}".format(botid)




