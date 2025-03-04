from playwright.sync_api import Page


def test_dynamic_uncheck(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")
    header_menu = page.locator("#menu-item-7128", has_text='FREE EBOOKS')

    print(header_menu.inner_text())
    print(header_menu.count())

    header_menu.hover()
    page.wait_for_timeout(3000)


def get_header_submenu(menu, submenu):
    return f"//div[@class='dark_menu']//a[text()='{menu}']/parent::li/ul[@class='sub-menu']//a[contains(., '{submenu}')]"


def test_select_element_after_hover_over(page: Page) -> None:
    page.goto("https://www.globalsqa.com/demo-site/")
    free_books = page.locator("#menu-item-7128", has_text='FREE EBOOKS')
    print(free_books.all_inner_texts())

    free_books.hover()
    page.wait_for_timeout(3000)
    all_free_books = page.locator("//li[@id='menu-item-7128']//ul[@class='sub-menu']//a")
    print(all_free_books.all_inner_texts())

    free_deep_learning_book = page.locator(get_header_submenu("Free Ebooks", "Deep Learning"))
    free_deep_learning_book.click()
    page.wait_for_timeout(3000)
    print(page.title())
