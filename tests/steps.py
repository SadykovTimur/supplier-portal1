import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from dit.qa.pages.auth_page import AuthPage
from dit.qa.pages.catalog_goods_page import CatalogGoodsPage
from dit.qa.pages.catalog_page import CatalogPage
from dit.qa.pages.contract_registry_page import ContractRegistryPage
from dit.qa.pages.element_contract_registry_page import ElementContractRegistryPage
from dit.qa.pages.element_need_registry_page import ElementNeedRegistryPage
from dit.qa.pages.element_registry_organisation_page import ElementRegistryOrganisationPage
from dit.qa.pages.element_registry_quotation_sessions_page import ElementRegistryQuotationSessionsPage
from dit.qa.pages.need_registry_page import NeedRegistryPage
from dit.qa.pages.product_page import ProductPage
from dit.qa.pages.register_page import RegisterPage
from dit.qa.pages.registry_catalog_page import RegistryCatalogPage
from dit.qa.pages.registry_organisation_page import RegistryOrganisationPage
from dit.qa.pages.registry_quotation_sessions_page import RegistryQuotationSessionsPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.test_link_page import TestLinkPage

__all__ = [
    'open_start_page',
    'open_auth_page',
    'sign_in',
    'open_start_page_after_auth',
    'open_register_page',
    'open_simplified_register_page',
    'fill_simplified_register',
    'open_create_user',
    'open_confirmation_create_user',
    'open_registry_catalog',
    'transition_element_registry_catalog',
    'transition_element_product_list',
    'open_display_id_cte',
    'open_catalog_goods_page',
    'open_registry_quotation_sessions_page',
    'transition_element_registry_quotation_sessions',
    'check_text_status_block_quotation_sessions',
    'open_need_registry',
    'transition_element_need_registry',
    'check_text_status_block_need_procurement',
    'open_contract_registry',
    'transition_element_contract_registry',
    'check_text_status_block_contract_registry',
    'open_registry_organisation',
    'transition_element_registry_organisation',
    'check_server_answer',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def open_register_page(app: Application) -> None:
    with allure.step('Opening Register page'):
        try:
            StartPage(app).menu.registration.click()

            RegisterPage(app).wait_for_loading()

            screenshot_attach(app, 'register_page')
        except Exception as e:
            screenshot_attach(app, 'register_page_error')

            raise e


def open_simplified_register_page(app: Application) -> None:
    with allure.step('Opening Simplified register page'):
        try:
            page = RegisterPage(app)
            page.action_bar.register.click()

            page.wait_transition_register()

            screenshot_attach(app, 'simplified_register_page')
        except Exception as e:
            screenshot_attach(app, 'simplified_register_page_error')

            raise e


def open_auth_page(app: Application) -> None:
    with allure.step('Opening Auth page'):
        try:
            StartPage(app).menu.submit.click()

            AuthPage(app).wait_for_loading()

            screenshot_attach(app, 'auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = AuthPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def fill_simplified_register(app: Application) -> None:
    with allure.step('Fill simplified register'):
        try:
            auth_register = RegisterPage(app)

            auth_register.last_name.send_keys('Орлов')
            auth_register.first_name.send_keys('Геннадий')
            auth_register.middle_name.send_keys('Сергеевич')
            auth_register.email.send_keys('kakzdorov@yandex.ru')
            auth_register.password.send_keys('Kakzdorovo15152')
            auth_register.password_confirm.send_keys('Kakzdorovo15152')

            auth_register.regulation.click()
            ActionChains(app.driver).click(auth_register.agreement.webelement).perform()  # type: ignore[no-untyped-call]

            screenshot_attach(app, 'register_data')
        except Exception as e:
            screenshot_attach(app, 'register_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_register.action_bar.continue_btn.click()


def open_confirmation_create_user(app: Application) -> None:
    with allure.step('Opening Confirmation create user modal'):
        try:
            RegisterPage(app).wait_confirmation_create_user()

            screenshot_attach(app, 'confirmation_create_user_modal')
        except Exception as e:
            screenshot_attach(app, 'confirmation_create_user_modal_error')

            raise e


def open_create_user(app: Application) -> None:
    with allure.step('Opening Create user page'):
        try:
            registry = RegisterPage(app)
            registry.modal.accept.click()
            registry.checkbox[0].webelement.click()
            registry.send.click()

            registry.wait_create_user()

            screenshot_attach(app, 'create_user_page')
        except Exception as e:
            screenshot_attach(app, 'create_user_page_error')

            raise e


def open_start_page_after_auth(app: Application) -> None:
    with allure.step('Opening Start after page'):
        try:
            page = StartPage(app)

            page.wait_for_loading_after_auth()

            screenshot_attach(app, 'start_after_page')
        except Exception as e:
            screenshot_attach(app, 'start_after_page_error')

            raise e


def open_registry_catalog(app: Application) -> None:
    with allure.step('Opening Registry catalog page'):
        try:
            page = RegistryCatalogPage(app)
            page.base_url = 'https://zakupki.mos.ru/catalog/goods/1'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'registry_catalog_page')
        except Exception as e:
            screenshot_attach(app, 'registry_catalog_page_error')

            raise e


def transition_element_registry_catalog(app: Application) -> None:
    with allure.step('Transition Element registry page'):
        try:
            RegistryCatalogPage(app).paper.click()

            CatalogPage(app).wait_for_loading()

            screenshot_attach(app, 'element_registry_page')
        except Exception as e:
            screenshot_attach(app, 'element_registry_page_error')

            raise e


def transition_element_product_list(app: Application) -> None:
    with allure.step('Transition Element product page'):
        try:
            name = CatalogPage(app).choose_item()

            ProductPage(app).wait_for_loading(name)

            screenshot_attach(app, 'element_product_page')
        except Exception as e:
            screenshot_attach(app, 'element_product_page_error')

            raise e


def open_display_id_cte(app: Application) -> None:
    with allure.step('Opening Display id cte page'):
        try:
            ProductPage(app).wait_for_loading_id_cte()

            screenshot_attach(app, 'display_id_cte_page')
        except Exception as e:
            screenshot_attach(app, 'display_id_cte_page_error')

            raise e


def open_catalog_goods_page(app: Application) -> None:
    with allure.step('Opening Catalog page'):
        try:
            page = CatalogGoodsPage(app)
            page.base_url = 'https://zakupki.mos.ru/catalog/goods'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'catalog_page')
        except Exception as e:
            screenshot_attach(app, 'catalog_error')

            raise e


def open_registry_quotation_sessions_page(app: Application) -> None:
    with allure.step('Opening Registry quotation sessions page'):
        try:
            page = RegistryQuotationSessionsPage(app)
            page.base_url = 'https://zakupki.mos.ru/purchase/list?state=%7B%22currentTab%22%3A3%7D'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'registry_quotation_sessions_page')
        except Exception as e:
            screenshot_attach(app, 'registry_quotation_sessions_error')

            raise e


