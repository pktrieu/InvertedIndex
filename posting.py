
class Posting:
    def __init__(self, newUrl):
        self.url = newUrl
        self.frequency = {} # Dictionary of tokenized term in document/webpage
        self.tf_idf = None # Score generated later on during search (?)



    #Methods
