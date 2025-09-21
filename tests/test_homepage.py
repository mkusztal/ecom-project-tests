from selenium.webdriver.common.by import By
from logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger(__name__)


def test_homepage_title(browser):
    """
    Test: Verify homepage title and navbar
    """

    expected_title = "Yours Yerba"
    # xpath_homepage_title = '//*[@id="root"]/div/div[2]/nav/div/div[1]/div/a/span'  # xpath will be swap with id

    homepage_title_id = "navbar-title"
    logger.info(f"Waiting for homepage title element using ID: {homepage_title_id}")

    homepage_title_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, homepage_title_id))
    )

    actual_title = homepage_title_element.text
    logger.info(f"Found homepage title: '{actual_title}'")

    assert expected_title in actual_title, (
        f"Expected title '{expected_title}' but got '{actual_title}'"
    )
    logger.info("Homepage title verified successfully!")
