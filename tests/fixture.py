from assertpy import assert_that
import pdb
import pytest

class Page:
    @pytest.fixture
    def home_page(page):
        page.goto("/")
        assert_that(page.is_visible("//h1[contains(.,'UNLOCK THE POWER OF YOUR FULL POTENCIAL')]")).is_true()
        
class Login:
    @pytest.fixture
    def teacher_login(page):
        page.goto("/")
        page.click("//button[contains(.,'Login')]")
        assert_that(page.is_visible("//h4[contains(.,'Log In Account')]")).is_true()
        assert_that(page.is_visible("//div[contains(@id,'role')]")).is_true()
        assert_that(page.is_visible("//input[contains(@id,'email')]")).is_true()
        assert_that(page.is_visible("//input[contains(@id,'password')]")).is_true()