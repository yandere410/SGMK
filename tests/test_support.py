from pages.locators import AllLocataors
from pages.login_page import UserData, LoginPage
from pages.support_page import SupportPage


class TestSupport():
    def test_create_ticket(self, driver):
        login_page = LoginPage(driver=driver)
        login_page.authorize()
        support_page = SupportPage(driver=driver)
        support_page.go_support_field()
        support_page.problem_description_textarea(UserData.DESCRIPTION_WRITE.value)
        support_page.send_description()

        assert support_page.is_element_present(AllLocataors.SUCCESS_SEND)

    def test_select_file(file_name, driver):
        login_page = LoginPage(driver=driver)
        login_page.authorize()
        support_page = SupportPage(driver=driver)
        support_page.go_support_field()
        support_page.problem_description_textarea(UserData.DESCRIPTION_WRITE.value)
        support_page.attach_file('unix.pdf')
        support_page.send_description()

        assert support_page.is_element_displayed(AllLocataors.SUPPORT_VALID_FAILED)
