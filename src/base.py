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


def die(msg=""):
    if msg:
        errlog(msg)
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
        terms_file = open(filepath, "r+")
        data = json.load(terms_file)
        terms_file.close()
        return data
    except IOError:
        raise FileNotFoundError
    except ValueError:
        raise JSONDecodeError()


def write_term_data(data):
    terms_file = open(filepath, "w+")
    json.dump(data, terms_file)