def transition_element_registry_quotation_sessions(app: Application) -> None:
    with allure.step('Transition Element registry quotation sessions page'):
        try:
            name = RegistryQuotationSessionsPage(app).choose_item()
            app.driver.switch_to.window(app.driver.window_handles[1])

            ElementRegistryQuotationSessionsPage(app).wait_for_loading(name)

            screenshot_attach(app, 'element_registry_quotation_sessions_page')
        except Exception as e:
            screenshot_attach(app, 'element_registry_quotation_sessions_page_error')

            raise e


def check_text_status_block_quotation_sessions(app: Application) -> None:
    with allure.step('Checking Status block quotation sessions page'):
        try:
            status = ElementRegistryQuotationSessionsPage(app)

            status.wait_for_loading_status()

            screenshot_attach(app, 'status_block_quotation_sessions_page')
        except Exception as e:
            screenshot_attach(app, 'status_block_quotation_sessions_page_error')

            raise e


def open_need_registry(app: Application) -> None:
    with allure.step('Opening Need registry page'):
        try:
            page = NeedRegistryPage(app)
            page.base_url = 'https://zakupki.mos.ru/purchase/list?state=%7B%22currentTab%22%3A4%7D'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'need_registry_page')
        except Exception as e:
            screenshot_attach(app, 'need_registry_error')

            raise e


def transition_element_need_registry(app: Application) -> None:
    with allure.step('Transition Element need registry page'):
        try:
            name = NeedRegistryPage(app).choose_item()

            ElementNeedRegistryPage(app).wait_for_loading(name)

            screenshot_attach(app, 'element_need_registry_page')
        except Exception as e:
            screenshot_attach(app, 'element_need_registry_page_error')

            raise e


def check_text_status_block_need_procurement(app: Application) -> None:
    with allure.step('Checking Status block need procurement page'):
        try:
            status = ElementNeedRegistryPage(app)

            status.wait_for_loading_status_block()

            screenshot_attach(app, 'status_block_need_procurement_page')
        except Exception as e:
            screenshot_attach(app, 'status_block_need_procurement_page_error')

            raise e


def open_contract_registry(app: Application) -> None:
    with allure.step('Opening Contract registry page'):
        try:
            page = ContractRegistryPage(app)
            page.base_url = 'https://zakupki.mos.ru/contract/list'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'contract_registry_page')
        except Exception as e:
            screenshot_attach(app, 'contract_registry_error')

            raise e


def transition_element_contract_registry(app: Application) -> None:
    with allure.step('Transition Element contact registry page'):
        try:
            name = ContractRegistryPage(app).choose_item()

            ElementContractRegistryPage(app).wait_for_loading(name)

            screenshot_attach(app, 'element_contact_registry_page')
        except Exception as e:
            screenshot_attach(app, 'element_contact_registry_page_error')

            raise e


def check_text_status_block_contract_registry(app: Application) -> None:
    with allure.step('Checking Status block contract registry page'):
        try:
            status = ElementContractRegistryPage(app)

            status.wait_for_loading_status()

            screenshot_attach(app, 'status_block_contract_registry_page')
        except Exception as e:
            screenshot_attach(app, 'status_block_contract_registry_page_error')

            raise e


def open_registry_organisation(app: Application) -> None:
    with allure.step('Opening Registry organisation page'):
        try:
            page = RegistryOrganisationPage(app)
            page.base_url = 'https://zakupki.mos.ru/organization/list'
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'registry_organisation_page')
        except Exception as e:
            screenshot_attach(app, 'registry_organisation_page_error')

            raise e


def transition_element_registry_organisation(app: Application) -> None:
    with allure.step('Transition Element registry organisation page'):
        try:
            name = RegistryOrganisationPage(app).choose_item()

            ElementRegistryOrganisationPage(app).wait_for_loading(name)

            screenshot_attach(app, 'element_registry_organisation_page')
        except Exception as e:
            screenshot_attach(app, 'element_registry_organisation_page_error')

            raise e


def check_server_answer(app: Application, url: str) -> None:
    with allure.step('Checking server answer'):
        try:
            page = TestLinkPage(app)
            page.base_url = url
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'server_answer')
        except Exception as e:
            screenshot_attach(app, 'server_answer_error')

            raise e
