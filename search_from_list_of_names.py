import argparse

from elasticsearch import Elasticsearch


def search(input_filename):
    es = Elasticsearch()
    with open(input_filename, "r") as handle:
        names = handle.readlines()

    for line in names:
        name = line.strip()
        res = es.search(index="great_db", q=name)
        for i in res['hits']['hits']:
            if i['_score'] >= 2.0:
                out = "{0}\t{1}\t{2}\t{3}".format(
                    i['_score'], i['_source']['source'], name, i['_source']['raw_data'],
                )
                print(out)


def main():
    parser = argparse.ArgumentParser(description="Do a search of person's name "
                                                 "in our database. Input is a file "
                                                 "containing one name per line.")
    parser.add_argument('-i', '--input', dest='input_file', action='store',
                        help='filename containing names (one per line).')

    args = parser.parse_args()
    input_filename = args.input_file
    if input_filename:
        search(input_filename)


if __name__ == "__main__":
    main()
