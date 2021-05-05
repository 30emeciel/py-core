import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Mailer:

    def __init__(self):
        self.SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
        self.sg = SendGridAPIClient(self.SENDGRID_API_KEY)

    def send_mail(self, to_name, to_email, subject, html_content):
        message = Mail(
            from_email="Coliv'app <admin@30emeciel.fr>",
            to_emails=f"{to_name} <{to_email}>",
            subject=subject,
            html_content=html_content
        )

        response = self.sg.send(message)
        assert response.status_code == 202
        return response


if __name__ == "__main__":

    mailer = Mailer()
    mailer.send_mail("Tony <tony.lbvre@gmail.com>", "Test email", "<strong>hello World!</strong>")

