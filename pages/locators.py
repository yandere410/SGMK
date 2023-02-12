from selenium.webdriver.common.by import By

#locator storage
class AllLocataors():
    LOGIN_FIELD = (By.CSS_SELECTOR,'#input-21')
    PASSWORD_FIELD = (By.CSS_SELECTOR,'#input-25')
    SUBMIT_BUTTON = (By.CSS_SELECTOR,'._input-group._input-group__buttons-row button')
    STOP_WORD = (By.CSS_SELECTOR,'.label-container__text-right')
    SUPPORT_CLICK = (By.XPATH, '//span[contains(text(),"Техподдержка")]')
    WELCOME_HEADER = (By.CSS_SELECTOR,'.page-title-line.mb-5')
    LOGIN_ERROR = (By.CSS_SELECTOR, '.v-snack__content:nth-child(1)')
    SUPPORT_PIC = (By.CSS_SELECTOR, '.v-list-item__title')
    DESCRIPTION = (By.CSS_SELECTOR, 'textarea[id^="input"]')
    BUTTON_SAVE = (By.CSS_SELECTOR, 'button.ml-2')
    SUCCESS_SEND = (By.XPATH, '//div[contains(text(),"заявка зарегистрирована")]')
    CLOSE_POP_UP = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div[4]')
    GENERAL_BUTTON = (By.CSS_SELECTOR, '.v-select__selections')
    GENERAL_OPEN = (By.CSS_SELECTOR, '.v-list-item__title')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[type="file"]')
    SUPPORT_VALID_FAILED = (By.XPATH, '//span[contains(text(),"Заявка не создана")]')