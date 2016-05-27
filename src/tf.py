import base


def main(args):
    if not base.terms_file_exists():
        if not base.can_write_terms_file():
            base.die("Fatal error: Cannot create Terms.json!")
        else:
            base.make_terms_file()

    elif not base.can_write_terms_file():
        base.die("Fatal error: Cannot write to Terms.json! \
                    (Invalid file permissions?)")

    elif not base.can_write_terms_file():
        base.die("Fatal error: Cannot read Terms.json! \
                    (Invalid file permissions?)")

    print("Enter the name of the term you would like to store:")
    term_name = ""
    while len(term_name) < 1:
        term_name = raw_input()

    print("Enter a brief description for the term:")
    term_desc = ""
    while len(term_desc) < 1:
        term_desc = raw_input()

    try:
        data = base.read_term_data()
        if term_name.lower() in data:
            # TODO: add system which allows user to specify whether they want
            # to overwrite
            print("This term already exists")
        else:
            data[term_name.lower()] = {
                "proper_capitalization": term_name, "description": term_desc}
            base.write_term_data(data)
    except ValueError:
            # TODO
            # Better to make user explicitly request to rebuild Terms.json with
            # a flag
        base.die("Fatal error: Terms data appears to be corrupt")

if __name__ == '__main__':
    main([])
