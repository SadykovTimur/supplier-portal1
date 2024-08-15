from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_need_registry, transition_element_need_registry


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Страница реестра потребностей')
@allure.title('Переход по первому элементу реестра потребности')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_transition_element_need_registry(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_need_registry(app)

    transition_element_need_registry(app)
