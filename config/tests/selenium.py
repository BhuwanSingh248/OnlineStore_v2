import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def chrome_browser_instance(request):
    options = Options()
    # options.binary_location = "SYS_store/chromedriver"
    options.headless = False
    chrome_bin = os.path.abspath(os.curdir) + "/chromedriver"  # python chrome driver
    browser = webdriver.Chrome(chrome_bin, chrome_options=options)
    yield browser
    browser.close()
