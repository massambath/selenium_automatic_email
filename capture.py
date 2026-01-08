import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.mailer import send_email
from app.config import (
    GRAFANA_URL,
    GRAFANA_USER,
    GRAFANA_PASSWORD,
    DASHBOARD_URLS,
    SCREENSHOTS_DIR,
)


def capture_dashboards():
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    chrome_options = Options()
    #chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options,
    )

    screenshots = []

    try:
        # 1️⃣ Ouvrir Grafana (page login)
        driver.get(GRAFANA_URL)
        time.sleep(3)

        # 2️⃣ Login Grafana
        driver.find_element(By.NAME, "user").send_keys(GRAFANA_USER)
        driver.find_element(By.NAME, "password").send_keys(GRAFANA_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)

        # 3️⃣ Parcours des dashboards
        for idx, dashboard_url in enumerate(DASHBOARD_URLS, start=1):
            driver.get(dashboard_url)

            # laisser le temps aux panels de charger
            time.sleep(10)

            filename = f"dashboard_{idx}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)

            driver.save_screenshot(filepath)
            screenshots.append(filepath)

    finally:
        driver.quit()

    return screenshots

send_email()