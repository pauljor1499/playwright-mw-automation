from assertpy import assert_that
import pdb
import pytest
from fixture import Login

screenshot_path = './screenshots'
teacher_login = Login.teacher_login

@pytest.mark.admin
def test_valid_teacher_login(page, teacher_login):
    page.fill("//input[contains(@id,'email')]", "teacher@gmail.com")
    page.fill("//input[contains(@id,'password')]", "Teacher123!")
    page.click("//button[contains(@aria-label,'toggle password visibility')]")
    page.click("//button[contains(.,'Sign In')]")
    page.wait_for_timeout(3000)
    page.screenshot(path=f'{screenshot_path}/login.png')
    assert_that(page.is_visible("//h6[contains(.,'Dashboard')]")).is_true()
    assert_that(page.is_visible("//span[contains(.,'Teacher')]")).is_true()