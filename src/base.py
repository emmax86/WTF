import argparse
import json
import os
import sys

class FileNotFoundError(Exception):
    pass

class JSONDecodeError(Exception):
    pass

filepath = os.path.join(os.path.expanduser("~"), "Terms.json")

def errlog(msg):
    sys.stderr.write("{}\n".format(msg))

def die():
    exit(1)
    
def die(msg):
    errlog(msg):
    exit(1)

def terms_file_exists():
    return False if not os.path.exists(filepath) else True
    
def make_terms_file():
    with open(filepath, "w") as terms_file:
        terms_file.write("{}")
    
def can_read_terms_file():
    return False if not os.access(filepath, os.R_OK) else True
    
def can_write_terms_file():
    return False if not os.access(filepath, os.W_OK) else True
    
def read_term_data():
    try:
        terms_file = open(filepath, "w+")
        data = json.load(terms_file)
        return terms_file, data
    except IOError:
        raise FileNotFoundError
    except ValueError:
        raise JSONDecodeError()