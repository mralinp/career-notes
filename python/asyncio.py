import asyncio
import time


async def make_coffee():
    
    await asyncio.sleep(10)
    
    return "java"

async def make_cheese_cake():
    
    await asyncio.sleep(5)
    
    return "cheesecake"

async def main():
    start = time.time()
    breakfast_batch = asyncio.gather(make_coffee(), make_cheese_cake())
    coffee, cake = await breakfast_batch
    # or 
    # coffee_task = asyncio.create_task(make_coffee())
    # cake_task = asyncio.create_task(make_cheese_cake())
    # coffee = await coffee_task
    # cake_task = await cake_task
    end = time.time()
    
    elapsed_time = end - start
    
    print(f"Your breakfast is ready after: {elapsed_time} seconds")
    
if __name__ == '__main__':
    asyncio.run(main())