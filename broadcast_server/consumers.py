from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .redis_client import redis_client
import json
from datetime import datetime


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('chat_group', self.channel_name)
        await self.accept()

        redis_client.sadd('connected_clients', self.channel_name)
        redis_client.hset(f'Client: {self.channel_name}', mapping={
            'connected_at': str(datetime.utcnow()),
            'username': 'Anonymus'
        })
        # print(f'Connected: ', self.channel_name)
        print(f'websocket connected: {self.channel_name}')


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('chat_group', self.channel_name)
        redis_client.srem('connected_clients', self.channel_name)
        redis_client.delete(f'client:{self.channel_name}')
        print(f'Disconnected: {self.channel_name}')

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get('message', '')
            user = data.get('user', 'Anonymus')
            
            if not message:
                await self.send_json({'error': 'Missing message field'})
                return
            
            await self.channel_layer.group_send('chat_group', {'type': 'chat_message', 'user': user, 'message': message})
        
        except json.JSONDecodeError:
            await self.send_json({'error': 'Invalid JSON format'})
        
        except Exception as e:
            await self.send_json({'error': f'Unexpected error: {str(e)}'})

# class ChatConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.channel_layer.group_add('chat_group', self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard('chat_group', self.channel_name)

    # async def receive(self, text_data):
    #     try:
    #         data = json.loads(text_data)
    #         message = data.get('message', None)
    #         user = data.get('user', 'Anonymus')

    #         if not message:
    #             await self.send_json({'error': 'Missing message field'})
    #             return

    #         await self.channel_layer.group_send('chat_group',{'type': 'chat_message',
    #             'user': user, 'message': message
    #             })

    #     except json.JSONDecodeError:
    #         await self.send_json({'error': 'Invalid JSON format'})
    #     except Exception as e:
    #         await self.send_json({'error': f'Unexpected error: {str(e)}'})

    async def chat_message(self, event):
        await self.send_json({
            'message': event['message']
        })
