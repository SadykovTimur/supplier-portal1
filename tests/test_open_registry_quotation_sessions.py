from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_registry_quotation_sessions_page


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Стартовая страница')
@allure.title('Открытие страницы реестра котировочных сессий')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_open_registry_quotation_sessions(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_registry_quotation_sessions_page(app)
