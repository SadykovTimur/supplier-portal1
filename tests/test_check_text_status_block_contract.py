from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    check_text_status_block_contract_registry,
    open_contract_registry,
    transition_element_contract_registry,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Страница реестра контрактов')
@allure.title('Наличие текста в блоке "Статус контракта"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_check_text_status_block_contract(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_contract_registry(app)

    transition_element_contract_registry(app)

    check_text_status_block_contract_registry(app)
