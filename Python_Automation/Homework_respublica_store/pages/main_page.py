from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.respublica.ru/'



    """locators"""

    loc_autorization_button = '//a[@title="Авторизоваться"]'
    loc_profile_button = '//div[@class="nr-header__user-nav-item nr-header__user-nav-item--user nr-header__user-nav-item--logged"]'
    loc_login = '//input[@id="sign-in-login"]'
    loc_password = '//input[@id="sign-in-password"]'
    loc_enter_button = '//button[@title="Войти"]'
    loc_catalog_button = '//button[@class="nr-header__burger-desktop"]'
    loc_catalog_book = '//div[@class="categories-root"]/div/a[contains(text(), "Книги")]'
    loc_catalog_book_bestsellers = '//div[@class="category-children-item computed-span-2"]/a[contains(text(), "Бестселлеры")]'
    section_name = '(//h1[@class="title font-medium text-2xl leading-7 text-black p-0 m-0 mb-4 px-5 lg:px-0"])'

    """Getters"""

    def get_loc_autorization_button(self): #получение локатора кнопки авторизации
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_autorization_button)))

    def get_loc_profile_button(self): #получение локатора кнопки профиля
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_profile_button)))

    def get_loc_login(self): #получение локатора поля логина
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_login)))

    def get_loc_password(self): #получение локатора поля пароля
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_password)))

    def get_loc_enter_button(self): #получение локатора кнопки входа
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_enter_button)))

    def get_loc_catalog_button(self): #получение локатора кнопки входа
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_catalog_button)))

    def get_loc_catalog_book(self): #получение локатора строки меню - книги
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_catalog_book)))

    def get_loc_catalog_book_bestsellers(self): #получение локатора строки каталока - бестселлеры
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_catalog_book_bestsellers)))

    def get_section_name(self): #получение локатора строки каталока - бестселлеры
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.section_name)))

    """Actions"""

    def click_autorization_button(self):
        self.get_loc_autorization_button().click()
        print('Click autorization button')

    def input_login(self,login):
        self.get_loc_login().send_keys(login)
        print('Input login')

    def input_password(self,password):
        self.get_loc_password().send_keys(password)
        print('Input password')

    def click_enter_button(self):
        self.get_loc_enter_button().click()
        print('Click enter button')

    def click_catalog_button(self):
        self.get_loc_catalog_button().click()
        print('Click catalog button')

    def move_to_catalog_book(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_loc_catalog_book()).perform()  # наведение на строку "книги"
        print('Moved on catalog book')

    def click_catalog_book_bestseller(self):
        self.get_loc_catalog_book_bestsellers().click()
        print('Click link bestseller')


    """Methods"""

    def autorization(self):
        self.driver.get(self.url) #переход на сайт
        self.driver.maximize_window() #раскрытие окна на полный экран
        self.get_current_url() #функция получения текущего url
        self.click_autorization_button() #клик по кнопке авторизации
        self.input_login(login='ae.semenova17@gmail.com') #ввод логина
        self.input_password(password='testpass') #ввод пароля
        self.click_enter_button() #клик по кнопке входа
        try:
            self.assert_word(self.get_loc_profile_button(), 'А') #проверка содержания кнопки профиля
            print('Autorization success')
        except:
            print('Autorization failed')

    def navigation_catalog_to_bestsellers(self):
        self.click_catalog_button() #клик по кнопке каталога
        self.move_to_catalog_book() #наведение на строку меню книги
        self.click_catalog_book_bestseller() #клик по строке бестселлеры
        self.assert_word(self.get_section_name(), 'Книги бестселлеры')






