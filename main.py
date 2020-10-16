from robots.text_robot import txt_rob

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
    content.searchTerm = str(input('Type an search term: '))
    content.Scentences.text = 'test'
    txt_rob(content)

if __name__ == '__main__':
    Start()
