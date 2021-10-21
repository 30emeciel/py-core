import os
import requests


class DiscordMessageSender:
    def __init__(self):
        self.token = os.environ['DISCORD_TOKEN']
        self.channel_id = os.environ['DISCORD_CHANNEL_ID']

    def send_message(self, txt):
        url = "https://discord.com/api/v9/channels/{channel_id}/messages".format(channel_id=self.channel_id)
        headers = {
            "Authorization": "Bot {token}".format(token=self.token)
        }
        data = {
            "content": txt,
        }
        requests.post(url, data=data, headers=headers)


