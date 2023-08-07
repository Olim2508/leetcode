import asyncio


async def test():
    print("Printing 1")
    await asyncio.sleep(1)
    print("Printing 2")


async def main():
    await asyncio.gather(test(), test())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

