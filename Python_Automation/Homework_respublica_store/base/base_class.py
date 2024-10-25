from datetime import datetime
from selenium.webdriver import ActionChains

""" Базовый класс, содержащий универсальные методы """
class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Method assert word"""
    def assert_word(self, word, result):
        value_world = word.text
        assert value_world == result



    """Method make screenshot"""
    def screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")  # ,текущая дата
        name_screenshot = f'screenshot_{now_date}.png'  # переменная для имени скриншота
        self.driver.save_screenshot(f".\\screens\\{name_screenshot}")  # создание скриншота
        print(name_screenshot, 'created')

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url
        print('Get value url')

    """Method move to elements"""
    def move_to_elements(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()





