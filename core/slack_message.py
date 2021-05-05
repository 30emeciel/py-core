import os

from slack_sdk import WebClient


class SlackSender:
    def __init__(self):
        self.client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
        self.channel = os.environ['SLACK_CHANNEL']

    def send_slack_message(self, txt):
        self.client.chat_postMessage(
            channel=self.channel,
            text=txt,
            unfurl_links=False,
            unfurl_media=False,
            link_names=False,
        )
