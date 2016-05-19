#!/usr/bin/python

import json
import os
import sys
import traceback

errlog = lambda msg: sys.stderr.write("{}\n".format(msg))

filepath = os.path.join(os.path.expanduser('~'), 'Terms.json')

if os.path.isfile(filepath):
    if os.access(filepath, os.W_OK):
        terms_file = open(filepath, "r+")
        try:
            data = json.load(terms_file)
        except ValueError as e:
            errlog(
                "Error has occurred loading file. File will be regenerated from scratch")
            data = dict()
        finally:
            terms_file.close()
    else:
        errlog("Fatal error! Cannot write to terms file!")
        exit(1)
else:
    errlog("Terms file not found. Creating a new one.")
    terms_file = open(filepath, "w+")
    terms_file.close()
    data = dict()

print("Enter the name of the term you would like to store:")
term_name = ""
while len(term_name) < 1:
    term_name = raw_input()

print("Enter a brief description for the term")
term_desc = ""
while len(term_desc) < 1:
    term_desc = raw_input()

terms_file = open(filepath, "w")
data[term_name.lower()] = {
    "proper_capitalization": term_name, "description": term_desc}
json.dump(data, terms_file)
terms_file.close()
