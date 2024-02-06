from assertpy import assert_that
import pdb
import pytest
from fixture import Login


admin_login = Login.admin_login

@pytest.mark.admin
def test_valid_admin_login(page, admin_login):
    page.fill("//input[contains(@type,'email')]", "admin")
    page.fill("//input[contains(@type,'password')]", "admin")
    page.click("//button[contains(.,'LOG IN')]")
    assert_that(page.is_visible("//h1[contains(.,'Welcome to your Dashboard!')]")).is_true()