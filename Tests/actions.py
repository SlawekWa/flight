from selenium import webdriver
from Pages.searchPage import SearchPage
from selenium.webdriver.common.keys import Keys
import unittest

class SearchFlights(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path=r'C:\Users\SG0304762\OneDrive - Sabre\Documents\PRV\GIT\drivers\geckodriver.exe')
        cls.driver.implicitly_wait(2)

    def test_search_for_flight(self):
        driver = self.driver
        driver.get('https://www.skyscanner.pl/')

        search = SearchPage(driver)
        search.set_market("KRK", "TXL")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
