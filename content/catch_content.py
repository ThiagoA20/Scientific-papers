import time
import os
import requests
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

cwd = os.getcwd() + '/content'

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", f"{cwd}")
profile.set_preference("browser.download.useDownloadDir", True)
profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.helperApps.neverAsk.openFile", 'application/pdf')
profile.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
profile.set_preference("pdfjs.disabled", True)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

file_names = []

def Catch_content(content):
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={content.searchTerm}"
    print(url)
    i = 0
    o = 0

    option = Options()
    option.headless = True
    driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr", firefox_profile=profile)

    while i < 10:
        driver.get(url)
        time.sleep(1)
        if o > 10:
            driver.find_element_by_xpath("//button[@data-ga-action='show_more']").click()
            time.sleep(2)

        o += 1
        try:
            driver.find_element_by_xpath(f"//a[@data-ga-action='{o}']").click()
            driver.get(f"https://sci-hub.st/{driver.current_url}")
            org = driver.find_element_by_xpath("//a[@href='#']")
            text = org.get_attribute("onclick")
            ind = []
            for index, item in enumerate(text):
                if item == '/':
                    ind.append(index)
                elif item == '?':
                    a = index
            ind = max(ind) + 1
            file_names.append(text[ind:a])
            print(f"Article founds: {i+1}")
            i += 1
        except:
            print('Article not found')
            continue

    for article in file_names:
        print(f"{cwd}/{article}.part")
        while os.path.exists(f"{cwd}/{article}.part"):
            time.sleep(1)
    
    driver.quit()
    return file_names
