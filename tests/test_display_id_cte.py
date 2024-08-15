from typing import Callable

import allure
import pytest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    open_display_id_cte,
    open_registry_catalog,
    transition_element_product_list,
    transition_element_registry_catalog,
)


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('SUPPLIER-PORTAL')
@allure.story('Страница реестра каталога')
@allure.title('Отображение ID СТЕ')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_display_id_cte(make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    app = make_app(browser, device_type)

    open_registry_catalog(app)

    transition_element_registry_catalog(app)

    transition_element_product_list(app)

    open_display_id_cte(app)
