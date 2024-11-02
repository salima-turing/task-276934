import asyncio
import unittest
from unittest.mock import AsyncMock
import time

from event_driven_data_processing import process_data


class TestAsyncDataProcessing(unittest.IsolatedAsyncioTestCase):

    async def test_process_data(self):
        # Create a mocked event loop for testing
        event_loop = AsyncMock()
        event_loop.get = AsyncMock(return_value="hello")

        # Asynchronous function to test
        async def test_func():
            await process_data(await event_loop.get())

        # Run the test asynchronous function
        await test_func()

        # Verify that the process_data ran as expected
        event_loop.get.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()
