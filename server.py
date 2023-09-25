
import asyncio
from websockets.server import serve
positions = {}
names = []
running = True
async def echo(websocket):
    async for message in websocket:
        r = message.split(" ")
        positions[r[2]] = [int(r[0]), int(r[1])]
        if not r[2] in names:
            names.append(r[2])
        d = ""
        for i in names:
            d+= f"k{positions[i][0]} {positions[i][1]} {i}"
        await websocket.send(d)
async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever
    
asyncio.run(main())
