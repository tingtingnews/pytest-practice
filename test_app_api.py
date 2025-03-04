import pytest 
from playwright.sync_api import Page

# def test_user_api(page: Page):
#     response = page.goto("https://dummyjson.com/users/1")
#     user_data = response.json()

#     print(user_data)

#     assert "firstName" in user_data
#     assert "lastName" in user_data

#     assert user_data["firstName"] == "Emily"
#     assert user_data["lastName"] == "Johnson"

# import pytest
# from playwright.sync_api import*

# @pytest.fixture
# def api_context(playwright: Playwright) -> APIRequestContext: 
#     api_context = playwright.request.new_context(
#         base_url="https://dummyjson.com"
#     )
#     yield api_context
#     api_context.dispose()

# def test_user_api(api_context: APIRequestContext):
#     query = "Emily"
#     response = api_context.get(f"/users/search?q={query}")

#     users_data = response.json()

#     print("Users found:", users_data["total"])

#     for user in users_data["users"]:
#         print("Checking user:", user["firstName"])
#         assert query in user ["firstName"]

    # assert "firstName" in user_data
    # assert "lastName" in user_data

    # assert user_data["firstName"] == "Emily"
    # assert user_data["lastName"] == "Johnson"


# from playwright.sync_api import Route, Page, expect

# def on_route(route: Route):
#     if route.request.resource_type == "image":
#         route.abort()
#     else:
#         route.continue_()


# def test_docs_link(page:Page):
#     page.route(
#         "**",
#         on_route
#     )
#     page.goto("https://playwright.dev/python")
#     page.screenshot(path="playwright.jpg")






# from playwright.sync_api import Route, Page

# def on_route(route: Route):
#     response = route.fetch()
#     body= response.text().replace(
#         "enables reliable end-to-end testing for modern web apps",
#         "is a awesome gramework for web automation!"
#         )
    
#     route.fulfill(
#         response=response,
#         body=body,
#     )
    

# def test_docs_link(page: Page):
#     page.route(
#         "https://playwright.dev/python",
#         on_route
#     )
#     page.goto("https://playwright.dev/python")
#     page.pause()


# import pytest 
# from playwright.sync_api import*

# @pytest.fixture
# def api_context(playwright: Playwright) -> APIRequestContext:
#     api_context = playwright.request.new_context(
#         base_url="https://dummyjson.com",
#         extra_http_headers={'Content-Type':'application/json'},
#     )
#     yield api_context
#     api_context.dispose()


# def test_create_user(api_context: APIRequestContext):
#     response = api_context.post(
#         "users/add",
#         data={
#             "firstName":"Damien",
#             "lastName":"Smith",
#             "age": 27
#         }
#     )
#     user_data = response.json()
#     print("\n")
#     assert user_data["id"] == 101
#     assert user_data["firstName"] == "Damien"


# def test_update_user(api_context: APIRequestContext):

#     print(api_context.get("user/1").json()["lastName"])

#     response = api_context.put(
#         "users/1",
#         data={
#             "lastName": "Smith",
#             "age": 20,
#         }
#     )
#     user_data = response.json()

#     api_context.delete("users/1")

#     print(user_data)

#     assert user_data["lastName"] == "Smith"
#     assert user_data["age"] == 20

import pytest
from playwright.sync_api import*

# @pytest.fixture
# def api_context(playwright:Playwright):
#     api_context = playwright.request.new_context(
#         base_url="https://dummyjson.com",
#         headers={'Content_Type':'aaplication/json'},
#     )
#     yield api_context
#     api_context.dispoe()

# def test_user_api(api_context: APIRequestContext):
#     query = "John"
#     response = api_context.get("/users/search?q={query}")
#     # response_products = api_context.get("/products")
#     uer_data = response.json()

#     print("Users found:", users_data["total"])
#     for user in users_data["users"]:
#         assert query in user["firstName"]
#     # assert "firstName" in user_data
#     # assert "lastName" in user_data

#     # assert user_data["firstName"] == "Terry"
#     # assert user_data["lastName"] == "Medhurst"

#     # api_context.dispose()



# def on_api_call(route:Route):
#     route.fufill(
#         json={
#             "firstName": "Damian",
#             "lastName": "Smith"
#         }
#     )





# def test_create_user(api_context: APIRequestContext):
#     response = api_context.post(
#         "users/add",
#         data={
#             "firstName":"Damien",
#             "lastName":"Smith",
#             "age":27
#         }
#     )

#     user_data = response.json()
#     assert user_data["id"] == 101
#     assert user_data["firtName"] == Damien


# def test_update_user(api_context:APIRequestContext):

#     print(api_context.get("/users/1").json()["lastName"])
#     api_context.put(
#         "users/1",
#         data={
#             "lastName":"Smith",
#             "age":20,
#         }
#     )
#     uer_data = response.json()
#     assert user_data["lastName"] == "Smith"
#     assert user_data["age"]==20


# page = browser.new_page()
# print("Page loading...")
# start = perf_counter()

# page.oto("https://playwright.dev/python", wait_until='domcontentloaded',)

# time_taken = perf_counter() - start
# print(f"...Page loaded in {round (time_taken, 2)}s")

# browser.close()

# page.wait_for_selector(selector="td.film-title")


# from playwright.sync_api import sync_playwright

# def on_dislog(dialog):
#     print("Dialog opened:", dialog)
#     dialog.accept("Playwright is cool")


# with playwright() as playwright:
#     browser = playwright.chromium.launch(
#         headless=False, slow_mo=200
#     )
#     page = browser.new_page()
#     page.goto('https://testpages.herokuapp.com/style/alerts/alert-test')

#     page.on("dialog", on_dialog)

#     alert_btn = page.get_by_text("Show prompt box")
#     alert_btn.click()

# def on_download(download):
#     print("Download received!")
#     download.save_as("moon.jpg")

# with playwright() as playwright:
#     browser = playwright.chromium.launch(
#         headless=False, slow_mo=200
#     )
#     page = browser.new_page()
#     page.goto('https://testpages.herokuapp.com/style/alerts/alert-test')

# btn = page.get_by_role("link", name="Download Free")
# with page.expect_download() as download_info:
#     btn.click()

# page.once("download", on_download)
# # download = download_info.value
# # download.save_as("moon.jpg")
# browser.close()

num: int = 100
lst: list [int]= [1,2, 3, 4]
dt = dict[str, int] = {"key":0}

def root(num: int) -> float:
    return pow(num, .5)


import json
import response_products
def test_report_json():
    report.generate_report()

def test_report_fields():
    report.generate_report()

    with open("report.json") as file:
        dt = json.load(file)
        assert "timestamp" in dt

def generate_report():
    dt = {
        "timestamp":"2023-4-7"
    }

    with open ("report.json", "w") as file:
        json.dump(dt, file)

def test_report_json():
    report.generate_report()

    with open("resport.json") as file:
        dt = json.load(file)

        assert "timestamp" in dt.keys
        assert "status" in dt