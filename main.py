import os
from dotenv import load_dotenv

from messenger import LinkedinMessenger

load_dotenv()


RECIPIENT = "John Doe"
MESSAGE = """
Hello John,
I am sending you this message through LinkedIn.
Best Regards.
"""


def main():
    EMAIL = os.getenv("LINKEDIN_EMAIL", "")
    PASSWORD = os.getenv("LINKEDIN_PASSWORD", "")

    scraper = LinkedinMessenger()
    scraper.login(email=EMAIL, password=PASSWORD)
    scraper.send_message(recipient=RECIPIENT, message=MESSAGE)
    scraper.logout()


if __name__ == "__main__":
    main()
