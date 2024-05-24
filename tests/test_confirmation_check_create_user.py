from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    fill_simplified_register,
    open_confirmation_create_user,
    open_register_page,
    open_simplified_register_page,
    open_start_page,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Страница регистрации')
@allure.title('Проверка открытия окна подтведждения создания пользователя')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_confirmation_check_create_user(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_start_page(app)

    open_register_page(app)

    open_simplified_register_page(app)

    fill_simplified_register(app)

    open_confirmation_create_user(app)
