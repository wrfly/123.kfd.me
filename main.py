#!/usr/bin/env python3
# -*- coding: utf-8 -*

import template

import re
def clean_url(url):
    url =  re.sub('http[s]?://', '', url)
    return url.strip('/')

def open_links(f="list.txt"):
    links = list()
    with open(f) as f:
        for line in f.readlines():
            if line.startswith("//"):
                continue
            x = line.split("#")
            if len(x)!=3:
                print("bad line", line)
                continue
            link = dict()
            link["link"] = x[0].strip("\n")
            link["site"] = clean_url(x[0])
            link["name"] = x[1].strip("\n")
            link["desc"] = x[2].strip("\n")
            links.append(link)
    return links


def write_file(content_left, content_right, file="index.html"):
    elem_left, elem_right = "", ""

    for content in content_left:
        elem = template.elem.format(
            name=content["name"],
            link=content["link"],
            desc=content["desc"],
            site=content["site"],
        )
        elem_left += (elem)

    for content in content_right:
        elem = template.elem.format(
            name=content["name"],
            link=content["link"],
            desc=content["desc"],
            site=content["site"],
        )
        elem_right += (elem)

    left = template.left.format(elements=elem_left)
    right = template.right.format(elements=elem_right)
    home = template.home.format(home=left + right)
    body = home + template.ga + template.footer
    page = template.page.replace('__BODY__', body)
    with open('index.html', 'w') as f:
        f.write(page)

if __name__ == '__main__':
    links = open_links()
    l = int(len(links) / 2)
    write_file(links[:l], links[l:])