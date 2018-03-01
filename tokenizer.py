import re
import json
import nltk
from bs4 import BeautifulSoup
from nltk.stem.porter import *
from pathlib import Path
from collections import defaultdict
import string


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


def parse_page(relative_path):
    page = file_open(relative_path)
    '''Returns tuple where tuple[0] = title of page and tuple [1] is dictionary of parsed word and count'''
    result = defaultdict(int)
    content = page_content(page)
    line_list = []
    for line in content[1].split("\n"):
        line_list.extend(re.findall('[0-9a-zA-Z]+', line))
    tokens = [x for x in line_list if not x in stopwords]
    processed = token_stem(tokens, PorterStemmer())
    for word in processed:
        result[word]+=1
    return (content[0], result)

def page_content(page):
    soup = BeautifulSoup(page, "lxml")
    [s.extract() for s in soup('script')]
    [x.extract() for x in soup("style")]
    return (soup.title.string, soup.get_text().lower())
