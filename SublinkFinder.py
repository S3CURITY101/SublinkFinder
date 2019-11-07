#!/usr/bin/python3

"""SublinkFinder.py: For Batang Hamog Republic."""

__author__      = "Batang Hamog"
__copyright__   = "Copyright 2019, Planet Earth"

import os
import argparse


class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def log(lvl, col, msg):
        logger.log(lvl, col + msg + color.END)

print (color.BOLD + color.GREEN +"""
SublinkFinder.py - Finding SubLinks made Easier
Author: Batang Hamog (S3CUR1TY101)
Email: anti.static189@gmail.com
Usage: SublinkFinder.py target site https://website.com Note* include http:// or https:// 

Description: SublinkFinder is a python tool for finding Sublinks
in websites. This tool is the recompile from one liner curl scripts
Instead of just checking one page as most of the tools do, this tool
traverses the website and find all the links and subdomains first.
After that, it starts scanning each and every input on each and every
page that it found while its traversal. It uses small yet effective
payloads to search for Sublinks that can leak some interesting reconnaissance.
""")

parser = argparse.ArgumentParser()

parser.add_argument('-i', action='store', dest='info',
                    help='This basic tool use curl with one line payload that will dumb all the Sublinks of the site enjoy Mga Hamogs! ')
results = parser.parse_args()


hamog = input('SublinkFinder.py: ')
cmd = 'curl {}'.format(hamog) + ' | grep -Po "(\/)((?:[a-zA-Z\-_\:\.0-9\{\}]+))(\/)*((?:[a-zA-Z\-_\:\.0-9\{\}]+))(\/)((?:[a-zA-Z\-_\/\:\.0-9\{\}]+))" | sort -u '
os.system(cmd)



