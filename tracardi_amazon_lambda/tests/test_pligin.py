import asyncio
from tracardi_amazon_lambda.plugin import LambdaAction


init = dict(
    apiEndpoint='https://dy9zfzh264.execute-api.eu-central-1.amazonaws.com/test2/'
)

payload = {}


async def main():
    plugin = LambdaAction(**init)
    result = await plugin.run(payload)
    print(result)

asyncio.run(main())
