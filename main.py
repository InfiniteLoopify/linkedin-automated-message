from scraper import LinkedinScraper
import utils


def main():
    cred_file = "credentials.json"
    email, password = utils.get_creds(cred_file)

    recipient = "Maarij Ahmed Khan"
    message = """
Hello Maarij!
How are you.
I hope you are doing fine.
"""

    scraper = LinkedinScraper()
    scraper.login(email=email, password=password)
    scraper.send_message(recipient=recipient, message=message)
    scraper.logout()


if __name__ == "__main__":
    main()
