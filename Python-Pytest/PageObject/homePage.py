from Utils.locators import *
from Utils.helpers import *
import time
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.main_menu_elements_xpath = Locators.mainMenu_xpath
        self.search_box_xpath = Locators.searchBox_xpath
        self.search_result_container_xpath = Locators.searchResultContainer_xpath
        self.matches_xpath = Locators.matches_xpath


    def navigateToMenuPage(self, menuPageName):
        menuElems = self.driver.find_elements_by_xpath(self.main_menu_elements_xpath)

        for menuElem in menuElems:
            if menuElem.get_attribute("textContent").lower() == menuPageName.lower():
                menuElem.click()
                break

    def searchEvent(self, eventName):
        self.driver.find_element_by_xpath(self.search_box_xpath).send_keys(eventName)

    def selectEvent(self, eventOrder):

        search_results = self.driver.find_elements_by_xpath(f"{self.search_result_container_xpath}{self.matches_xpath}")
        search_results[eventOrder-1].click()