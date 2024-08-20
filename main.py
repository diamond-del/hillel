from utils import email_sender

print("From main", __name__)


def main():
    email_sender.send_email(recipients=["evgeny_saprykin@ukr.net"], mail_body="Yo check this pic", mail_subject="Email")


if __name__ == "__main__":
    main()
