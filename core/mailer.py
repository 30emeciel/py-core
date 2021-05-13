import os

from sendgrid import SendGridAPIClient, Cc, From, Subject, To, Content, MimeType
from sendgrid.helpers.mail import Mail


class Mailer:

    def __init__(self):
        self.SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
        self.sg = SendGridAPIClient(self.SENDGRID_API_KEY)

    def send_mail(self, to_name, to_email, subject, html_content):
        message = Mail()
        message.from_email = From("admin@30emeciel.fr", "Coliv'app")
        message.to = To(to_email, to_name)
        message.subject = Subject(subject)
        message.content = Content(
            MimeType.html, html_content)
        response = self.sg.send(message)
        assert response.status_code == 202
        return response


if __name__ == "__main__":

    mailer = Mailer()
    mailer.send_mail("Tony <tony.lbvre@gmail.com>", "Test email", "<strong>hello World!</strong>")

