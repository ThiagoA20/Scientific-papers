import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def txt_rob(content):
    url = f"https://pubmed.ncbi.nlm.nih.gov/?term={content.searchTerm}"
    print(url)

    option = Options()
    option.headless = True
    driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")

    driver.get(url)

    time.sleep(10)
    driver.quit()
