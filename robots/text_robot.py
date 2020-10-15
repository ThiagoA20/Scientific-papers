import time
import requests
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 1)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.openFile", 'application/pdf')
profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
profile.set_preference("pdfjs.disabled", True)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

def txt_rob(content):
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={content.searchTerm}"
    print(url)

    option = Options()
    option.headless = True
    driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr", firefox_profile=profile)

    driver.get(url)
    time.sleep(2)

    driver.find_element_by_xpath("//a[@data-ga-action='3']").click()

    time.sleep(2)

    driver.get(f"https://sci-hub.st/{driver.current_url}")

    org = driver.find_element_by_xpath("//a[@href='#']")

    print(org.get_attribute("onclick"))

    time.sleep(5)
    driver.quit()
