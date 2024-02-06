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
    def admin_login(page):
        page.goto("/")
        page.click("//span[contains(.,'Log In')]")
        assert_that(page.is_visible("//div[@class='title'][contains(.,'Log In')]")).is_true()
        assert_that(page.is_visible("//input[contains(@type,'email')]")).is_true()
        assert_that(page.is_visible("//input[contains(@type,'password')]")).is_true()
        print('Hello')