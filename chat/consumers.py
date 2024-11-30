import json
import weakref
from channels.generic.websocket import AsyncWebsocketConsumer
from . models import ChatModel
from channels.db import database_sync_to_async


class PersonalChatConsumer(AsyncWebsocketConsumer):
    """
    it is Generic WebSocket Consumer and it handles multiple request simultaneously,
    (e.g both synchronous and asynchronous).
    """

    async def connect(self):
        """
        when the connection is open or about to finish a handshake.
        """
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        print(self.scope['user'],my_id)
        print(self.scope['url_route']['kwargs'])
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name
        

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
       

    async def receive(self, text_data=None, bytes_data=None):
        """
        executes when a message is received from a client.
        """
        data = json.loads(text_data)    # Converting json string to Python obj.
        if data['message']:
            message = data['message']
            username = data['username']
            await self.save_message(username, self.room_group_name, message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                }
            )

    async def chat_message(self, event):
        """
        send message to each client.
        """
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
       
    async def disconnect(self, code):
        """
         executes when a connection is about to be lost or disconnected.
        """
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_message(self, username, thread_name, message):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name)
        


