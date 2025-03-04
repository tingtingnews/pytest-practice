from playwright.sync_api import Page, expect
import re


def test_check_uncheck(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    # page.locator("//select[@name='Month']").select_option(['Jan', 'Ap', 'July'])
    page.locator("//select[@name='Month']").select_option( ['Ap', 'July'], index=5, label='February')
    page.wait_for_timeout(4000)
    page.locator("//select[@name='Month']").select_option()
    page.wait_for_timeout(2000)

def test_example2(page: Page) -> None:
    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    multi_sel_dropdown = page.locator("//select[@name='Month']")
    multi_sel_dropdown.select_option(['Sept', 'July', 'May'])
    page.wait_for_timeout(2000)
    # expect(multi_sel_dropdown).to_have_values(['May', 'July', 'Sept'])
    expect(multi_sel_dropdown).to_have_values([re.compile(r"May"), re.compile(r"July"), re.compile(r"Sept")])