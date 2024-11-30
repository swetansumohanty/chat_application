from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from . models import Group,Chat
from a_user.models import ChatUser
import json


class MySyncConsumer(SyncConsumer):
    """
    handles the request in concurrent manner and blocks the client while
    one request is processed.
    """
    def websocket_connect(self,event):
        """
        When a connection is open or about to finish handshake.s
        """
        self.gp_name = self.scope['url_route']['kwargs']['groupname']
        # adding channel to new or existing group
        async_to_sync(self.channel_layer.group_add)(
            self.gp_name,                        #group name
            self.channel_name
            )

        # for sending data to client
        self.send({
            "type":"websocket.accept"
        })

    def websocket_receive(self,event):
        """
        executes when server receives a message from the client.
        """
        
        data = json.loads(event['text'])    # converting string to python object(dict)
        
        # finding group object
        group = Group.objects.get(name=self.gp_name)
    
        if data['msg']:            
            # chat object
            chat = Chat(
                chat_user = data['sender'],
                content = data['msg'],
                group = group
            )
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
                self.gp_name,
                {
                    "type":"chat.message",     # it sends message to groups
                    "text":event["text"]
            }
            )
        
    def chat_message(self,event):           # sends message to clients
       
        # sending message
        self.send({
            "type":"websocket.send",
            "text":event["text"]
        })

    def websocket_disconnect(self,event):
        """
        executes when a connection is about to lost or disconnected.
        """     
        async_to_sync(self.channel_layer.group_discard)(
            self.gp_name,               #group name
            self.channel_name
            )
        raise StopConsumer()
       

class MyAsyncConsumer(AsyncConsumer):
    """
    handles the request simultaneously and does not blocks the client while
    one request is processed.
    """
    async def websocket_connect(self,event):
        """
        When a connection is open or about to finish handshake.
        """
        self.gp_name = self.scope['url_route']['kwargs']['groupname']
        # adding channel to new or existing group
        await self.channel_layer.group_add(
            self.gp_name,          #group name
            self.channel_name
            )

        # for sending data to client
        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self,event):
        """
        executes when server receives a message from the client.
        """
        data = json.loads(event['text'])    # converting string to python object(dict)
        # finding group object
        group = await database_sync_to_async(Group.objects.get)(name=self.gp_name)    # as django ORM is a synchronours code 

        if data['msg']:       
            # chat object
            chat = Chat(
                content = data['msg'],
                group = group,
                c_user = data['sender']
            )
            await database_sync_to_async(chat.save)()

            await self.channel_layer.group_send(
                self.gp_name,
                {
                    "type":"chat.message",     # it sends message to groups
                    "text":event["text"]
            }
            )
        
    async def chat_message(self,event):           
        """
        sends message to clients.
        """
        # sending message
        await self.send({
            "type":"websocket.send",
            "text":event["text"]
        })

    async def websocket_disconnect(self,event):
        """
        executes when a connection is about to lost or disconnected.
        """     
        await self.channel_layer.group_discard(
            self.gp_name,                           #group name
            self.channel_name
            )
        raise StopConsumer()
       