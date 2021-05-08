import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()
    from mailer import Mailer
    mailer = Mailer()
    mailer.send_mail("Test name", "tony.lbvre@gmail.com", "Test subject", "content")

