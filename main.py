from robots.text_robot import txt_rob
from content.catch_content import Catch_content
import os

class content(object):
    def __init__(self, searchTerm, originalContent, cleanContent):
        self.searchTerm = searchTerm
        self.originalContent = originalContent
        self.cleanContent = cleanContent

    class Scentences(object):
        def __init__(self, text, keywords, image_url):
            self.text = text
            self.keywords = keywords
            self.image_url = image_url

def Start():
    for file in os.listdir(f"{os.getcwd()+'/content/originals/'}"):
        os.remove(f"{os.getcwd()+'/content/originals/'+file}")
    content.searchTerm = str(input('Type an search term: '))
    pdf_path = Catch_content(content)
    txt_rob(content, pdf_path)

if __name__ == '__main__':
    Start()
