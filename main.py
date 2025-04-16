import logging
import os
#import re
from datetime import datetime

from dotenv import load_dotenv
from playwright.sync_api import (Browser, Page, 
                                 Playwright, expect, 
                                 sync_playwright)


def context_manager() -> None:
    p: Playwright
    with sync_playwright() as p:
        browser: Browser = p.firefox.launch(headless=False)
        page: Page = browser.new_page()
        page.goto("https://google.com")
        browser.close()

def interactive_mode(headless: bool = False) -> tuple[Browser, Page]:
    p: Playwright = sync_playwright().start()
    browser: Browser = p.firefox.launch(headless=headless)
    page: Page = browser.new_page()
    return browser, page
    
def main() -> None:
    load_dotenv()

    logs_directory: str = os.environ.get("LOGS_DIRECTORY")

    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=rf"logs\{datetime.now().strftime("%Y-%m-%d %a")}.log"
    )

    browser: Browser
    page: Page

    browser, page = interactive_mode()

    page.goto("https://youtube.com")
    page.get_by_placeholder("Search").fill("warriors")
    page.locator("//button[@class='ytSearchboxComponentSearchButton']").click()
    print()

if __name__ == "__main__":
    main()