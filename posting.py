
class Posting:
    def __init__(self, rel_path):
        # self.url = newUrl
        # self. title = newTitle # May need title of page to make a more relevant search
        # self.frequency_dict = {} # Dictionary of tokenized term in document/webpage
        self.docID = rel_path
        self.freq = 0
        self.tf_idf = None # Score generated later on during search (?)
        """ method that calculates tf-idf"""

    #Methods
