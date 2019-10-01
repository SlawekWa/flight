from Locators.searchPageLocators import SearchPageLocators
from selenium import webdriver

class SearchPage():

    #WebElement elementName = driver.findElement(By.LocatorStrategy("LocatorValue"));
    #form_element = driver.find_element_by_xpath("/html/body/form[1]")

    def __init__(self, driver):
        self.driver = driver
        self.origin_input = driver.find_element_by_xpath(SearchPageLocators.origin_input_xpath)
        self.destination_input = driver.find_element_by_xpath(SearchPageLocators.destination_input_xpath)

    def set_market(self, orig, dest):
        self.origin_input.send_keys(orig)
        self.destination_input.send_keys(dest)