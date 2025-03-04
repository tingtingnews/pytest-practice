from playwright.sync_api import Page


def test_dynamic_uncheck(page: Page) -> None:
    page.goto("https://git-scm.com/docs")
    # download_link = page.locator("a", has_text='Download')
    # download_link.click()
    # page.wait_for_timeout(3000)

    # four_elements = page.locator("ul.expanded", has=page.locator("a",has_text="Reference"))
    # text = four_elements.inner_text()
    # print(text)
    # page.wait_for_timeout(3000)

    page.goto("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page.wait_for_timeout(3000)
    print(page.locator("select:has(option[value='AF'])").text_content())
    page.wait_for_timeout(3000)