from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# from django.core.management.base import BaseCommand
# from .consumers import shutdown_message
# import asyncio

class Command(BaseCommand):
    help = 'Broadcasts shutdown message to all connected clients'
    
    def handle(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'chat_group',
            {
                'type': 'server_shutdown',
                'message': 'Server is shutting down. Try reconnecting later'
            }
        )
        self.stdout.write(self.style.SUCCESS('Shutdown message broadcasted'))
