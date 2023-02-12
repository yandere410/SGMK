from pages.login_page import UserData, LoginPage
from pages.locators import AllLocataors


class TestLoginPage():
    def test_successful_login(self, driver):
        main_page = LoginPage(driver=driver)
        main_page.open()
        main_page.set_login(UserData.LOGIN.value)
        main_page.set_password(UserData.PASSWORD.value)
        main_page.submit_login()
        assert main_page.is_element_present(AllLocataors.WELCOME_HEADER)


    def test_login_validation_error(self, driver):
        main_page = LoginPage(driver=driver)
        main_page.open()
        main_page.set_login(UserData.LOGIN.value)
        main_page.set_password(UserData.INCORRECT_PASSWORD.value)
        main_page.submit_login()
        assert main_page.is_element_present(AllLocataors.LOGIN_ERROR)

