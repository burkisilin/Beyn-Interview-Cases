import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:



    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initializing Chrome driver")
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/Users/chromedriver.exe")  # Specify your chrome path here if you don't have added it to global variables.
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.core.bet/")

        yield self.driver

        if self.driver is not None:
            print("-----------------------------------------")
            print("Test is finished")
            self.driver.close()
            self.driver.quit()

