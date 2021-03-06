# The code for the chat consumer that is responsible for managing WebSocket connections and sending messages
# over was added when following the Django Channels tutorial linked below
# http://channels.readthedocs.io/en/latest/tutorial/part_3.html

from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
	# A channel is where messages are sent to
	# Anyone with the channel name can send messages to the channel
	# A group is a collection of related channels
	# Anyone with the group name add/remove a channel and send messages to the channels in the group

	# The ChatConsumer will add its channel to the group (which is the room name)
	# to talk to other ChatConsumers in the group (room)

	# Channel is a user, Group is a chat room

	async def connect(self):
		# Get the room name from URL and construct a channel
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name

		# Join the group with the room name
		await self.channel_layer.group_add(
			self.room_group_name,
			self.channel_name
		)

		# Accept WebSocket connection
		await self.accept()

	async def disconnect(self, close_code):
		# Removes channel from the group
		await self.channel_layer.group_discard(
			self.room_group_name,
			self.channel_name
		)

	# User sends a message which is sent over WebSocket (WebSocket receives a message)
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']

		# Send a message to the group
		# All the channels in the group will receive it
		await self.channel_layer.group_send(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message
			}
		)

	# Receive message from group sent by a channel in the group
	async def chat_message(self, event):
		message = event['message']

		# Send message over WebSocket which will be added to the chat log
		await self.send(text_data=json.dumps({
			'message': message
		}))