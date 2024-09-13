from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()  # Maximiza la ventana del navegador al iniciar
        self.wait = WebDriverWait(self.driver, 20)

    def wait_for_element(self, by_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(by_locator))
            return element
        except TimeoutException:
            print(f"Timeout while waiting for element: {by_locator}")
            return None
