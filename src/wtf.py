import argparse

import base


def main(args):
    term_name = " ".join(args.term).lower()

    if not base.terms_file_exists():
        if not base.can_write_terms_file():
            base.die("Fatal error: Cannot create Terms.json!")
        else:
            base.make_terms_file()
            print("Term not found\nUse tf to create a new term.")

    elif not base.can_read_terms_file():
        base.die("Fatal error: Cannot read Terms.json! \
                    (Invalid file permissions?)")

    else:
        try:
            data = base.read_term_data()
            if term_name in data:
                print(data[term_name]["proper_capitalization"] + ":")
                print(data[term_name]["description"])
            else:
                print("Term not found!\nUse tf to create a new term")
        except base.JSONDecodeError:
            # TODO:
            # Better to make user explicitly request to rebuild Terms.json with
            # a flag
            base.die("Fatal error: Terms data appears to be corrupt")

if "__main__" == __name__:
    parser = argparse.ArgumentParser(
        description="What's this for?\n Enter a term")
    parser.add_argument("term", nargs="+")

    args = parser.parse_args()

    main(args)
