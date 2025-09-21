from logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logger = get_logger(__name__)


def test_scroll_progress_bar(browser):
    """
    Test: Verify animation scroll progress bar with changing color to full green
    """

    scroll_progress_bar_id = "progress-bar"
    logger.info(f"Waiting for scroll bar element using ID: {scroll_progress_bar_id}")

    time.sleep(3)

    scroll_pb_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, scroll_progress_bar_id))
    )

    logger.info(f"Found scroll progress bar: {scroll_pb_element.text}")

    logger.info("Scrolling to bottom of the page...")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    progress_color = scroll_pb_element.value_of_css_property("background-color")
    progress_width = scroll_pb_element.value_of_css_property("width")

    logger.info(f"Progress bar color: {progress_color}")
    logger.info

    actual_color = "#268c51"

    assert actual_color in progress_color or "rgb(38, 140, 81)" in progress_color, (
        f"Progress bar is not actual color: {actual_color}"
    )
    assert float(progress_width.replace("px", "")) > 0, (
        f"Progress bar do not changed the width: {progress_width}"
    )

    logger.info("Scroll progress bar verified successfully")
