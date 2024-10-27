from datetime import datetime
from selenium.webdriver import ActionChains

""" Базовый класс, содержащий универсальные методы """
class Base():
    def __init__(self, driver):
        self.driver = driver

    """Метод получения текущего url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Метод сопоставления текста"""
    def assert_word(self, word, result):
        value_world = word.text
        assert value_world == result

    """Метод создания скриншота"""
    def screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'
        self.driver.save_screenshot(f".\\screens\\{name_screenshot}")
        print(name_screenshot, 'created')

    """Метод сверки url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url
        print('Get value url')

    """Метод перемещения к элементу"""
    def move_to_elements(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()





