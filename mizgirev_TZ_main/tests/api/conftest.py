import pytest
from src.api.client import ApiClient
from driver import SetupDriver

from src.ui.page_and_helpers.base_page import BasePage
from src.ui.page_and_helpers.helper_user_generator import PersonDataGenerate


@pytest.fixture
def test_data():
    return PersonDataGenerate()


@pytest.fixture
def api_client():
    return ApiClient()
