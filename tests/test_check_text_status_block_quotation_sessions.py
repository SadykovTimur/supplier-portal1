from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    check_text_status_block_quotation_sessions,
    open_registry_quotation_sessions_page,
    transition_element_registry_quotation_sessions,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Страница реестра котировочных сессий')
@allure.title('Наличие текста статуса в блоке "Статус котировочной сессии"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_check_text_status_block_quotation_sessions(
    make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_registry_quotation_sessions_page(app)

    transition_element_registry_quotation_sessions(app)

    check_text_status_block_quotation_sessions(app)
