import time
import os
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

cwd = os.getcwd() + '/content/originals'

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
    print("\n---Choose your database---")
    databases = {1:'PubMed',2:'PubChem',3:'Wikipedia Content',4:'SciElo',5:'Core',6:'arXiv',7:'ERIC'}
    print("\n[1] - PubMed\n[2] - PubChem\n[3] - Wikipedia Content\n[4] - SciElo\n[5] - Core\n[6] - arXiv\n[7] - ERIC\n")
    database = int(input("Database Num: "))
    if database != 3:
        art_amount = int(input("Articles Amount: "))
    else:
        art_amount = 1
    print(f"\nCatching content from: {databases[database]}, Searches Amount: {art_amount}")
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr", firefox_profile=profile, options=option)

    if database == 1:
        url = f"https://pubmed.ncbi.nlm.nih.gov/?term={content.searchTerm}"
        print(url)
        i = 0
        o = 0 
        while i < art_amount:
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
                file_names.append(f"{cwd}/{text[ind:a]}")
                print(f"Article founds: {i+1}")
                i += 1
            except:
                print('Article not found in Sci-hub database')
                continue

        for article in file_names:
            time.sleep(1)
            while os.path.exists(f"{article}.part"):
                print("Waiting the files download...")
                time.sleep(2)
        
        driver.quit()
        return file_names

    elif database == 2:
        driver.quit()
        sys.exit('Working on PubChem... Select another database')

    elif database == 3:
        driver.quit()
        sys.exit('Working on Wikipedia Content... Select another database')

    elif database == 4:
        driver.quit()
        sys.exit('Working on SciElo...Select another database')

    elif database == 5:
        driver.quit()
        sys.exit('Working on Core... Select another database')

    elif database == 6:
        driver.quit()
        sys.exit('Working on arXiv...Select another database')

    elif database == 7:
        driver.quit()
        sys.exit('Working on ERIC...Select another database')

    else:
        driver.quit()
        sys.exit('Invalid database!')
