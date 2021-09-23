from pydantic import BaseModel
import aiohttp
from tracardi_plugin_sdk.domain.result import Result


class AmazonLambda(BaseModel):
    apiEndpoint: str

    async def connect(self):
        async with aiohttp.ClientSession() as session:
            return await session.get(url=self.apiEndpoint)
