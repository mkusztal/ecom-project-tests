import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
from pytest_html import extras
from urllib.parse import quote
from logger import get_logger

ECOM_PROJECT_URL = "https://ecom-project-mk-8e79c4754866.herokuapp.com/"
logger = get_logger(__name__)


@pytest.fixture(scope="function")
def browser():
    logger.info("Starting browser...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    logger.info(f"Navigating to {ECOM_PROJECT_URL}")
    driver.get(ECOM_PROJECT_URL)

    yield driver
    logger.info("Closing browser...")
    driver.quit()


def pytest_runtest_setup(item):
    logger.info(f"===== START TEST: {item.name} =====")


def pytest_runtest_teardown(item):
    logger.info(f"===== END TEST: {item.name} =====")


def pytest_html_report_title(report):
    report.title = "E-com Project Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if not hasattr(report, "extras"):
        report.extras = []

    if report.when != "call" or not report.failed:
        return

    now_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = item.name
    error_msg = str(report.longreprtext)

    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_name = f"{now_date}-{test_name}.png"
    screenshot_local_path = os.path.join(screenshot_dir, screenshot_name)

    logger.error(f"Test '{test_name}' failed at {now_date}\n{error_msg}")
    logger.info(f"Saving screenshot to: {screenshot_local_path}")

    browser = item.funcargs.get("browser", None)

    if browser:
        try:
            browser.save_screenshot(screenshot_local_path)
            logger.info(f"Screenshot saved: {screenshot_name}")
            report.extras.append(extras.image(screenshot_local_path))
        except Exception as e:
            logger.error(f"Error saving screenshot: {e}")
    else:
        logger.warning("WebDriver not found in request node; screenshot skipped.")

    chatgpt_prompt = f"Summarize and explain this test failure:\nTest: {item.name}\nError: {error_msg}"
    chatgpt_url = "https://chat.openai.com/?model=gpt-4&prompt=" + quote(chatgpt_prompt)
    report.extras.append(extras.url(chatgpt_url, name="ChatGPT Analysis"))
    # error_msg += f"\n\n[ChatGPT] Link to the ChatGPT chat: \n\n{chatgpt_url}"
