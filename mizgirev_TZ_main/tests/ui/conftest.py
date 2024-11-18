import pytest
from src.api.client import ApiClient
from driver import SetupDriver

from src.ui.page_and_helpers.base_page import BasePage
from src.ui.page_and_helpers.helper_user_generator import PersonDataGenerate


@pytest.fixture
def base_page():
    return BasePage(SetupDriver.setup_driver())


@pytest.fixture
def test_data():
    return PersonDataGenerate()
