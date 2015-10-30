"""Adds all data of "REDAM" to our elasticsearch index.
"""
from elasticsearch import Elasticsearch


es = Elasticsearch()

with open("data/prosecuted_candidates_2014.tsv", "r") as handle:
    data = handle.readlines()

for raw_line in data:
    line = raw_line.strip()
    candidate = line.split("\t")
    doc = {
        "raw_data": ', '.join([
            candidate[2],
            candidate[3],
            candidate[4],
            candidate[1],
            candidate[7],
        ]),
        "source": "candidato_2014",
    }

    res = es.index(index="great_db", doc_type="text", body=doc)
    print("created: {}".format(res['created']))
