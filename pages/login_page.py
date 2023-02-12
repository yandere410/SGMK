from .base_page import BasePage


from .locators import AllLocataors
from enum import Enum


#data input
class UserData(Enum):
    LOGIN = 'support@gmail.com'
    PASSWORD = 'Zz!123456'
    INCORRECT_PASSWORD = 'Zz!123455'
    DESCRIPTION_WRITE = 'Help me'

#funcitons for select fields and input login password
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def set_login(self, login):
        login_input = self.find_element(AllLocataors.LOGIN_FIELD)
        login_input.send_keys(login)
        return self


    def set_password(self, password):
        password_input = self.find_element(AllLocataors.PASSWORD_FIELD)
        password_input.send_keys(password)
        return self

#click enter field
    def submit_login(self):
        baton = self.find_element(AllLocataors.SUBMIT_BUTTON)
        baton.click()
        return self

#authorization for support test
    def authorize(self):
        self.open()
        self.set_login(UserData.LOGIN.value)
        self.set_password(UserData.PASSWORD.value)
        self.submit_login()

