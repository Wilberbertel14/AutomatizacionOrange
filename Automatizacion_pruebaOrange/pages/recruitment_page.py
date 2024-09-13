from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RecruitmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.recruitment_menu = (By.XPATH, "//span[normalize-space()='Recruitment']")
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        
    def click_recruitment_menu(self):
        # Esperar a que el elemento sea clickeable
        recruitment_element = self.wait.until(EC.element_to_be_clickable(self.recruitment_menu))
        recruitment_element.click()
        
    def click_recruitment_menu(self):
        # Desplazarse hasta el elemento para asegurarse de que esté visible
        recruitment_element = self.wait.until(EC.element_to_be_clickable(self.recruitment_menu))
        self.driver.execute_script("arguments[0].scrollIntoView();", recruitment_element)
        recruitment_element.click()
        
    def click_add_button(self):
        try:
            add_button_element = self.wait.until(EC.element_to_be_clickable(self.add_button))
            add_button_element.click()
        except Exception as e:
            print(f"Error al hacer clic en el botón Add: {e}")
