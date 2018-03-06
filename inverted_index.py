""" This module is reponsible for the overall construction of the inverted index. This includes the validation  and parsing of URL documents located wihtin
the provided directories.
The order of processes are as follows:
- parse through URLs-> validate URL -> construct new Posting_Object collections """

from collections import defaultdict
import json
from bs4 import BeautifulSoup
import nltk
from pprint import pprint
import posting
import tokenizer

doc_counter = 0
file_path = "C:\\Users\C_los\PycharmProjects\WEBPAGES_RAW\\"
inverted_index = defaultdict(list)
postingsList = list()

def create_index():
    global doc_counter
    bookkeeping_file = open(file_path+'bookkeeping.json', 'r')
    json_object = json.load(bookkeeping_file)
    # pprint(json_object)
    counter = 0
    invalid = 0
    for site in json_object:
        # print(site)
        if counter == 10:
            break
        if json_object[site].endswith(".java") or json_object[site].endswith(".txt") or len(json_object[site]) > 100:
            continue
        tokenizer.parse_page(site, inverted_index)
        counter += 1
        doc_counter += 1
        # print(str(counter))
        # print(inverted_index.items())
    for token, posts in inverted_index.items():
        print("----> TOKEN: " + token + "\n")
        for post in posts:
            print("############## docID: " + post.docID + " frequency: " + str(post.freq) + "\n")
        # posting_obj = posting.Posting(json_object[site], tokenizer.page_content(json_object)[1])
        # for k,v in posting_obj.frequency:
        #     print(k + ": " + v + "\n")
        # print("-----" + posting_obj.url + "-----")
        # print("rel path: " + site + " -- url: " + json_object[site] + "\n")
    bookkeeping_file.close()


def json_to_file(index):
    outfile = open("inverted_index.txt", "w")
    outfile.write("Total number of docs: " + str(doc_counter))
    outfile.write("\nNumber of Unique Words" + str() + "\n")
    # sorted_index = sorted(inverted_index, key = )
    json.dump(inverted_index, outfile, sort_keys=True, indent=4)


if __name__ == '__main__':
    create_index()
    # json_to_file(inverted_index)
    print(" Unique Tokens: " + str(len(inverted_index.keys())))
    print(" Documents counted: " + str(doc_counter))
