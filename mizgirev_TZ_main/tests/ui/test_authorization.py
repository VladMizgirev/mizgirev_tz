import allure

from src.ui.locators.locators import CustomBasePageLocators, LoginPageLocators


class TestAuthorizationPage:

    @allure.title("Авторизация - 001")
    @allure.description("Авторизация с неверными данными")
    def test_authorization_failed(self, base_page, test_data):

        with allure.step("Негатив - Вход с фейк данными, проверка появления ошибки"):
            person_random = test_data.get_random_person()
            base_page.move_to_element_and_click(locator=CustomBasePageLocators.LOG_IN_BUTTON)

            base_page.auth_person(person_random)
            assert base_page.element_is_present(
                locator=LoginPageLocators.ERRORE_TITLE), "Ошибка данных авторизации не отобразилась"


