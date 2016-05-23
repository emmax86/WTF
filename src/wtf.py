import argparse
from base import *

def main(args):
    term_name = " ".join(args.term).lower()

    if not terms_file_exists():
        if not can_write_terms_file():
            die("Fatal error: Cannot create Terms.json!")
        else:
            make_terms_file()
            print("Term not found\nUse tf to create a new term.")
    
    elif not can_read_terms_file():
            die("Fatal error: Cannot read Terms.json! (Invalid file permissions?)")
    
    else:
        try:
            data = read_term_data()
            if term_name in data:
                print(data[term_name]["proper_capitalization"] + ":")
                print(data[term_name]["description"])
            else:
                print("Term not found!\nUse tf to create a new term")
        except JSONDecodeError:
            # Better to make user explicitly request to rebuild Terms.json with a flag
            # TODO
            die("Fatal error: Terms data appears to be corrupt")
    
if "__main__" == __name__:
    parser = argparse.ArgumentParser(
        description="What's this for?\n Enter a term")
    parser.add_argument("term", nargs="+")

    args = parser.parse_args()

    main(args)
