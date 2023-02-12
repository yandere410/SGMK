import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#fixture with preset driver
@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()

