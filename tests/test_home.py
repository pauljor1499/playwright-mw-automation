from assertpy import assert_that
import pdb
import pytest

def test_home_page(page):
    page.goto("/")
    def home_page(page):
        page.goto("/")
        assert_that(page.is_visible("//h1[contains(.,'UNLOCK THE POWER OF YOUR FULL POTENCIAL')]")).is_true()