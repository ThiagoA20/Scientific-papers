# https://pubmed.ncbi.nlm.nih.gov/
from robots.text_robot import txt_rob

class content:
    def __init__(self, searchTerm, originalContent, cleanContent, text, keywords, image_url):
        self.searchTerm = searchTerm
        self.originalContent = originalContent
        self.cleanContent = cleanContent
        self.scentences = self.Scentences(text, keywords, image_url)

class Scentences:
    def __init__(self, text, keywords, image_url):
        self.text = text
        self.keywords = keywords
        self.image_url = image_url

def Start(): 
    content.searchTerm = str(input('Type an search term: '))
    txt_rob(content)

if __name__ == '__main__':
    Start()
