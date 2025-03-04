from playwright.sync_api import Page


def test_frame_part2(page: Page) -> None:
    page.goto("https://www.rediff.com/")
    frame = page.frame("moneyiframe")
    mf = page.main_frame
    iframe_locator = get_frame_by_index(mf, 2)
    print(iframe_locator)
    print(type(frame))
    nse_index = frame.locator("span#nseindex")
    print(nse_index.inner_text())
    page.wait_for_timeout(8000)
    #
    # for iframe in page.main_frame.child_frames:
    #     print(iframe.name)
    #     print(len(page.main_frame.child_frames))


def get_frame_by_index(main_frame, index):
    return main_frame.child_frames[index]
