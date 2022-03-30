import pytest

from PageObject.homePage import HomePage
from PageObject.betSlipPage import BetSlipPage
from Base.base import Base

import pytest_check as check
from Utils.helpers import *

import time

@pytest.mark.usefixtures('set_up')
class Test_corebet(Base):


    def test_betSlipEventTimes(self):
        driver = self.driver

        homePage = HomePage(driver)
        betPage = BetSlipPage(driver)
        helpers = Helpers(driver)

        homePage.navigateToMenuPage("Sport")  # Navigate To Sport Page
        helpers.save_screenshot("PageNavigation")

        homePage.searchEvent("HataySpor")  # Search event
        helpers.save_screenshot("EventSearch")

        homePage.selectEvent(1)  # Select the event (1 is the first one that appears)
        helpers.save_screenshot("EventChosen")


        matchDetailClasses = betPage.getAllMatchesDetails()  # Get all the match detail classes which are includes required data for assertion.
        betPage.placeBetOnAll("1X2", "1")  # Places the bets with given setting.
        helpers.save_screenshot("BetsPlaced")

        slipTexts = betPage.getSlipItems()  # Get all of the events required data for assertion at Bet Slip.

        # SOFT ASSERTIONS #
        for matchClass, slipText in zip(matchDetailClasses, slipTexts):
            formattedText = f"{matchClass.id.rstrip(' ')}{matchClass.date}{matchClass.name}".rstrip(" ")  # Reformat the match detail class data to match texts with slip text.

            check.is_true(formattedText == slipText)

