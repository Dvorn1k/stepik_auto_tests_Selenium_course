from selenium.webdriver.common.by import By


def test_button_add_to_cart(browser):
    button = browser.find_elements(by=By.CSS_SELECTOR, value="button.btn-add-to-basket")
    assert button, "Кнопки нет!"
