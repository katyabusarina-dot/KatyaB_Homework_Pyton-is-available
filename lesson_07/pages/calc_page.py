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

    def click_button(self,):
        button = self.driver.find_element(*self.BUTTON_CALC)
        button.click()

    def get_result(self):
        result_field = self.driver.EC.text_to_be_present_in_element(
            self.RESULT)
        return result_field.text
