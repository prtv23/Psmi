from selenium import webdriver
import os


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_driver_instance(self):

        # choose the baseURL
        base_url = "http://50.108.46.90:6080/"

        # browser driver path Firefox & Chrome
        cur_work_dir = os.getcwd()
        browser_dir = os.path.join(cur_work_dir, 'browser_drivers')
        firefox_driver = os.path.join(browser_dir, 'geckodriver.exe')
        chrome_driver = os.path.join(browser_dir, 'chromedriver.exe')

        if self.browser == 'firefox':
            driver = webdriver.Firefox(executable_path=firefox_driver)

        elif self.browser == 'chrome':
            os.environ["webdriver.chrome.driver"] = chrome_driver
            driver = webdriver.Chrome(chrome_driver)

        else:
            driver = webdriver.Firefox(executable_path=firefox_driver)

        # load application url in the browser
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get(base_url)
        return driver
