import asyncio
import time


async def f1():
    for i in range(5):
        print(f'f1 {i}')
        await asyncio.sleep(1.5)


async def f2():
    for i in range(5):
        print(f'f2 {i}')
        await asyncio.sleep(1)


async def f3():
    for i in range(10):
        print(f'f2 {i}')
        await asyncio.sleep(1.2)


async def main():
    await asyncio.gather(
        # *[f1() for _ in range(100000)]
        f1(),
        f2(),
        f3(),
    )


start = time.time()
asyncio.run(main())
end = time.time()

time = end - start
print(f'{time:.2f}')

# sync 12.60 s
# async 7.54 s
# async with 3-rd f 12.03 s
# async f1 100000 times 19.78 s
