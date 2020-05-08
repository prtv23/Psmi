from pages.home.Login_Page import LoginPage
from utilities.test_result import TestResult
from data.login_page_data import LoginPageData as Data
import pytest
import unittest
import allure

@pytest.mark.usefixtures("onetime_setup", "setup")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.TS = TestResult(self.driver)

    @allure.description("Valid User Login Test Case")
    @allure.severity(severity_level="NORMAL")
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        login_result = self.lp.valid_login(Data.email_id, Data.password)
        self.TS.mark(login_result, "Login Verification")
        page_title_result = self.lp.validate_page_title(Data.psmi_landing_page_title)
        tc_result = self.TS.mark_final(page_title_result, "Page Title Verification")
        assert True == tc_result
        self.lp.sign_out()

    @allure.description("Invalid User Login Test Case")
    @allure.severity(severity_level="HIGH")
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        result = self.lp.invalid_login(Data.email_id, Data.invalid_passwd)
        assert result == True