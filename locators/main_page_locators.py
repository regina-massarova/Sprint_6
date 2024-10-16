from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Локатор кнопки куков
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'  # Локатор вопросов
    QUESTION_LOCATOR_8 = By.XPATH, '//*[@id="accordion__heading-7"]'  # Локатор 8-го вопроса (скроллинг)
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'  # Локатор ответов
    ORDER_BUTTON_TOP_LOCATOR = By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and not(contains(@class, "Button_Middle__1CSJM"))]'  # Локатор кнопки Заказать вверху
    ORDER_BUTTON_BOTTOM_LOCATOR = By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM")]'  # Локатор кнопки Заказать внизу


