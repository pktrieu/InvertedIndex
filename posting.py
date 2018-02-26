
class Posting:
    def __init__(self, newUrl, newTitle):
        self.url = newUrl
        self. title = newTitle # May need title of page to make a more relevant search
        self.frequency = {} # Dictionary of tokenized term in document/webpage
        self.tf_idf = None # Score generated later on during search (?)




    #Methods
