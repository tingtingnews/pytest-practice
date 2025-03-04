from playwright.sync_api import Page


def test_iframe_1(page: Page) -> None:
    page.goto("https://jqueryui.com/autocomplete/")
    page_element = page.frame_locator("iframe.demo-frame")
    input_field = page_element.locator("input.ui-autocomplete-input")
    input_field.fill("e")
    page.wait_for_timeout(3000)

# def test_iframe_1(page: Page) -> None:
#     page.goto("https://jqueryui.com/autocomplete/")
#     input_field = page.locator("iframe.demo-frame input.ui-autocomplete-input")
#     input_field.fill("e")
#     page.wait_for_timeout(3000)


def test_iframe_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/iframe")
    input_area = page.locator("body#tinymce")
    input_area.type("abcde")
