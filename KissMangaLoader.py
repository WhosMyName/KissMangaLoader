""" some module doc-string """

import os
#import sys
#import re 
import urllib.parse
from argparse import ArgumentParser
import concurrent.futures as cf

import requests
from bs4 import BeautifulSoup, SoupStrainer 

def parse_url(sUrl: str, nNumThreads: int):
    """ WIP """
    pass

def parse_file(sFileName: str, nNumThreads: int):
    """ WIP """
    pass

def open_file(sFileName: str) -> list:
    """ opens a file and returns its content stripped off the newline as list """
    with open(sFileName, "r") as fp:
        return fp.read(os.path.getsize(sFileName)) # temp return for testing with local files
        #return [line for line.strip("\n") in fp]

#######################################CC#######################################

def parse_cc_manga_name(data: str) -> str:
    """ parses the mangas title for mangas from KissManga.cc """
    data = open_file("/home/koro/Documents/GitKrakken/KissMangaLoader/kissmanga.cc.inmanga.html")
    strainer = SoupStrainer(itemprop="title")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].contents[0]

def parse_cc_chaper_list(data: str) -> dict:
    """ parses and returns the mangas chapters as dict """
    pass

def parse_cc_chapter_images(data: str) -> list:
    """ parses all image urls from a given chapter """
    pass

#######################################ORG######################################

def parse_org_manga_name():
    pass

def parse_org_chaper_list():
    pass

def parse_org_chapter_images():
    pass

#######################################IN#######################################

def parse_in_manga_name(data: str) -> str:
    """ parses the mangas title for mangas from KissManga.in """
    data = open_file("/home/koro/Documents/GitKrakken/KissMangaLoader/kissmanga.in.inmanga.html")
    strainer = SoupStrainer(class_="rate-title")
    soup = BeautifulSoup(data, "html.parser", parse_only=strainer)
    return soup.contents[0].contents[0]

def parse_in_chaper_list():
    #
    #<div class="list-chapter">
	#	                    <div class="chapter-item ">
    pass

def parse_in_chapter_images():
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
    print(parse_cc_manga_name(""))
    print(parse_in_manga_name(""))


if __name__ == "__main__":
    __main__()
