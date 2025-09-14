import asyncio
import websockets
import json

async def simulate_client():
    uri = 'ws://localhost:8000/ws/chat/'
    async with websockets.connect(uri) as websocket:
        print('Connnected to server')
        
        message = {'message': 'Hello from a simulated client'}
        await websocket.send(json.dumps(message))
        print('Message sent')
        
        response = await websocket.recv()
        print(f'Received: {response}')
        
        await asyncio.sleep(5)
        
        print('Disconnecting...')

if __name__ == '__main__':
    asyncio.run(simulate_client())
