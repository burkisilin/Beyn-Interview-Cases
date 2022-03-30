mainMenuClassName = 'nvs-products-menu'
mainMenuElementClassName = 'ng-star-inserted'

class Locators:
    # # Home Page Locators # #

    mainMenu_xpath = f"//ul[@class='{mainMenuClassName}']/li[@class='{mainMenuElementClassName}']"
    sportsPageMenuButton_xpath = "//a[text()='Sport']"
    searchBox_xpath = "//input[@placeholder='Find Events, Tournaments or Categories']"
    searchResultContainer_xpath = "//tab[@class='active tab-pane ng-star-inserted']"
    matches_xpath = "//div[@class='result-row card ng-star-inserted']"

    
    # # BetSlip Page Locators # #

    matchNamesXpath = "//td[contains(@class,'event-name')]"
    matchTimesXpath = "//td[contains(@class,'time')]"
    matchIdsXpath = "//td[contains(@class,'code')]"

    matchDateXpath = "(//td[contains(@class,'event-name')])[index]//ancestor::table//th[@colspan='4']"
    placeBetXpath = "(//td[contains(@class,'event-name')])[matchIndex]//parent::tr//td[contains(@class,'BET_SELECTION')]"

    eventsOnSlipXpath = "//div[@class='event-name']"
