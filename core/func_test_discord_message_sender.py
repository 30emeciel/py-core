import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()
    from discord_message_sender import DiscordMessageSender
    message_sender = DiscordMessageSender()
    message_sender.send_message("Hello World!")

