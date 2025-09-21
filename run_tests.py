import os
import pytest
from datetime import datetime

if __name__ == "__main__":
    reports_dir = os.path.join(os.getcwd(), "reports")
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")

    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    now_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(reports_dir, f"report_{now_date}.html")

    pytest.main(
        [
            "tests",
            f"--html={report_file}",
            "--self-contained-html",
            "--tb=long",
            "-v",
            "--capture=tee-sys",
        ]
    )


# pytest ecom_project_tests/tests --html=ecom_project_tests/reports/manual_report.html --self-contained-html
