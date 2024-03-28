import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class SendMails:
    def gmail_credentials(self):
        try:
            creds = Credentials.from_authorized_user_file('token.json')
        except FileNotFoundError:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                ['https://www.googleapis.com/auth/gmail.send']
            )
            creds = flow.run_local_server(port=0)

        if creds and creds.valid:
            pass

        elif creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

        return creds

    def gmail_compose(self, mail_subject, email_recipient, mail_body):
        message = {
            'raw': base64.urlsafe_b64encode(
                f'MIME-Version: 1.0\n'
                f'Content-Type: text/html; charset="UTF-8"\n'
                f"From: [VALUE]\n"
                f"To: {email_recipient}\n"
                f"Subject: {mail_subject}\n\n"
                f"{mail_body}"
                .encode("utf-8")
            ).decode("utf-8")
        }
        return message

    def gmail_send(self, creds, message):
        service = build('gmail', 'v1', credentials=creds)
        service.users().messages().send(userId='me', body=message).execute()

    def send_mail(self, email_to, email_subject, email_body):
        credentials = self.gmail_credentials()
        mail_content = self.gmail_compose(email_subject, email_to, email_body)
        self.gmail_send(credentials, mail_content)
