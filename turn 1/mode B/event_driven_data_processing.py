import asyncio

# A fictional event loop or data source
class EventLoop:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def put(self, data):
        await self.queue.put(data)

    async def get(self):
        return await self.queue.get()

# Simple data processing function
async def process_data(data):
    await asyncio.sleep(0.1)  # Simulate processing time
    return data.upper()

async def main(event_loop):
    while True:
        data = await event_loop.get()
        result = await process_data(data)
        print(f"Processed data: {result}")

if __name__ == "__main__":
    event_loop = EventLoop()
    asyncio.run(main(event_loop))
    event_loop.put("hello")
    event_loop.put("world")
