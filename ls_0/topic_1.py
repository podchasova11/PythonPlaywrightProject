from playwright.sync_api import sync_playwright, Playwright, BrowserContext, Page, expect

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)

page = browser.new_page()
page.goto("https://yahoo.com")
page.wait_for_timeout(3000)

browser.close()
playwright.stop()



