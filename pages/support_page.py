from .base_page import BasePage
from .locators import AllLocataors
from resources import files
from selenium.webdriver.common.keys import Keys


class SupportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #function for closing popup and go to the ticket writing page
    def go_support_field(self):
        close_popup = self.find_element(AllLocataors.CLOSE_POP_UP)
        self.is_element_displayed(AllLocataors.CLOSE_POP_UP)
        close_popup.click()
        tech = self.find_element(AllLocataors.SUPPORT_CLICK)
        tech.click()

    
    #for chose category of ticket
    def global_field(self):
        common_ticket = self.find_element(AllLocataors.GENERAL_BUTTON)
        common_ticket.click()
    
    #for select ticket area and write description
    def problem_description_textarea(self, popup):
        textarea = self.find_element(AllLocataors.DESCRIPTION)
        textarea.send_keys(popup)

    #click send button
    def send_description(self):
        save_submit = self.find_element(AllLocataors.BUTTON_SAVE)
        save_submit.click()
    #select file for testing unvalid request
    def attach_file(self, file_name):
        attachment = self.find_element(AllLocataors.FILE_INPUT)
        attachment.send_keys(files.to_resource(f'{file_name}'))  
