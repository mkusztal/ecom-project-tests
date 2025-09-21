from selenium.webdriver.common.by import By
from logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logger = get_logger(__name__)


def test_products_dropdown(browser):
    """
    Test: Verify dropdown for products
    """

    # id="collapsible-nav-dropdown"

    products_dropdown_id = "collapsible-nav-dropdown"

    logger.info(
        f"Waiting for products dropdown element using ID: {products_dropdown_id}"
    )

    products_dropdown_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, products_dropdown_id))
    )

    logger.info(
        f"Found products link dropdown element: {products_dropdown_element.text}"
    )

    time.sleep(2)

    products_dropdown_element.click()

    time.sleep(2)

    logger.info("Dropdown clicked")

    dropdown_option = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="responsive-navbar-nav"]/div/div/div/div[1]/a')
        )
    )

    dropdown_option.click()

    assert "yerbamate" in browser.current_url.lower()

    logger.info("Products dropdown verified successfully!")
