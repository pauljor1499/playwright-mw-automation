from assertpy import assert_that
import pdb
import pytest
from fixture import Login

def test_home_page(page):
    page.goto("/")
    assert_that(page.is_visible("//h2[contains(.,'MathMatters')]")).is_true()
    print('Home Page')