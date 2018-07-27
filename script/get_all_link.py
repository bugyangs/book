#coding=utf-8
import urllib
import urlparse
import sys
import os
from pyquery import PyQuery as pq

def execute():
    doc = pq(url)
    a_tags = doc("a")
    for a_item in a_tags.items():
        link = a_item.attr("href")
        if link.find("http://") == 0 or link.find("https://") == 0:
            print link
        else:
            print "%s/%s" % (url.strip("/"), link)



def get_domain(url):
    parser = urlparse.urlparse(url)
    if not parser:
        return False
    return parser.netloc


if __name__ == '__main__':
    url = ""
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        print "error"
        exit()
    execute()
