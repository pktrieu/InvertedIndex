# import inverted_index
from nltk.stem.porter import *
import json

file_path = "C:\\Users\C_los\PycharmProjects\WEBPAGES_RAW\\"

def query_input():
    url_count = 0
    query = input("Search: ")
    processed = PorterStemmer().stem(query)
    index = open("inverted_index.txt", 'r')
    json_index = json.load(index)
    for token in json_index[processed]:
        if url_count >= 5:
            break
        url_count += 1
        print("Url #" + str(url_count) + " : " + grab_url(token))


def grab_url(doc_ID):
    bookkeeping_file = open(file_path+'bookkeeping.json', 'r')
    json_object = json.load(bookkeeping_file)
    return json_object[doc_ID]

if __name__ == '__main__':
    query_input()