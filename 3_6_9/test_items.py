from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_cart(browser):
    browser.get(link)
    button = browser.find_elements(by=By.CSS_SELECTOR, value="button.btn-add-to-basket")
    assert button, "Кнопки нет!"
