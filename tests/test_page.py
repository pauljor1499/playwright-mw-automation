from assertpy import assert_that
import pdb
import pytest

def test_home_page(page):
    page.goto("/")
    assert_that(page.is_visible("//h1[contains(.,'UNLOCK THE POWER OF YOUR FULL POTENCIAL')]")).is_true()
        
def test_login_page(page):
    page.goto("/")
    page.click("//button[contains(.,'Login')]")
    assert_that(page.is_visible("//h4[contains(.,'Log In Account')]")).is_true()
    assert_that(page.is_visible("//div[contains(@id,'role')]")).is_true()
    assert_that(page.is_visible("//input[contains(@id,'email')]")).is_true()
    assert_that(page.is_visible("//input[contains(@id,'password')]")).is_true()