from logging import Logger, StreamHandler
from os import environ as env
from typing import Optional

from aiohttp import ClientSession

from novelai_api import NovelAIAPI
from novelai_api.utils import get_encryption_key


class API:
    _username: str
    _password: str
    _session: ClientSession

    logger: Logger
    api: Optional[NovelAIAPI]
    access_token: Optional[str]

    def __init__(self, access_token):
        self.logger = Logger("NovelAI")
        self.logger.addHandler(StreamHandler())

        self.api = NovelAIAPI(logger=self.logger)
        self.access_token = access_token

    @property
    def encryption_key(self):
        return get_encryption_key(self._username, self._password)

    async def __aenter__(self):
        self._session = ClientSession()
        await self._session.__aenter__()

        self.api.attach_session(self._session)
        #self.access_token = await self.api.high_level.login(self._username, self._password)
        self.access_token = await self.api.high_level.login_with_token(self.access_token)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.__aexit__(exc_type, exc_val, exc_tb)