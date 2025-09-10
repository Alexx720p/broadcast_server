import asyncio
import websockets
import json


async def simulate_user(user_id):
    uri = 'ws://localhost:8000/ws/chat/'
    try:
        async with websockets.connect(uri) as websocket:
            message = {
                'message': f'Hello from user_{user_id}'
            }
            await websocket.send(json.dumps(message))
            response = await websocket.recv()
            print(f'Received: {response}')

            response = await websocket.recv()
            print (f'user_{user_id} receiver: {response}')

            await asyncio.sleep(5)

    except Exception as e:
        print(f'user_{user_id} error: {e}')

async def main():
    users = [simulate_user(i) for i in range(1,6)]
    await asyncio.gather(*users)

if __name__ == '__main__':
    asyncio.run(main())