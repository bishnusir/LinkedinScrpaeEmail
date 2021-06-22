from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from constants import DRIVER_PATH, MAX_WAIT



class WebDriver:
    """
    Higher Level class for chrome webdriver
    """
    __driver = webdriver.Chrome(DRIVER_PATH)
    __driver.maximize_window()

    @property
    def currentURL(self):
        """returns focused tab url"""
        return self.__driver.current_url

    def load_url(self, url):
        """loads url into chrome driver"""
        print(url)
        self.__driver.get(url)
    
    def focus_to_element(self, element):
        """scrolls to specific element"""
        self.__driver.execute_script('arguments[0].scrollIntoView(true);', element)
    
    def find_element(self, element_search_string, method='xpath'):
        """finds element by identifier(like id value, xpath value) and method(like id, xpath)"""
        # self.validate_method(method)
        wait = 0
        while wait< MAX_WAIT:
            try:
                element = getattr(self.__driver, f'find_element_by_{method}')(element_search_string)
                return element
            except Exception as e:
                # print("waiting element to load ")
                time.sleep(2)
                wait += 2
                continue
        raise Exception(f"Max wait time over element {element_search_string} not found through {method}")
                
    def find_elements(self, element_search_string, method='xpath'):
        """finds elements by identifier(like id value, xpath value) and method(like id, xpath)"""
        # self.validate_method(method)
        wait = 0
        while wait< MAX_WAIT:
            try:
                element = getattr(self.__driver, f'find_elements_by_{method}')(element_search_string)
                return element
            except Exception as e:
                print("waiting element to load ")
                time.sleep(2)
                wait += 2
                continue
        raise Exception(f"Max wait time over element {element_search_string} not found through {method}")
        
    def page_source(self):
        """returns entire web page source"""
        data = BeautifulSoup(self.__driver.page_source, features="html.parser")
        return data