from selenium.webdriver import ActionChains
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from datetime import datetime

# # IMPORTS ARE OPTIMIZED, SOME LOOKING AS UNUSED STATEMENT BECAUSE OF EVAL FUNCTION. DO NOT REFACTOR! # #

class Helpers:

    def __init__(self, driver):
        self.driver = driver

    def getElementText(self,element):
        return element.get_attribute("textContent")

    def locateBy(self, method, selector):  # Following syntax must be used when this function is called (Single quote mark and Double quote mark difference) -> locateBy("xpath", f"//label[text()='text']") SYNTAX -> locateBy("method","locator")
        return eval(f'self.driver.find_element_by_{method}("{selector}")')


    def locateAndClick(self, method, selector):
        self.locateBy(method, selector).click()


    def scrollToElement(self, method, selector):
        time.sleep(0.1)
        eval(f'self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_{method}("{selector}"))')


    def hoverOnElement(self, element):
        ActionChains(self.driver).move_to_element(element).perform()


    def waitElementToBeLocated(self, method, selector):
        wait = WebDriverWait(self.driver, 5)
        eval(f'wait.until(ec.visibility_of_element_located((By.{method.upper()}, f"{selector}")))')


    def checkElementExistence(self, method, selector):  # Returns True if element can be located.
        try:
            (self.locateBy(method, selector))
            return True
        except:
            return False


    def save_screenshot(self, filename):  # Captures screenshot of page.
        time.sleep(1) # Sleep for page load.
        now = datetime.now()
        date_string = now.strftime("%d-%m-%Y")
        time_string = now.strftime("%H.%M")
        if not os.path.exists(f'./screenshot/{date_string}'):
            os.makedirs(f'./screenshot/{date_string}')

        self.driver.save_screenshot(f"./screenshot/{date_string}/{time_string}&{filename}.png")
        return(print(f"Screenshot saved as: ./screenshot/{date_string}/{time_string}&{filename}.png"))

    def getText(self, method, selector):  # Returns text content of element.
        return eval(f'self.driver.find_element_by_{method}("{selector}").get_attribute("textContent")')


    def returnChildElements(self, method1, selector1, method2, selector2):  # Returns web element.
        parentElement = eval(f'self.locateBy("{method1}","{selector1}")')
        childElement = eval(f'parentElement.find_elements_by_{method2}("{selector2}")')

        return childElement

    def checkPageValidation(self, **kwargs):  # Usage -> checkPageValidation(by ="By.BrowserTitle", operand ="!=", validate ="Page Not Found", link =link) or checkPageValidation(by ="By.ResponseCode", validate = 200, link =link). Returns True or False.
        operand = None

        for key, value in kwargs.items():
            if key == "by":
                by = value
            elif key == "operand":
                operand = value
            elif key == "validate":
                validate = value
            elif key == "link":
                link = value

        if operand is None:  # Set default operand as '=='.
            operand = "=="

        if by == "By.ResponseCode":

            if eval(f'requests.get(link).status_code {operand} {validate}'):
                return True
            else:
                print(f"Error at link: {link}")
                self.driver.get(link)  # Go to the link to capture screenshot.
                self.save_screenshot(link.split('/')[-1])
                return False

        elif by == "By.BrowserTitle":

            self.driver.get(link)
            if eval(f'self.driver.title {operand} "{validate}"'):
                return True
            else:
                print(f"Error at link: {link}")
                self.save_screenshot(link.split('/')[-1])
                return False
