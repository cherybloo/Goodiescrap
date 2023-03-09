import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page,time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        options=Options()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        options.add_experimental_option("detach",True)
        url='http://www.python.org'
        PATH='chromedriver.exe'
        self.driver=webdriver.Chrome(PATH,chrome_options=options)
        self.driver.get(url)
        
    def test_search_python(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element="pycon"
        mainPage.click_go_button()
        search_result_page=page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        time.sleep(10)
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()