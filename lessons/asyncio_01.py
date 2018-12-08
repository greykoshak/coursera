import asyncio

async def hello_world():
    while True:
        print("Hello, World!")
        await asyncio.sleep(2.3)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
	
