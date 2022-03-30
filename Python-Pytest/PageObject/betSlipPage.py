from Utils.locators import *
from Utils.helpers import *
from Utils.classes import MatchDetail


class BetSlipPage():

    def __init__(self, driver):
        self.driver = driver
        self.helpers = Helpers(driver)

        self.match_names_xpath = Locators.matchNamesXpath
        self.match_times_xpath = Locators.matchTimesXpath
        self.match_ids_xpath = Locators.matchIdsXpath
        self.match_date_xpath = Locators.matchDateXpath
        self.place_bet_xpath = Locators.placeBetXpath
        self.events_on_slip_xpath = Locators.eventsOnSlipXpath

    def getAllMatchesDetails(self):
        matchDetailClasses = []

        matchNames = self.driver.find_elements_by_xpath(self.match_names_xpath)  # Get list of Match Names
        matchTimes = self.driver.find_elements_by_xpath(self.match_times_xpath)  # Get list of Match Times
        matchIds = self.driver.find_elements_by_xpath(self.match_ids_xpath)  # Get list of Match ID's

        for index in range(len(matchNames)):  # Match the values of datas with matches.
            matchDate = self.driver.find_element_by_xpath(
                self.match_date_xpath.replace("index", str(index + 1))).get_attribute(
                "textContent")

            matchTime = matchTimes[index].get_attribute("textContent")

            # Create a Match Detail Class #
            match = MatchDetail()
            match.id = matchIds[index].get_attribute("textContent")
            match.date = f"{matchDate} {matchTime.rstrip(' ')}"
            match.name = matchNames[index].get_attribute("textContent")

            matchDetailClasses.append(match)  # Append all the match detail classes into a list.

        return matchDetailClasses  # Return the list that contains match detail classes.

    def placeBet(self, matchIndex, betType,
                 bet):  # Allows testing of any kind of betting. Example Usage : self.placeBet(1, O/U 2.5, Over)
        betType = self.convertBetSelection(betType)
        place_bet_xpath = self.place_bet_xpath.replace("matchIndex", str(matchIndex + 1)).replace("BET_SELECTION",
                                                                                                  f"{bet}{betType}")
        self.driver.find_element_by_xpath(place_bet_xpath).click()

    def convertBetSelection(self, betType):  # Adjust the Bet Type in order to Match the HTML Content
        betType = betType.upper()
        if betType == "1X2":
            return "1X2"
        elif betType == "DC":
            return "Double Chance"
        elif betType == "O/U 2.5":
            return "Over/Under 2.5"
        elif betType == "GG/NG":
            return "GG/NG"
        else:
            raise Exception("Invalid Bet")

    def placeBetOnAll(self, betType, bet):  # Try to bet on 99 matches with given parameters.

        for x in range(99):
            try:
                self.placeBet(x, betType, bet)
            except:
                break

    def getSlipItems(self):  # Returns all of the events required data for assertion at Bet Slip.
        slipItems = self.driver.find_elements_by_xpath(self.events_on_slip_xpath)

        slipTexts = []
        for element in slipItems:
            text = self.helpers.getElementText(element)
            slipTexts.append(text)

        slipTexts = slipTexts[::-1]  # Reverse the slip items to match the class order.

        return slipTexts



