from scraper import LinkedinScraper
import utils


def main():
    cred_file = "credentials.json"
    email, password = utils.get_creds(cred_file)

    recipient = "Jordan Anthus"
    message = """
Hi Jordan,

This message is generated automatically using a script. The script sends message automatically to a Linkedin user.
I have attached the Github link for this script below.

Link: https://github.com/InfiniteLoopify/linkedin-automated-message

Regards,
Umair Shahab
"""

    scraper = LinkedinScraper()
    scraper.login(email=email, password=password)
    scraper.send_message(recipient=recipient, message=message)
    scraper.logout()


if __name__ == "__main__":
    main()
