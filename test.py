import httpx
import asyncio

async def post_data():
    data = {'name': '程序员阿江','email':'relakkes@gmail.com'}
    async with httpx.AsyncClient() as client:
        response = await client.post('https://httpbin.org/post', data=data)
        print(response.json())

asyncio.run(post_data())