""" some module doc-string """

import os
#import sys
import re
import urllib.parse
from argparse import ArgumentParser
import concurrent.futures as cf

import requests
from bs4 import BeautifulSoup, SoupStrainer
from bs4.element import Tag as bs4Tag

CWD = f"{os.path.dirname(os.path.realpath(__file__))}{os.sep}"

def parse_url(sUrl: str, nNumThreads: int):
    """ WIP """
    pass

def parse_file(sFileName: str, nNumThreads: int):
    """ WIP """
    pass

def open_file(sFileName: str) -> list:
    """ opens a file and returns its content stripped off the newline as list """
    with open(sFileName, "r", encoding="utf-8") as fp:
        return fp.read(os.path.getsize(sFileName)) # temp return for testing with local files
        #return [line for line.strip("\n") in fp]

#######################################CC#######################################

def parse_cc_manga_name(data: str) -> str:
    """ parses the mangas title for mangas from KissManga.cc """
    data = open_file(f"{CWD}kissmanga.cc.inmanga.html")
    strainer = SoupStrainer(itemprop="title")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].contents[0]

def parse_cc_chaper_list(data: str) -> dict:
    """ parses and returns the mangas chapters as dict """
    data = open_file(f"{CWD}kissmanga.cc.inmanga.html")
    strainer = SoupStrainer(class_="chapter-list")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    chapters = []
    for elem in soup.contents[0]:
        if not isinstance(elem, bs4Tag):
            continue
        chapters.append({"chapterUrl": elem.a["href"], "chapterName": elem.p.contents[0].split(": ")[1]})
    return chapters # .reverse()

def parse_cc_chapter_images(data: str) -> list:
    """ parses all image urls from a given chapter """
    data = open_file(f"{CWD}kissmanga.cc.inchapter.html")
    strainer = SoupStrainer(id="arraydata")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].string.split(",")

#######################################ORG######################################

def parse_org_manga_name(data: str) -> str:
    """ parses the mangas title for mangas from KissManga.in """
    data = open_file(f"{CWD}kissmanga.org.inmanga.html")
    strainer = SoupStrainer(class_="bigChar")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].contents[0]

def parse_org_chaper_list(data: str) -> list:
    """ parses and returns the mangas chapters as dict """
    data = open_file(f"{CWD}kissmanga.org.inmanga.html")
    strainer = SoupStrainer(class_="listing listing8515 full")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    chapters = []
    rePattern = re.compile(r"\s{2,}")
    for elem in soup.contents[0]:
        if not isinstance(elem, bs4Tag):
            continue
        if elem.a is None:
            continue
        chapterName =  elem.a.contents[0].replace("\n", "").strip()
        chapterName = re.sub(rePattern, " ", chapterName)
        chapters.append({"chapterUrl": elem.a["href"], "chapterName": chapterName})
    return chapters.reverse()

def parse_org_chapter_images():
    """ parses all image urls from a given chapter """
    pass

#######################################IN#######################################

def parse_in_manga_name(data: str) -> str:
    """ parses the mangas title for mangas from KissManga.in """
    data = open_file(f"{CWD}kissmanga.in.inmanga.html")
    strainer = SoupStrainer(class_="rate-title")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].contents[0]

def parse_in_chaper_list():
    """ parses and returns the mangas chapters as dict """
    pass

def parse_in_chapter_images():
    """ parses all image urls from a given chapter """
    pass

################################################################################







def __main__():
    """ MAIN """
    #parser = ArgumentParser(
    #    description="A tiny script that (proga-)magically converts URLs into Mangas",
    #    prog="KissMangaLoader"
    #)
    #argGroup = parser.add_mutually_exclusive_group(required=True)
    #fileSubParserGroup = parser.add_subparsers("Operation Mode: File")
    #urlSubParserGroup = parser.add_subparsers("Operation Mode: URL")
    #argGroup.add_argument(
    #    "-u",
    #    "--url",
    #    help="Input KissManga-URL",
    #    type=str,
    #    dest="url"
    #)
    #argGroup.add_argument(
    #    "-f",
    #    "--file",
    #    help="Input file name KissManga-URL list",
    #    type=str,
    #    dest="file"
    #)
    #parser.add_argument(
    #    "-t",
    #    "--threads",
    #    help="Amount of Threads in the ThreadPool",
    #    type=int,
    #    dest="threads",
    #    default=10
    #)
    #args = parser.parse_args()
    #if len(args) <= 1:
    #    args.print_help()
    #if args.file:
    #    parse_file(args.file, args.threads)
    #elif args.url:
    #    parse_url(args.url, args.threads)
    #else:
    #    exit(0)
    #print(parse_cc_manga_name(""))
    #print(parse_in_manga_name(""))
    #print(parse_org_manga_name(""))
    #print(parse_cc_chaper_list(""))
    #print(parse_cc_chapter_images(""))
    print(parse_org_chaper_list(""))


if __name__ == "__main__":
    __main__()
