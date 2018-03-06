import re
import json
import nltk
from bs4 import BeautifulSoup
from nltk.stem.porter import *
from pathlib import Path
# from collections import defaultdict
# from inverted_index import inverted_index
from posting import Posting
# import string


stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', "did", 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off',
'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def file_open(rel):
    location = Path("C:\\Users\C_los\PycharmProjects\WEBPAGES_RAW\\")
    return location / rel


def token_stem(t, stemmer):
    return [stemmer.stem(word) for word in t]


def parse_page(rel_path, index):
    page = file_open(rel_path)
    '''Returns tuple where tuple[0] = title of page and tuple [1] is dictionary of parsed word and count'''
    # result = defaultdict(int)
    content = page_content(open(page, encoding="utf8"))
    line_list = []
    for line in content.split("\n"):
        line_list.extend(re.findall('[0-9a-zA-Z]+', line))
    tokens = [x for x in line_list if not x in stopwords]
    processed = token_stem(tokens, PorterStemmer())

    for word in processed:
        # have loop ignore
        if len(index[word]) > 0:
            for post in index[word]:
                if post.docID == rel_path:
                    post.freq += 1
                    break
        else:
            post = Posting(rel_path)
            post.freq += 1
            index[word].append(post)

    #for word,posts in index:
    #    print( word + " : " + index[word] )
    # for word in processed:
    #     inverted_index[word]
    #     for post in inverted_index[word]:
    #         if post.docID in inverted_index [word]:
    #             post.freq += 1
    #         inverted[]


def page_content(page):
    soup = BeautifulSoup(page, "lxml")
    [s.extract() for s in soup('script')]
    [x.extract() for x in soup("style")]
    return soup.get_text().lower()
