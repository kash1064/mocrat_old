import requests

import feedparser

from config.environ_config import env

hatebu_it_top_xml_rss = env("HATEBU_IT_TOP_XML_RSS")

def return_tophatebu_itposts():
    feeds = feedparser.parse(hatebu_it_top_xml_rss)
    ret = []
    for i, entry in enumerate(feeds.entries):
        ret.append((entry.title, entry.link))
        if not i < 5:
            break
    
    return ret
