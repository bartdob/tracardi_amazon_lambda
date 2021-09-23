import asyncio
import aiohttp
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_amazon_lambda.model.model import AmazonLambda


class LambdaAction(ActionRunner):
    def __init__(self, **kwargs):
        self.apiEndpoint = kwargs['apiEndpoint']

    async def run(self, payload):
        # print(self.apiEndpoint)
        async with aiohttp.ClientSession() as session:
            result = await session.get(url=self.apiEndpoint)
            return Result(port="payload", value={
                "status": result.status,
                "body": await result.json()
            })


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='',
            className='pushover',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "apiEndpoint": None,
            }

        ),
        metadata=MetaData(
            name='AmazonLabda',
            desc='Connects to Amazon Lambda.',
            type='flowNode',
            width=200,
            height=100,
            icon='amazonLambda',
            group=["Connectors"]
        )
    )
