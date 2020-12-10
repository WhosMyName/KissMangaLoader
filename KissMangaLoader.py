""" some module doc-string """

import os
#import sys
#import re 
import urllib.parse
from argparse import ArgumentParser
from threading import ThreadPoolExecutor
import concurrent.futures as cf

import requests

def __main__():
    parser = ArgumentParser(
        description="A tiny script that (proga-)magically converts URLs into Mangas",
        prog="KissMangaLoader"
    )
    argGroup = parser.add_mutually_exclusive_group(required=True)
    argGroup.add_argument(
        "-u",
        "--url",
        help="Input KissManga-URL",
        type=str,
        dest="url"
    )
    argGroup.add_argument(
        "-f",
        "--file",
        help="Input file name KissManga-URL list",
        type=str,
        dest="file"
    )
    parser.add_argument(
        "-t",
        "--threads",
        help="Amount of Threads in the ThreadPool",
        type=int,
        dest="threads",
        default=10
    )
    args = parser.parse_args()
    if len(args) <= 1:
        args.print_help()
    if args.file:
        parse_file(args.file, args.threads)
    elif args.url:
        parse_url(args.url, args.threads)
    else:
        exit(0)


if __name__ == "__main__":
    __main__()
