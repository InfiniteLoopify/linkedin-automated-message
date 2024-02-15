import time
import traceback

from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager, ChromeDriver
from selenium_stealth import stealth


class LinkedinScraper:
    def __init__(self) -> None:
        self.driver = self._get_driver()

    def _get_driver(self):
        ua = UserAgent()  # 1
        random_agent = ua.random  # 1
        fixed_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"""  # 1

        options = webdriver.ChromeOptions()  # 1
        options.add_argument("start-maximized")  # 1

        options.add_argument(f"user-agent={fixed_agent}")  # 1
        # options.add_argument(f"user-agent={random_agent}")
        options.add_argument("disable-infobars")  # 1
        options.add_argument("--disable-extensions")  # 1
        options.add_argument("--disable-gpu")  # 1
        options.add_argument("--disable-dev-shm-usage")  # 1
        options.add_argument("--no-sandbox")  # 1
        options.add_argument("--incognito")  # 1
        # options.add_argument("--headless")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 1
        options.add_experimental_option("useAutomationExtension", False)  # 1

        service = Service(ChromeDriverManager().install())  # 1
        driver = webdriver.Chrome(service=service, options=options)  # 1

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )  # 1

        driver.implicitly_wait(4)  # 1
        driver.maximize_window()  # 1
        return driver

    def login(self, email: str, password: str):
        if not self.driver:
            return

        link = "https://www.linkedin.com/login"
        try:
            self.driver.get(link)
            self.driver.implicitly_wait(6)

            time.sleep(1)

            email_box = self.driver.find_element(By.XPATH, "//input[@id='username']")
            password_box = self.driver.find_element(By.XPATH, "//input[@id='password']")

            email_box.send_keys(email)
            time.sleep(1)
            password_box.send_keys(password)
            time.sleep(1)

            sign_in = self.driver.find_element(
                By.XPATH, '//*[@id="organic-div"]/form/div[3]/button'
            )
            sign_in.click()
            time.sleep(1)
        except Exception as e:
            print(traceback.format_exc())

    def send_message(self, recipient: str, message: str):
        if not self.driver:
            return

        link = "https://www.linkedin.com/messaging/thread/new/"
        try:
            self.driver.get(link)
            self.driver.implicitly_wait(6)

            time.sleep(3)

            search_name = self.driver.find_element(
                By.XPATH,
                '//input[contains(@class, "msg-connections-typeahead__search-field")]',
            )
            for name_part in recipient.split():
                search_name.send_keys(f"{name_part} ")
                time.sleep(1)
            time.sleep(2)

            search_name.send_keys(Keys.RETURN)
            message_box = self.driver.find_element(
                By.XPATH,
                '//form[contains(@class, "msg-form")]/div[3]/div/div[1]/div[1]/p',
            )
            message_box.send_keys(message)
            time.sleep(3)

            send_button = self.driver.find_element(
                By.XPATH,
                '//form[contains(@class, "msg-form")]/footer/div[2]/div[1]/button',
            )
            send_button.click()

            time.sleep(8)

        except Exception as e:
            print(traceback.format_exc())

    def logout(self):
        if not self.driver:
            return

        link = "https://www.linkedin.com/m/logout"
        try:
            self.driver.get(link)
            self.driver.implicitly_wait(4)
            time.sleep(4)
        except Exception as e:
            print(traceback.format_exc())
