# Example of a potential pitfall with synchronous testing
import asyncio
import time
import unittest

async def process_data(data):
	await asyncio.sleep(1)
	return data.upper()

class TestMyCode(unittest.TestCase):
	def test_processing_time(self):
		start = time.time()
		asyncio.run(process_data("hello"))
		duration = time.time() - start
		self.assertLess(duration, 0.2)  # This test might fail inconsistently

if __name__ == "__main__":
	unittest.main()
