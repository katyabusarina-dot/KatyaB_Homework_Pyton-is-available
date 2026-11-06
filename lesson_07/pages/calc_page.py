from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_CALC = (By.XPATH, "//span[text()]")
    RESULT = (By.CLASS_NAME, "screen")

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay_time):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(delay_time)

    def click_button(self, button_text):
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        return self.driver.find_element(*self.RESULT).text
