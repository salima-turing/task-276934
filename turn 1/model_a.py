import asyncio
import pytest


# Asynchronous data processor
async def process_data(queue: asyncio.Queue):
    while True:
        data = await queue.get()
        try:
            processed_data = data.upper()
            print(f"Processed: {processed_data}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            queue.task_done()


@pytest.mark.asyncio
async def test_asynchronous_data_processing():
    queue = asyncio.Queue()
    consumer_task = asyncio.create_task(process_data(queue))

    # Test data items
    test_data = ["hello", "python", "asyncio", "testing"]

    # Put data items into the queue
    for item in test_data:
        await queue.put(item)

    # Wait for all data to be processed
    await queue.join()

    # Cancel the consumer task
    consumer_task.cancel()
    await consumer_task


if __name__ == "__main__":
    asyncio.run(test_asynchronous_data_processing())
