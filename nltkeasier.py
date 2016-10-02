import nltk
from nltk.tokenize import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
import feedparser

def raw_to_word_tokenize(txtfile):
    txt = nltk.Text(word_tokenize(open(txtfile, 'r').read()))
    return txt

def html_raw_word_tokkenized(url):
    html = request.urlopen(url).read().decode('utf8')
    html = nltk.Text(word_tokenize(html))
    return html

def html_parsed_word_tokenized(url):
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html).get_text()
    tokens = nltk.Text(word_tokenize(raw))
    return tokens

def rss_feed_word_tokenized(url):
    llog = feedparser.parse(url)
    post = llog.entries
    print(post)
    raw = BeautifulSoup(post).get_text()
    tokens = word_tokenize(raw)
    return tokens
